"""
llm.py — Universal LLM client via the OpenAI-compatible API.

Works with any provider that speaks the OpenAI chat-completions format:
OpenAI, Groq, Mistral, Together AI, Ollama, LM Studio, vLLM, company gateways, etc.

Configure with three environment variables:

  LLM_BASE_URL   Base URL of the endpoint   (default: https://api.openai.com/v1)
  LLM_MODEL      Model identifier            (default: gpt-4o-mini)
  LLM_API_KEY    API key                     (falls back to OPENAI_API_KEY; use any
                                              non-empty string for keyless endpoints)

Examples
--------
  # OpenAI
  LLM_BASE_URL=https://api.openai.com/v1
  LLM_MODEL=gpt-4o-mini
  LLM_API_KEY=sk-...

  # Groq (fast inference, generous free tier)
  LLM_BASE_URL=https://api.groq.com/openai/v1
  LLM_MODEL=llama-3.1-8b-instant
  LLM_API_KEY=gsk_...

  # Ollama (local, no key needed)
  LLM_BASE_URL=http://localhost:11434/v1
  LLM_MODEL=llama3.2
  LLM_API_KEY=ollama

  # LM Studio (local)
  LLM_BASE_URL=http://localhost:1234/v1
  LLM_MODEL=local-model
  LLM_API_KEY=lm-studio

  # Any company / internal gateway
  LLM_BASE_URL=http://your-llm-gateway/v1
  LLM_MODEL=your-model-name
  LLM_API_KEY=your-internal-key

Special case — Claude Code (uses the local `claude` CLI, no API key needed):
  LLM_PROVIDER=claude-code
"""

import os
import sys

_PROVIDER = os.environ.get("LLM_PROVIDER", "").lower()


def chat(system: str, user: str, max_tokens: int = 2048) -> str:
    if _PROVIDER == "claude-code":
        return _chat_claude_code(system, user)
    return _chat_openai_compat(system, user, max_tokens)


def _chat_openai_compat(system: str, user: str, max_tokens: int) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("openai package not installed. Run: pip install openai")

    base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
    model    = os.environ.get("LLM_MODEL") or "gpt-4o-mini"
    api_key  = (
        os.environ.get("LLM_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
        or "no-key"  # local endpoints often don't require a key
    )

    client = OpenAI(base_url=base_url, api_key=api_key)
    resp = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
    )
    return resp.choices[0].message.content.strip()


def _chat_claude_code(system: str, user: str) -> str:
    """
    Shell out to the local `claude` CLI (Claude Code).
    No API key required — uses the Claude Code session credentials.
    """
    import shutil
    import subprocess
    import re as _re

    if not shutil.which("claude"):
        sys.exit(
            "claude CLI not found. Install Claude Code: https://claude.ai/code\n"
            "Or set LLM_BASE_URL + LLM_MODEL for any OpenAI-compatible endpoint."
        )

    constraint = (
        "CRITICAL OUTPUT FORMAT: Your response MUST start immediately with the "
        "content itself — no preamble, no explanation, no permission requests. "
        "If writing a Chinese article, begin with the markdown title line (e.g. `# 标题`). "
        "Nothing before it. Nothing after the last line of the content.\n\n"
    )
    prompt = f"{constraint}{system}\n\n---\n\n{user}"
    result = subprocess.run(
        ["claude", "--print"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=300,
    )
    if result.returncode != 0:
        sys.exit(f"claude CLI error:\n{result.stderr.strip()}")

    output = result.stdout.strip()

    # Extract from first markdown heading if Claude added a preamble
    heading_match = _re.search(r"^(#+ .+)$", output, _re.MULTILINE)
    if heading_match:
        output = output[heading_match.start():].strip()

    # Strip trailing meta-commentary lines
    lines = output.split("\n")
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i].strip()
        if line and not any(kw in line for kw in [
            "请确认", "写入权限", "等待", "授权", "保存到", "文件路径",
            "文件已", "以下是", "你可以先", "先预览",
        ]):
            output = "\n".join(lines[:i + 1]).strip()
            break

    return output
