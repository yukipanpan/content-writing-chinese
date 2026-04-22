# Web Source Remix → CSDN Original Article Template

## Purpose

Take external web blogs, Twitter/X posts, and other source material, combine it with the existing `output/` article library, and produce an original CSDN article with a fresh angle, rich content, and strong readability.

**How this differs from other templates**:
- `wiki-to-csdn.md`: translation and restructuring of a single wiki page
- `polkadot-docs-to-csdn.md`: how-to tutorial format
- **This template**: multi-source remix + existing library integration → original article with a new angle

---

## Input

1. **External source links** (at least 1, can mix multiple):
   - Web blog URL (any domain)
   - Twitter/X post link
   - Any other readable web page link
2. **(Optional) Writing direction hint**: the user may specify a desired angle, e.g. "from a developer perspective", "focus on economic model changes", etc.

---

## Execution Steps

### Step 1: Fetch external sources

For each input link:

**Web blog**: use WebFetch to retrieve the full content, extracting:
- Title, author, publication date
- Core arguments and data from the body
- Key data, charts, and code snippets cited in the article

**Twitter/X link**: use the `adhx` skill to fetch the post content, extracting:
- Poster, post time
- Post body (including thread expansion)
- Engagement data (likes, retweets, comments — for reference only, do not include in the article body)
- Links cited in the post (if any, fetch those too)

Organise each source into an internal work card (do not output to the user):

```
[Source Card]
Source: [URL]
Type: Blog / Twitter / Other
Title/Summary: [one sentence]
Core arguments:
  - [argument 1]
  - [argument 2]
  - [argument 3]
Key data: [if any]
Publication date: [date]
```

---

### Step 2: Scan the existing content library

Read the article lists from all subdirectories under `output/`:
- `output/polkadot-hype-articles/`
- `output/monthly-recap/`
- `output/CSDN tutorials/`

Based on the topic keywords extracted in Step 1, identify **3–8** of the most relevant existing articles. Quickly scan their titles, summaries, and core sections to extract integration points:

- **Different angles or deeper analysis** on the same topic from existing articles
- **Data, case studies, technical details** from existing articles that can corroborate this article
- **Gaps not yet covered** in existing articles — these may be the source of novelty for this article

Compile into an integration list (do not output to the user):

```
[Integration List]
Relevant existing articles:
  - [filename]: integration point → [specific content]
  - [filename]: integration point → [specific content]
Gap opportunities: [new angles mentioned in external sources but not covered in existing articles]
```

---

### Step 3: Determine article angle and structure

Based on the source cards + integration list, determine:

#### Angle Strategy (choose the most suitable one)

| Strategy | When to Use | Example |
|------|---------|------|
| **Contrast** | External source conflicts with existing understanding | "The community is bullish, but on-chain data tells a different story" |
| **Trend threading** | Multiple independent events point to the same direction | "Three seemingly unrelated events all point to the same pivot in Polkadot" |
| **Deeper questioning** | A hot event has underlying questions no one is discussing | "Everyone is talking about JAM launching; the question nobody is asking is the real issue" |
| **Timeline reconstruction** | How the same topic evolved across different time periods | "From proposal to launch: how this feature took an 18-month detour" |
| **Outside-in perspective** | Interpreting through a non-blockchain framework | "Viewing Coretime through SaaS pricing logic — what is Polkadot actually selling?" |
| **Overlooked detail** | A small change inside a big event is the real signal | "This Runtime upgrade hid one line of parameter change — with bigger impact than the main feature" |

#### Title Strategy

The title must simultaneously satisfy:
1. **Informative**: readers know roughly what the article is about after reading the title
2. **Cognitive tension**: creates curiosity, challenges expectations, or hints at a unique perspective
3. **SEO-friendly**: contains Polkadot-related keywords

Title sentence patterns for reference (not exhaustive):
- `The [real logic] behind [phenomenon]`
- `Don't just look at [A] — [B] is the real point of this upgrade`
- `From [X] to [Y]: Polkadot is answering a [Z] question`
- `What does [data/fact] tell us? — [N] signals about [topic]`
- `Why [popular opinion] is only half right`
- `[Event A] + [Event B]: the complete picture of Polkadot's [direction]`

**Prohibited**:
- Pure information-pile titles: "Polkadot Latest Developments Summary"
- Empty suspense titles: "Shocking! Polkadot actually…"
- Question-stacking titles: "Can Polkadot do it? Will it go up? Is it worth buying?"

