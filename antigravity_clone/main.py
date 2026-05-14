"""
Antigravity Clone — Interactive Chat
Run this to start chatting with your AI coding agent.

Usage:
    python main.py
"""
import sys
from graph import run_agent


BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     🚀 ANTIGRAVITY CLONE — AI Coding Agent                  ║
║                                                              ║
║     Commands:                                                ║
║       • Type anything to chat with the agent                 ║
║       • Type 'exit' or 'quit' to stop                        ║
║       • Type 'clear' to clear screen                         ║
║                                                              ║
║     Capabilities:                                            ║
║       📁 Read/Write/Edit files                               ║
║       💻 Run terminal commands                               ║
║       🌐 Control browser (Playwright)                        ║
║       🔍 Search the web                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


def main():
    print(BANNER)
    
    while True:
        try:
            user_input = input("\n\033[1;36mYou:\033[0m ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        
        if not user_input:
            continue
        
        if user_input.lower() in ("exit", "quit", "q"):
            print("\n👋 Goodbye!")
            break
        
        if user_input.lower() == "clear":
            import os
            os.system("clear" if os.name != "nt" else "cls")
            print(BANNER)
            continue
        
        print("\n\033[1;33m🤖 Thinking...\033[0m\n")
        
        try:
            response = run_agent(user_input)
            print(f"\033[1;32mAgent:\033[0m {response}")
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted. Type 'exit' to quit.")
        except Exception as e:
            print(f"\n\033[1;31m❌ Error:\033[0m {e}")


if __name__ == "__main__":
    main()
