# Content Writing Chinese System — Router

> This file is the **router only**. It tells Claude which template to use.
> All format specs, rules, and checklists live in the respective template files.
> To add a new content domain (e.g. Ethereum, AI), add its templates under `assets/templates/`
> and extend the routing table below.

---

## Zero-config usage

No scripts, no API key, no installation. Use this system in any AI chat window with nothing but this file and a template.

**Step 1 — Open this file and a template in your AI chat**

Paste the contents of `SKILL.MD` (this file) into any AI chat window (ChatGPT, Claude.ai, Gemini, Copilot Chat, etc.). Then paste the contents of the relevant template from `assets/templates/` (see the routing table below to pick the right one).

**Step 2 — Tell the AI what you want to write**

```
Use the following template to write an article. Here is the source content: [paste content]

Intent: [what you want to write, e.g. "analytical piece on staking economics for Chinese Web3 developers"]
```

**Step 3 — Paste your source material**

Paste the source content directly into the chat:
- Web article / blog post — paste the article text
- YouTube video — paste the transcript text (copy from youtube.com/watch → "..." → "Show transcript", or use `youtube-transcript-api` locally)
- Twitter/X thread — paste the thread text

The AI will follow the three-step workflow: generate snippets → produce an English outline for your review → write the Chinese article.

**Supported source types (all work in zero-config mode):**

| Source | How to get the text |
|--------|---------------------|
| Any webpage / blog | Copy and paste the article body |
| YouTube video | Paste the transcript text |
| Twitter / X thread | Paste the thread text |

---

## Global Path Conventions

| Constant | Value |
|------|----|
| `SNIPPET_DIR` | `references/snippets/` |
| `NOTES_DIR` | `references/notes/` |
| `GITHUB_DIR` | `references/GitHub理解/` |
| `OUTPUT_ANALYSIS` | `output/analysis/` |
| `OUTPUT_TUTORIALS` | `output/tutorials/` |
| `OUTPUT_EXPLAINERS` | `output/explainers/` |
| `OUTPUT_SCIENCE_POP` | `output/science-pop/` |
| `OUTPUT_RECAP` | `output/monthly-recap/` |
| `DATE_FORMAT` | `YYYYMMDD` (filename prefix) |
| `ID_FORMAT` | `S-YYYYMMDD-XXXX` (snippet), `N-YYYYMMDD-XXXX` (note) |

---

## Input → Template Routing

| User Input | Trigger Condition | Template to Use | Output Directory |
|---------|---------|---------|---------|
| Any URL or pasted text | Quick capture, for use in monthly recap | `templates/snippet.md` | `SNIPPET_DIR` |
| GitHub link (repo / PR / Issue) | Technical content translation | `templates/github-digest.md` | `GITHUB_DIR` |
| Official documentation URL | Generate how-to tutorial | `templates/polkadot-docs-to-csdn.md` | `OUTPUT_TUTORIALS` |
| Wiki / knowledge base URL | Generate mechanism explainer article | `templates/wiki-to-csdn.md` | `OUTPUT_EXPLAINERS` |
| Blog / Twitter / multi-source links | Remix into original analytical article | `templates/web-remix-to-csdn.md` | `OUTPUT_ANALYSIS` |
| YouTube link | Video content → popular science article | `templates/youtube-remix-to-csdn.md` | `OUTPUT_SCIENCE_POP` |
| Specific month (e.g. `2026-02`) | Summarise all snippets for that month | `templates/monthly-recap.md` | `OUTPUT_RECAP` |
| Description of an event experience | Generate event review report | `templates/event-review.md` | (see template) |
| Existing article / any text, needs AI de-fingerprinting | Standalone de-fingerprinting | `templates/humanizer-zh.md` | (original path) |

---

## Quick Decision Flow

```
User input
   │
   ├── GitHub link?              → github-digest.md
   ├── YouTube link?             → youtube-remix-to-csdn.md
   ├── Official docs link?       → polkadot-docs-to-csdn.md
   ├── Wiki link?                → wiki-to-csdn.md
   ├── Multiple links / blog / X?  → web-remix-to-csdn.md
   ├── Month (YYYY-MM)?          → monthly-recap.md
   ├── Event experience description? → event-review.md
   └── Other                    → snippet.md (default)
```

---

## Writing Style

All article-type outputs must follow:
- `assets/styles/_base.md` — general style (tone, vocabulary, critical perspective)
- `assets/styles/monthly-recap.md` — monthly recap style (inherits from base)

---

## Snippet → Note Upgrade

When snippets on a topic have accumulated enough, tell Claude:

> "Upgrade these snippets into a note: [list of filenames]"

Upgrade logic:
1. Read all specified snippets
2. Extract **invariants** across snippets (mechanisms, core rules)
3. Flag **time-sensitive information** (version parameters, vote results)
4. Generate the new file in note format at `NOTES_DIR`

---

## Template File Index

```
skills/
├── SKILL.MD                          — This file (router)
└── assets/
    ├── styles/
    │   ├── _base.md                  — General writing style
    │   └── monthly-recap.md          — Monthly recap style (inherits _base)
    └── templates/
        ├── snippet.md                — Quick summary snippets
        ├── github-digest.md          — GitHub content translation
        ├── monthly-recap.md          — Monthly recap generation
        ├── polkadot-docs-to-csdn.md  — Official docs → tutorial
        ├── wiki-to-csdn.md           — Wiki → mechanism explainer
        ├── web-remix-to-csdn.md      — Multi-source remix → original article
        ├── youtube-remix-to-csdn.md  — Video → popular science article
        ├── event-review.md           — Event review report
        └── humanizer-zh.md           — AI de-fingerprinting
```
