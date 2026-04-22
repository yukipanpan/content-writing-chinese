# YouTube Video Source → CSDN Original Article Template

## Purpose

Take YouTube video content (extracted via subtitles) and combine it with the existing `output/` article library to produce an original CSDN article with a fresh angle, strong popular-science accessibility, and high readability. Aimed at readers who are not native to blockchain — the goal is to make complex technical concepts understandable through evidence-based explanation and corroboration from existing documents.

**How this differs from other templates**:
- `web-remix-to-csdn.md`: remix of text sources such as blogs / Twitter
- `wiki-to-csdn.md`: translation and restructuring of a single wiki page
- **This template**: YouTube subtitle analysis + existing library integration → original popular-science article

**Core difference**: the special value of video material is that it is conversational, dialogue-driven, and often contains unpolished first-hand judgments and unreleased lines of reasoning. This is a "raw opinion density" that text sources rarely provide. The task of this template is to distil structured insights from this conversational content, then complement it with the rigorous analysis in existing technical articles.

---

## Input

1. **YouTube video link** (one or more)
2. **(Optional) Writing direction hint**: the user may specify a desired angle

---

## Execution Steps

### Step 1: Extract video content

For each input YouTube link, use the `/youtube-ref` skill to retrieve the full subtitles and analysis:

```
/youtube-ref [YouTube URL]
```

Wait for the skill to finish executing and the reference file to be generated, then read the full file and extract:
- Video title, channel, publication date, duration, view count
- Summary
- Key Takeaways
- Full Transcript

**If the youtube-ref skill is unavailable or subtitle retrieval fails**, fall back to manual mode:
```bash
python3 ~/.claude/skills/youtube-ref/scripts/fetch_transcript.py "VIDEO_ID"
```

Organise the video content into a source card (do not output to the user):

```
[Video Source Card]
Source: [YouTube URL]
Title: [Video title]
Channel: [Channel name] · [Duration] · [View count]
Publication date: [Date]
Language: [Subtitle language]
Core topic: [One-sentence summary]
Key arguments:
  - [argument 1]
  - [argument 2]
  - [argument 3]
  - [argument 4]
  - [argument 5]
Quotable lines:
  - "[Speaker's words]" — [timestamp]
  - "[Speaker's words]" — [timestamp]
Key data / details: [if any]
```

#### Deep Video Content Analysis Requirements

Relying only on the Summary and Key Takeaways is not enough. The full subtitles must be read in their entirety, paying attention to:

1. **Details not captured by the summary**: data, analogies, and examples the speaker mentions in passing — these are often the best article material
2. **Reasoning process**: not just conclusions, but how the speaker arrived at them step by step
3. **Points of tension in the dialogue**: follow-up questions from the host, moments where the speaker hesitates or revises their view — these are sources of cognitive tension
4. **Directly quotable lines**: pick out 3–5 sentences with the most force, the most vivid imagery, or the clearest representation of the speaker's core stance — record the timestamps

---

### Step 2: Scan the existing content library

Read the article lists from all subdirectories under `output/`:
- `output/polkadot-hype-articles/`
- `output/monthly-recap/`
- `output/CSDN tutorials/`

Also read reference materials under `references/` (e.g. other youtube-ref files, if any).

Based on the video's topic keywords extracted in Step 1, identify **3–8** of the most relevant existing articles. Quickly scan their titles, summaries, and core sections to extract integration points:

- **Technical in-depth analysis** of topics the video raises — the video's conversational discussion + existing articles' rigorous breakdown = best complement
- **Data, mechanism diagrams, comparison tables** from existing articles — as corroboration for the video's arguments
- **Angles not yet covered** in existing articles — new information the video raises that previous articles have not written about

Compile into an integration list (do not output to the user):

```
[Integration List]
Relevant existing articles:
  - [filename]: integration point → [specific content]
  - [filename]: integration point → [specific content]
Gap opportunities: [information / angles that appear in the video but are not covered by existing articles]
Corroboration pairings: [Video argument A] ← can be corroborated by [Existing article X]'s data / analysis
```

---

### Step 3: Determine article angle and structure

