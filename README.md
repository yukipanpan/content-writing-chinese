# Content Writing System

Turn English sources into polished Chinese articles — with any AI, in three steps.

---

## How it works

```
Step 1 — Feed sources        Step 2 — Review outline      Step 3 — Generate article
────────────────────────     ──────────────────────────   ──────────────────────────
URLs or a topic keyword  →   English outline appears   →  Approve → Chinese article
  auto-discover sources       edit angle / sections        saved to output/
  fetch web / YouTube / X     adjust thesis
  save snippets to KB
```

The same workflow runs whether you paste text into ChatGPT, use `/phase1` in Claude Code, run a CLI command, or trigger GitHub Actions.

---

## Quick start

No installation. No API key.

1. Clone the repo
2. Open `skills/SKILL.MD` in any AI chat (ChatGPT, Claude.ai, Gemini…)
3. Paste your source content and describe what you want to write
4. Done — the AI routes to the right template and runs the workflow

For automated URL fetching, YouTube transcripts, and Twitter/X threads: use Layer 2 below.

---

## Four ways to run it

### Layer 0 — Any AI chat, zero setup

Open `skills/SKILL.MD` + a template from `skills/assets/templates/` in any AI interface. Paste your source and intent. No code, no keys, no install.

---

### Layer 1 — Claude Code / Cursor / Copilot

```bash
git clone https://github.com/yukipanpan/content-writing-chinese-system.git
cd content-writing-chinese-system
```

`CLAUDE.md` is auto-loaded as project context. Use slash commands:

```
# From a URL
/phase1 https://polkadot.com/blog/jam-update  intent: analytical piece on JAM

# Auto-discover sources from a topic
/phase1 topic: Polkadot JAM upgrade 2025  intent: analytical piece on JAM

# Both — manual precision + auto breadth
/phase1 https://graypaper.com  topic: Polkadot JAM  intent: deep dive for developers

/generate
/monthly-recap 2026-04
```

---

### Layer 2 — CLI scripts

```bash
pip install -r requirements.txt
cp .env.example .env   # set LLM_BASE_URL + LLM_MODEL + LLM_API_KEY
```

Works with any OpenAI-compatible endpoint — OpenAI, Groq, Mistral, Ollama, LM Studio, or your company's internal gateway. See `.env.example` for provider examples. No API key? Set `LLM_PROVIDER=claude-code` to use the local `claude` CLI.

```bash
# Manual URLs
python3 scripts/run_skill.py phase1 \
  --urls "https://example.com/post, https://youtu.be/xyz" \
  --intent "analytical piece on staking economics" \
  --generate-snippets --pr-body-file pr_body.md

# Auto-discover from topic (uses DuckDuckGo by default, or Serper/Brave with a key)
python3 scripts/run_skill.py phase1 \
  --topic "Polkadot JAM upgrade 2025" \
  --intent "analytical piece on JAM" \
  --top-n 5 --generate-snippets --pr-body-file pr_body.md

# Both
python3 scripts/run_skill.py phase1 \
  --urls "https://graypaper.com" --topic "Polkadot JAM" \
  --intent "deep dive" --generate-snippets --pr-body-file pr_body.md

# Phase 2 — generate Chinese article from approved outline
python3 scripts/run_skill.py phase2 --pr-body-file pr_body.md

# Monthly recap
python3 scripts/run_skill.py monthly-recap --month 2026-04
```

---

### Layer 3 — GitHub Actions

**Actions → Generate Content (Phase 1) → Run workflow**

| Field | Notes |
|-------|-------|
| `source_urls` | Web pages only in CI — YouTube and Twitter/X are IP-blocked by those platforms |
| `intent` | Free text |
| `generate_snippets` | `yes` to save to KB |

A PR opens with the English outline. Review it, then comment `/generate`. The article is committed to the branch.

Setup: add `LLM_BASE_URL`, `LLM_MODEL`, and your API key to **Settings → Secrets and variables → Actions**.

---

## Supported sources

| Source | How | Local | CI |
|--------|-----|-------|----|
| Any webpage / blog | BeautifulSoup scrape | ✅ | ✅ |
| YouTube video | youtube-transcript-api (full transcript) | ✅ | ❌ IP-blocked |
| Twitter / X thread | ADHX API — no key needed | ✅ | ❌ DNS-blocked |

---

## Article types

Inferred automatically from your intent and URLs:

| Type | Template | Output folder |
|------|----------|---------------|
| Analytical / opinion | `web-remix-to-csdn.md` | `output/analysis/` |
| Tutorial (from docs) | `polkadot-docs-to-csdn.md` | `output/tutorials/` |
| Concept explainer | `wiki-to-csdn.md` | `output/explainers/` |
| Pop-science (YouTube) | `youtube-remix-to-csdn.md` | `output/science-pop/` |
| Monthly recap | `monthly-recap.md` | `output/monthly-recap/` |

---

## Knowledge base

Every Phase 1 run with `--generate-snippets` saves structured records to `references/snippets/`. Snippets accumulate and deduplicate automatically — re-fetching a known URL updates the existing snippet instead of creating a duplicate. The monthly recap synthesises all snippets from a given month into one article.

---

## Example outputs

→ [Snippet example](examples/example-snippet.md) — a structured source record saved to the KB

→ [Outline example](examples/example-outline.md) — the English outline that appears after Step 1

→ [Article example](examples/example-article.md) — the Chinese article produced in Step 3

---

## Repository layout

```
.
├── skills/                      ← Templates and routing (the core product)
│   ├── SKILL.MD                 ← Router + zero-config usage guide
│   └── assets/
│       ├── styles/              ← Writing style guides
│       └── templates/           ← One file per article type
├── scripts/
│   ├── run_skill.py             ← Orchestrator (phase1 / phase2 / monthly-recap)
│   ├── fetcher.py               ← URL fetching: web / YouTube / Twitter/X
│   ├── discover.py              ← Topic-based source auto-discovery
│   ├── llm.py                   ← Provider-agnostic LLM client
│   └── snippets.py              ← Snippet generation, dedup, update
├── .github/workflows/           ← GitHub Actions (Layer 3)
├── .claude/commands/            ← Claude Code slash commands (Layer 1)
├── references/snippets/         ← Knowledge base
├── output/                      ← Generated articles
├── examples/                    ← Sample outputs
├── CLAUDE.md                    ← AI assistant project guide
├── .env.example
└── requirements.txt
```
