# Content Writing Chinese System

A two-phase content pipeline for writing high-quality Chinese articles from English sources.

Capture sources → review an English outline → generate a Chinese article for CSDN, WeChat, and monthly recaps.

Works with **Anthropic**, **OpenAI**, or **Ollama** (local). Runs via GitHub Actions, CLI, or as a Python library.

---

## How it works

```
Phase 1                          Review              Phase 2
──────────────────────────────   ──────────────────  ─────────────────────
URLs + intent                    PR opens with       Comment /generate
  → fetch web/YouTube/Twitter    English outline       → Chinese article
  → generate snippets (KB)       ← edit if needed      → committed to PR
  → infer article type
  → English outline
```

---

## Usage

### Option A — GitHub Actions (recommended for teams)

**Step 1 — Submit sources**

> **Actions → Generate Content (Phase 1 — Outline) → Run workflow**

| Field | What to enter |
|-------|--------------|
| `source_urls` | One or more URLs. One per line or comma-separated. |
| `intent` | What you want to write — free text (see examples below). |
| `generate_snippets` | `yes` to save sources into the knowledge base. |

**Intent examples:**
```
"analytical piece on JAM's timeline and what it means for Ethereum developers"
"tutorial on how to set up an RPC node from the official docs"
"summarise this YouTube talk for a Chinese Web3 audience"
"explain the new staking changes to a non-technical reader"
```

A pull request opens with the English outline in the description.

**Step 2 — Review the outline**

Read the PR description. Edit it directly if you want to change the angle or sections. When satisfied, comment `/generate` on the PR.

The Chinese article is committed to the PR branch. Merge when ready.

---

### Option B — CLI

```bash
# Phase 1: fetch sources, generate outline
python3 scripts/run_skill.py phase1 \
  --urls "https://example.com/post, https://youtu.be/xyz" \
  --intent "analytical piece on staking economics" \
  --generate-snippets \
  --pr-body-file pr_body.md

# Review pr_body.md, edit the outline section, then:

# Phase 2: generate Chinese article from approved outline
python3 scripts/run_skill.py phase2 \
  --pr-body-file pr_body.md

# Monthly recap
python3 scripts/run_skill.py monthly-recap --month 2026-04
```

---

### Option C — Monthly recap (automated)

> **Actions → Generate Monthly Recap → Run workflow**

| Field | What to enter |
|-------|--------------|
| `month` | Format: `YYYY-MM` (e.g. `2026-04`) |

Also runs automatically on the 1st of every month.

---

## Article types

The system infers the type automatically from your intent and URLs:

| Type | Template used | Output folder |
|------|--------------|---------------|
| Analytical / opinion | `web-remix-to-csdn.md` | `output/analysis/` |
| Tutorial (from docs) | `polkadot-docs-to-csdn.md` | `output/tutorials/` |
| Concept explainer (from wiki) | `wiki-to-csdn.md` | `output/explainers/` |
| Pop-science (from YouTube) | `youtube-remix-to-csdn.md` | `output/science-pop/` |
| Monthly recap | `monthly-recap.md` | `output/monthly-recap/` |

---

## Setup

### 1. Fork or clone

```bash
git clone https://github.com/yourorg/content-writing-chinese-system.git
cd content-writing-chinese-system
pip install -r requirements.txt
```

### 2. Configure your LLM provider

Copy `.env.example` to `.env` and fill in your key:

```bash
cp .env.example .env
```

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `anthropic` | Choose: `anthropic` \| `openai` \| `ollama` |
| `ANTHROPIC_API_KEY` | — | Required for Anthropic |
| `ANTHROPIC_MODEL` | `claude-haiku-4-5-20251001` | Optional model override |
| `OPENAI_API_KEY` | — | Required for OpenAI |
| `OPENAI_MODEL` | `gpt-4o-mini` | Optional model override |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama endpoint |
| `OLLAMA_MODEL` | `llama3` | Ollama model name |

### 3. For GitHub Actions

Go to **Settings → Secrets and variables → Actions** and add:

- `ANTHROPIC_API_KEY` (or your chosen provider's key)
- `LLM_PROVIDER` (as a variable, not secret) — optional, defaults to `anthropic`

---

## Repository structure

```
.
├── skills/                         ← Prompt templates (the core logic)
│   ├── SKILL.MD                    ← Router: which template to use when
│   └── assets/
│       ├── styles/                 ← Writing style guides
│       └── templates/              ← One file per article type
├── scripts/
│   ├── llm.py                      ← Provider-agnostic LLM client
│   ├── fetcher.py                  ← URL content extraction (web/YouTube/Twitter)
│   ├── snippets.py                 ← Snippet generation, deduplication, update
│   └── run_skill.py                ← Main orchestrator (phase1 / phase2 / monthly-recap)
├── .github/workflows/
│   ├── generate.yml                ← Phase 1: fetch + snippets + outline → PR
│   ├── on-generate-comment.yml     ← Phase 2: /generate comment → Chinese article
│   └── generate-monthly-recap.yml  ← Manual + scheduled monthly recap
├── references/
│   └── snippets/                   ← Accumulated source records (knowledge base)
├── output/
│   ├── analysis/
│   ├── tutorials/
│   ├── explainers/
│   ├── science-pop/
│   └── monthly-recap/
├── .env.example
└── requirements.txt
```

---

## Supported URL types

| Source | How content is extracted |
|--------|--------------------------|
| Any webpage / blog | `requests` + `BeautifulSoup` |
| YouTube | `youtube-transcript-api` (transcript text) |
| Twitter / X | ADHX API (full thread content) |

---

## Output language

Articles are always written in **Chinese (中文)**.
PR descriptions, outlines, and status messages are always in **English**.
