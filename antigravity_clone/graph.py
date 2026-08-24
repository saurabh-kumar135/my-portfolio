"""
Antigravity Clone — LangGraph Agent
  - Direct LLM tool calling (NOT create_react_agent — it breaks on Groq)
  - ALL tools (files, terminal, browser, search)
  - Self-correction: loops until task is done
"""
import os
import json
import time
import re
from dotenv import load_dotenv
load_dotenv()

from langchain_core.globals import set_debug, set_verbose
set_debug(False)   # disabled — floods output and freezes the process
set_verbose(False) # disabled — not needed for web usage

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from prompts import agent_system_prompt

# ── Import all tools ──
from tools.file_tools import read_file, write_file, edit_file, list_files, search_in_files, delete_file
from tools.terminal_tools import run_command
from tools.search_tools import web_search

# Browser tools loaded lazily
try:
    from tools.browser_tools import open_url, click_element, type_text, screenshot, get_page_text, scroll_page, wait_seconds
    BROWSER_TOOLS = [open_url, click_element, type_text, screenshot, get_page_text, scroll_page, wait_seconds]
except Exception:
    BROWSER_TOOLS = []

# ── LLM Setup ──
llm = ChatGroq(
    model=os.getenv("GROQ_MODEL", "qwen/qwen3.6-27b"),
    max_retries=0,
)

# ── Tool registry ──
ALL_TOOLS = [
    read_file, write_file, edit_file, list_files, search_in_files, delete_file,
    run_command, web_search,
] + BROWSER_TOOLS

TOOL_MAP = {t.name: t for t in ALL_TOOLS}

def _tool_descriptions() -> str:
    lines = []
    for t in ALL_TOOLS:
        schema = t.get_input_schema().model_json_schema()
        props  = schema.get("properties", {})
        params = ", ".join(f"{k}: {v.get('type', 'str')}" for k, v in props.items())
        lines.append(f"  • {t.name}({params}) — {t.description}")
    return "\n".join(lines)


def _extract_tool_call(text: str):
    """Extract a JSON tool call from LLM text, even if surrounded by other text."""
    # Method 1: Try parsing the whole text as JSON
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict) and "tool" in parsed:
            return parsed
    except (json.JSONDecodeError, TypeError):
        pass

    # Method 2: Find JSON object with "tool" key using regex
    matches = re.findall(r'\{[^{}]*"tool"\s*:\s*"[^"]+"[^{}]*\}', text)
    for match in matches:
        try:
            parsed = json.loads(match)
            if isinstance(parsed, dict) and "tool" in parsed:
                return parsed
        except (json.JSONDecodeError, TypeError):
            pass

    # Method 3: Find any balanced JSON object containing "tool"
    for i, ch in enumerate(text):
        if ch == '{':
            depth = 0
            for j in range(i, len(text)):
                if text[j] == '{':
                    depth += 1
                elif text[j] == '}':
                    depth -= 1
                if depth == 0:
                    candidate = text[i:j+1]
                    try:
                        parsed = json.loads(candidate)
                        if isinstance(parsed, dict) and "tool" in parsed:
                            return parsed
                    except (json.JSONDecodeError, TypeError):
                        pass
                    break

    return None


# ── Agent node ──
def agent_node(state: dict) -> dict:
    messages  = state.get("messages", [])
    iteration = state.get("iteration", 0)

    system = (
        agent_system_prompt() + "\n\n"
        "AVAILABLE TOOLS:\n" + _tool_descriptions() + "\n\n"
        "TO USE A TOOL, respond with ONLY this JSON (nothing else before or after):\n"
        '{"tool": "tool_name", "args": {"param1": "value1"}}\n\n'
        "RULES:\n"
        "- Send ONLY the JSON object when using a tool. No explanation text.\n"
        "- Use ONE tool per response.\n"
        "- After each tool result, decide: use another tool OR give your final answer.\n"
        "- When DONE, respond with a plain text summary (no JSON)."
    )

    llm_messages = [SystemMessage(content=system)]
    for msg in messages:
        if msg["role"] == "user":
            llm_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            llm_messages.append(AIMessage(content=msg["content"]))
        elif msg["role"] == "tool":
            llm_messages.append(HumanMessage(content=f"[Tool Result]: {msg['content']}"))

    # LLM call with auto-retry on rate limit
    resp = None
    for attempt in range(4):
        try:
            resp = llm.invoke(llm_messages)
            break
        except Exception as e:
            err_str = str(e)
            wait_match = re.search(r'Please try again in (\d+\.?\d*)s', err_str)
            if wait_match and attempt < 3:
                wait_secs = float(wait_match.group(1)) + 2
                time.sleep(wait_secs)
            else:
                raise

    content    = resp.content.strip()
    tool_call  = _extract_tool_call(content)
    new_messages = messages.copy()

    if tool_call:
        tool_name = tool_call["tool"]
        tool_args = tool_call.get("args", {})

        if tool_name in TOOL_MAP:
            try:
                result = TOOL_MAP[tool_name].invoke(tool_args)
            except Exception as e:
                result = f"Tool error: {e}"
        else:
            result = f"Unknown tool: {tool_name}. Available: {list(TOOL_MAP.keys())}"

        new_messages.append({"role": "assistant", "content": json.dumps(tool_call)})
        new_messages.append({"role": "tool",      "content": str(result)})

        return {
            "messages":    new_messages,
            "iteration":   iteration + 1,
            "is_complete": False,
            "response":    None,
        }
    else:
        new_messages.append({"role": "assistant", "content": content})
        return {
            "messages":    new_messages,
            "iteration":   iteration + 1,
            "is_complete": True,
            "response":    content,
        }


# ── Router ──
def should_continue(state: dict) -> str:
    if state.get("is_complete", False) or state.get("iteration", 0) >= state.get("max_iterations", 20):
        return "done"
    return "continue"


# ── Build the graph ──
graph = StateGraph(dict)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue, {"continue": "agent", "done": END})
agent = graph.compile()


def run_agent(user_message: str, conversation_history: list = None) -> str:
    """Run the agent with a user message and return the response."""
    history  = conversation_history or []
    messages = history + [{"role": "user", "content": user_message}]

    result = agent.invoke({
        "messages":       messages,
        "iteration":      0,
        "max_iterations": 20,
        "is_complete":    False,
        "response":       None,
    })

    final_response = result.get("response")

    if not final_response:
        for msg in reversed(result.get("messages", [])):
            role    = msg.get("role", "") if isinstance(msg, dict) else getattr(msg, "role", "")
            content = msg.get("content", "") if isinstance(msg, dict) else getattr(msg, "content", "")
            if role == "assistant" and content and not content.startswith("{"):
                final_response = content
                break
        if not final_response:
            final_response = "Task completed. Please check the workspace for any created files."

    return final_response


if __name__ == "__main__":
    response = run_agent("What tools do you have available? List them all.")
    print(f"\n{'='*60}\n{response}")