Based on the video source card + integration list, determine the angle.

#### Angle Strategy (choose the most suitable one)

| Strategy | When to Use | Example |
| --- | --- | --- |
| **Insider perspective** | The speaker reveals judgments or plans not in public documents | "Gavin Wood said something nobody noticed — hinting at the real direction of the DOT economic model" |
| **Spoken word vs. whitepaper** | The video's spoken delivery is more direct / more bold than the official docs | "What the whitepaper won't tell you — reading Polkadot's real intentions from an interview" |
| **Multi-video threading** | Videos from different periods / different speakers point to the same trend | "Three statements from three different occasions — assembling Polkadot's true 2026 roadmap" |
| **Video prediction verified** | A prediction / plan in the video compared to what has since happened on-chain | "What he said half a year ago is now happening on-chain" |
| **Popular science translation** | Video content is high-density technical, needs to be made accessible for non-technical readers | "Understand in 10 minutes what Gavin Wood spent 33 minutes explaining" |
| **Overlooked segment** | One small section of the video contains the most important information | "This interview is 33 minutes — the most critical information is only 2 minutes" |

#### Special Requirements for Popular Science Orientation

This template's target audience includes **readers who are not native to blockchain**, so:

1. **Every technical concept must be explained the first time it appears** — in 1–2 sentences, not terminology stacking
2. **Use analogies instead of definitions** — "shared security is like a residential property management company: each unit doesn't need to hire its own security guard — the whole complex shares one security team"
3. **Use concrete scenarios instead of abstract descriptions** — don't say "cross-chain interoperability"; say "an NFT you bought on chain A can be used directly on chain B"
4. **Data needs a reference point** — don't say "6-second block time"; say "a new block every 6 seconds — credit card payment confirmation takes roughly 3–5 seconds, for comparison"

#### Title Strategy

The title must simultaneously satisfy:
1. **Informative**: readers know roughly what the article is about after reading the title
2. **Cognitive tension**: creates curiosity, challenges expectations, or hints at a unique perspective
3. **SEO-friendly**: contains Polkadot-related keywords
4. **Popular science appeal**: can attract readers who are not in blockchain

Title sentence patterns for reference:
- `[Speaker] said [judgment] — what is happening with [topic]`
- `Reading [topic]'s [core change] through a [N]-minute interview`
- `The real inside story of [hot event]: what [speaker] revealed at [occasion]`
- `What exactly is [technical concept]? — A video explains it better than the whitepaper`
- `[Speaker]'s [N] predictions — [M] of them are already happening on-chain`

**Prohibited**:
- Pure information-pile titles: "Polkadot Founder Interview Summary"
- Empty suspense titles: "Shocking! Gavin Wood actually said…"
- Video re-upload titles: "[Video title] — Chinese translation"

#### Article Outline

Generate an outline of 4–7 sections, with each section annotated with its source material. The outline must ensure:

- Opening uses the most impactful line or judgment from the video to create cognitive tension
- Middle has substantive content (video quotes + technical corroboration from existing articles + analogies)
- Closing has an independent judgment (not "let us wait and see")

---

### Step 4: Write the body

#### Writing Style

Follow the base style in `assets/styles/_base.md`:
- Calm observer perspective, not a video re-poster
- Clear stance grounded in facts
- Long sentences as primary form, with em-dashes for supplementary explanations
- Willing to point out problems, acknowledge uncertainty

#### Special Integration Rules for Video Material

**Quoting the speaker's words**:
- Quote 3–5 lines from the video per article (English original + Chinese translation), with timestamps
- Format: `> "[English original]" ([timestamp])`, immediately followed by Chinese translation and analysis
- Selection criteria: statements that most represent the core stance, most surprising, or most thought-provoking
- Do not quote filler, repetitive statements, or pleasantries with no informational content

**Converting spoken content to written form**:
- Spoken expressions from the video need to be distilled and reorganised — do not directly copy the scattered subtitle sentences
- Preserve the speaker's core judgment and reasoning logic, but reorganise in formal written language
- Speaker's hesitation, self-corrections, and self-deprecating humour — if informative, these can be preserved and commented on

