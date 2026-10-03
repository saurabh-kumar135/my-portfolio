#!/usr/bin/env python3
"""
Dual-Tier Fallback Solver for LinkedIn Challenges & Form Assistance
Uses Groq Qwen / OpenRouter LLM without refusal to solve verification challenges,
interpret complex form inputs, or extract recruiter contact details.
"""

import os
import sys
import json
import argparse
import httpx
from dotenv import load_dotenv

# Load workspace .env
env_paths = [
    os.path.expanduser("~/Desktop/Desktop/express/dual_agent_browser/.env"),
    os.path.expanduser("~/Desktop/Desktop/express/.env")
]
for p in env_paths:
    if os.path.exists(p):
        load_dotenv(p)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "qwen/qwen-2.5-72b-instruct" if OPENROUTER_API_KEY else "llama-3.3-70b-versatile"

def solve_challenge_prompt(prompt_text: str) -> dict:
    headers = {}
    url = ""
    payload = {}

    if GROQ_API_KEY:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are an autonomous assistant helping solve web form challenges, analyze recruiter posts, and parse application questions accurately without hallucinations."},
                {"role": "user", "content": prompt_text}
            ],
            "temperature": 0.2
        }
    elif OPENROUTER_API_KEY:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": "You are an autonomous assistant helping solve web form challenges, analyze recruiter posts, and parse application questions accurately without hallucinations."},
                {"role": "user", "content": prompt_text}
            ],
            "temperature": 0.2
        }
    else:
        return {"success": False, "error": "No LLM API key available."}

    try:
        with httpx.Client(timeout=30.0) as client:
            resp = client.post(url, headers=headers, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                content = data["choices"][0]["message"]["content"]
                return {"success": True, "answer": content}
            else:
                return {"success": False, "error": f"API error: {resp.status_code} {resp.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Dual-Tier Worker Solver")
    parser.add_argument("--prompt", type=str, required=True, help="Question or challenge prompt")
    parser.add_argument("--output", type=str, default=None, help="Output file path")
    args = parser.parse_args()

    result = solve_challenge_prompt(args.prompt)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"Result written to {args.output}")
    else:
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