#### Article Outline

Generate an outline of 4–7 sections, with each section annotated with its source material (which external link + which existing article). The outline structure is not fixed — follow the angle — but must ensure:

- Opening creates cognitive tension (not background introduction)
- Middle has substantive content (data, mechanism breakdown, case studies)
- Closing has a strong judgment (not "looking forward to the future")

---

### Step 4: Write the body

#### Writing Style

Follow the base style in `assets/styles/_base.md`:
- Calm observer perspective, not news reporting
- Clear stance grounded in facts
- Long sentences as primary form, with em-dashes for supplementary explanations
- Willing to point out problems, acknowledge uncertainty

#### Source Integration Rules

- **External sources**: extract core arguments and data, restate in your own words — do not copy the original text
- **Existing articles**: cite their analytical frameworks, data, or judgments to support this article's argument, but do not repeat the main thesis of existing articles
- **Integration ratio**: external sources form the main body (60–70%), existing content serves as background and supplement (30–40%)
- **Cite sources**: attribute key data and arguments inline (naturally woven into sentences, e.g. "according to Parity's March blog…")

#### Format Requirements

```markdown
---
title: [Creative title]
author: Source material: [list main source names, separated by /]
date: [Date of execution, format YYYY-MM-DD]
categories: [category]
tags: [keyword list]
---

> **Abstract**: [under 200 characters — clearly state the article's core argument and what readers will gain]
>
> **Keywords**: [6–10]

---

[Hook paragraph: create cognitive tension, make the reader want to continue]

[Angle paragraph: 1–2 sentences revealing the article's unique perspective — not a content preview]

---

## [Section title — carries a judgment, not a pure statement of fact]

[Body content]

---

## 小结 (Summary)

- **[Point 1]**: [one sentence]
- **[Point 2]**: [one sentence]
- **[Point 3]**: [one sentence]

[Closing statement: elevate to a higher level, with force]

---

**References**:
- [Source title](URL) —— external source links (list all)
- [Existing article title] —— internal project citations (if specific content was directly cited)
```

#### Word Count Requirements

- **1,500–4,000 characters** (excluding code blocks and tables)
- Information density takes priority over word count — do not pad
- Each section 200–600 characters, tight pacing

---

### Step 5: AI de-fingerprinting

**Must be executed**. Run the completed body through `templates/humanizer-zh.md` for a full check:

1. Determine the article's style type (usually "WeChat/community article" or "academic/technical in-depth article")
2. Scan through all 24 AI writing patterns
3. Rewrite flagged problem passages
4. Overall polish: ensure rhythm variation and natural transitions

**Key de-fingerprinting focus areas**:
- Opening must not use AI boilerplate openers like "In the context of…" or "As… continues to develop…"
- Do not start every paragraph with "it is worth noting that", "in addition", or similar connectors
- Closing must not use hollow endings like "the future is full of hope" or "let us wait and see"
- Do not list three adjectives in parallel: "efficient, secure, flexible"
- Bold text no more than 5 times; em-dashes no more than 3 times

**Note**: de-fingerprinting is applied directly to the body text — no need to output a before/after comparison (that format is for standalone use of humanizer). In this template, de-fingerprinting is part of the writing workflow; output the final version directly.

---

### Step 6: Save the file

1. Confirm that the output directory `output/polkadot-hype-articles/` exists
2. File naming: `YYYYMMDD-[SEO-title-keywords].md`
   - Date = date of execution
   - Replace spaces in the title with `-`, remove special characters
   - Keep length under 50 characters
3. Write the complete article to the file

---

## Quality Checklist

Confirm each item before outputting the file:

- [ ] At least 1 external source link's content was fetched
- [ ] Scanned the `output/` directory and found relevant existing articles for integration
- [ ] Article angle is original — not a simple translation / copy of the external sources
- [ ] Title has information + cognitive tension + SEO keywords
- [ ] Opening creates cognitive tension (not background setup)
- [ ] Key data and arguments in the body are attributed to their sources
- [ ] Content from existing articles is integrated as supplement, not the main body
- [ ] Humanizer-zh de-fingerprinting check completed — no obvious AI writing patterns
- [ ] Summary at the end (≤5 points + closing statement)
- [ ] References at the end — all external source links listed
- [ ] Word count between 1,500 and 4,000
- [ ] File saved to `output/polkadot-hype-articles/`