**Complementing existing articles**:
- Video mentions a technical concept → link to the complete technical analysis of that concept in an existing article
- Video makes a judgment → use data or mechanism breakdown from an existing article to verify / challenge it
- Abstract analysis in existing articles → use the video's concrete expressions to "ground" them

#### Key Techniques for Popular Science Writing

1. **"Feel first, understand second" principle**: first give a concrete scenario or analogy to build intuition, then give the technical explanation
2. **"One concept per paragraph" principle**: each paragraph explains only one new concept — do not cram multiple terms into a single paragraph
3. **"Delete details the reader doesn't need" principle**: unless it directly supports the argument, do not expand implementation details
4. **"A specific person said this" principle**: quoting specific words from a specific person is more persuasive than abstract summary

#### Format Requirements

```markdown
---
title: [Creative title]
author: Yuki
date: [Date of execution, format YYYY-MM-DD]
source: [YouTube URL]
categories: [category]
tags: [keyword list]
---

> **Abstract**: [under 200 characters — clearly state the article's core argument and what readers will gain]
>
> **Keywords**: [6–10]

---

[Hook paragraph: open with the most impactful quote or judgment from the video, creating cognitive tension]

[Angle paragraph: 1–2 sentences revealing the article's unique perspective]

---

## [Section title — carries a judgment, not a pure statement of fact]

[Body content]

> "[Video quote in English]" ([timestamp])

[Chinese translation + analysis / explanation / corroboration]

---

## 小结 (Summary)

- **[Point 1]**: [one sentence]
- **[Point 2]**: [one sentence]
- **[Point 3]**: [one sentence]

[Closing statement: elevate to a higher level, with force]

---

**References**:
- [Video title](YouTube URL) —— video source
- [Existing article title] —— internal project citations (if specific content was directly cited)
- [Other external links] —— external resources mentioned in the video or otherwise relevant
```

#### Word Count Requirements

- **1,500–4,000 characters** (excluding code blocks and tables)
- Information density takes priority over word count — do not pad
- Each section 200–600 characters, tight pacing

---

### Step 5: AI de-fingerprinting

**Must be executed**. Run the completed body through `templates/humanizer-zh.md` for a full check:

1. Determine the article's style type (usually "WeChat/community popular science article")
2. Scan through all 24 AI writing patterns
3. Rewrite flagged problem passages
4. Overall polish: ensure rhythm variation and natural transitions

**Key de-fingerprinting focus areas**:
- Opening must not use AI boilerplate openers like "In the context of…" or "As… continues to develop…"
- Do not start every paragraph with "it is worth noting that", "in addition", or similar connectors
- Closing must not use hollow endings like "the future is full of hope" or "let us wait and see"
- Do not list three adjectives in parallel: "efficient, secure, flexible"
- Bold text no more than 5 times; em-dashes no more than 3 times
- For popular science articles, pay special attention to: do not adopt a condescending "teaching" posture toward readers — maintain an equal narrative stance

**Note**: de-fingerprinting is applied directly — no need to output a before/after comparison.

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

- [ ] Full subtitles obtained via youtube-ref or manually
- [ ] Full subtitles read in their entirety (not relying only on Summary / Key Takeaways)
- [ ] Scanned the `output/` directory and found relevant existing articles for integration
- [ ] Article angle is original — not a simple translation / re-post of the video content
- [ ] Title has information + cognitive tension + SEO keywords + popular science appeal
- [ ] Opening uses a video quote or core judgment to create cognitive tension
- [ ] Body quotes 3–5 video lines (English + Chinese + timestamp)
- [ ] Key technical concepts explained with analogy or scenario on first appearance
- [ ] Content from existing articles integrated as corroboration, not the main body
- [ ] Humanizer-zh de-fingerprinting check completed — no obvious AI writing patterns
- [ ] Summary at the end (≤5 points + closing statement)
- [ ] References at the end — video link + all citations listed
- [ ] Word count between 1,500 and 4,000
- [ ] Non-blockchain readers can follow along (every term has an explanation, analogies provided)
- [ ] File saved to `output/polkadot-hype-articles/`
