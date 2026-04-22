# Content Writing Chinese System

A Claude-powered content production system for writing high-quality Chinese articles from multiple English sources.

Captures sources → generates structured snippets → produces Chinese articles for CSDN, WeChat, and monthly recaps.

---

## What This Produces

| Type | Folder | Description |
|------|--------|-------------|
| Analysis / Opinion | `output/analysis/` | Multi-source analytical articles |
| Tutorials | `output/tutorials/` | Step-by-step developer how-to guides |
| Concept explainers | `output/explainers/` | Mechanism deep-dives from wiki/docs |
| Pop-science | `output/science-pop/` | YouTube-based accessible articles |
| Monthly recaps | `output/monthly-recap/` | Aggregated monthly digests |
| Snippets | `references/snippets/` | Source records, versioned and deduplicated |

---

## How to Use

### Generate an article (Phase 1 — submit sources)

> **Actions → Generate Content (Phase 1 — Outline) → Run workflow**

| Field | What to enter |
|-------|--------------|
| `source_urls` | One or more URLs — blog posts, YouTube links, Twitter/X threads, docs pages. One per line or comma-separated. |
| `intent` | Free-text description of what you want to write. Examples below. |
| `generate_snippets` | `yes` to save sources into the knowledge base (recommended). Duplicates are auto-merged. |

**Intent examples:**

```
"analytical piece on JAM's timeline and what it means for Ethereum developers"
"tutorial on how to set up an RPC node from the official docs"
"summarise this YouTube talk for a Chinese Web3 audience"
"explain the new staking changes to a non-technical reader"
```

The system automatically:
- Fetches content from all URLs (web pages, YouTube transcripts, Twitter/X threads)
- Generates and deduplicates snippets if requested
- Infers the article type from your intent
- Produces an English outline

A pull request opens with the outline in the description.

---

### Review and approve the outline (Phase 2)

The PR description contains the English outline. You can:
- **Read it** to confirm the angle and coverage
- **Edit it directly** in the PR description to adjust sections or claims
- When satisfied, **comment `/generate`** on the PR

The system generates the Chinese article and commits it to the PR branch. Merge when ready.

---

### Generate a monthly recap

> **Actions → Generate Monthly Recap → Run workflow**

| Field | What to enter |
|-------|--------------|
| `month` | Format: `YYYY-MM` (e.g. `2026-04`) |

Also runs automatically on the 1st of every month covering the previous month.

---

## Repository Structure

```
.
├── skills/                     ← Claude prompt templates (the core logic)
│   ├── SKILL.MD                ← Router: which template to use when
│   └── assets/
│       ├── styles/             ← Writing style guides
│       └── templates/          ← One file per article/snippet type
├── scripts/
│   ├── fetcher.py              ← URL content extraction (web/YouTube/Twitter)
│   ├── snippets.py             ← Snippet generation, deduplication, update
│   └── run_skill.py            ← Main orchestrator (phase1 / phase2 / monthly-recap)
├── .github/workflows/
│   ├── generate.yml            ← Phase 1: fetch + snippets + outline → PR
│   ├── on-generate-comment.yml ← Phase 2: /generate comment → Chinese article
│   └── generate-monthly-recap.yml
├── references/
│   └── snippets/               ← Accumulated source records
├── output/
│   ├── analysis/
│   ├── tutorials/
│   ├── explainers/
│   ├── science-pop/
│   └── monthly-recap/
└── requirements.txt
```

---

## Setup

1. Fork or clone this repository
2. Go to **Settings → Secrets and variables → Actions**
3. Add a secret named `ANTHROPIC_API_KEY` with your Anthropic API key
4. Done — all three workflows are ready to run

---

## Supported URL Types

| Source | How content is extracted |
|--------|--------------------------|
| Any webpage / blog | `requests` + `BeautifulSoup` (main content only) |
| YouTube | `youtube-transcript-api` (transcript text) |
| Twitter / X | ADHX API (full thread + article content) |

---

## Article Output Language

Articles are always written in **Chinese (中文)**.
The PR description (outline, status messages, instructions) is always in **English**.

Use browser translation to read the generated articles if needed.
