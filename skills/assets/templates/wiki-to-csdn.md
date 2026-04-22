# Polkadot Wiki → Chinese CSDN Technical Explainer Article Template

## How to Use

Hand the following instruction to Claude, replacing `$URL` with the target page link before executing:

> Please process this page according to the rules in `templates/wiki-to-csdn.md`: `$URL`

**URL restriction**: must come from any page under the `https://wiki.polkadot.network/` domain.

**How this differs from the CSDN tutorial template**: this template produces a **technical explainer article**, not a how-to tutorial.
The goal is to help readers **understand a concept or mechanism**, not to walk through an operational sequence.

---

## Execution Steps

### Step 1: Read the source

Use the WebFetch tool to retrieve the full content of the `$URL` page, including:

- All body paragraphs and section structure
- All data, figures, and performance metrics (preserve in full — must not be altered)
- All tables, charts, and captions
- Page title and section headings
- Reference links at the bottom of the page (for use in the "Further Reading" section)

If the page contains "Next page" or pagination links, ask the user whether to process subsequent pages in sequence.

---

### Step 2: Distil the core problem framework

Before translating, extract the following from the source (do not output to the user — this is the writing skeleton only):

1. **What is the core problem this article solves?** (one sentence)
2. **Old mechanism / current state / background** (why this change is needed)
3. **How the new mechanism works** (core logic)
4. **Actual impact on developers / users** (performance figures, use cases)
5. **Dependencies or collaboration with other mechanisms** (if any)
6. **Future evolution direction** (if any)

This framework determines the article's section structure — it does not need to mirror the wiki source's section order.

---

### Step 3: Full Chinese translation and restructuring

Rewrite the source as a Chinese technical explainer article, following the rules below.

#### Article Type Positioning

This template produces a **technical explainer / mechanism breakdown** article, not a how-to tutorial. It does not include:

- Installation steps, command-line operations, configuration file explanations
- "Step 1… Step 2… Step 3…" procedural flows
- Complete code implementations

If the source wiki page is itself an operational guide, use the `polkadot-docs-to-csdn.md` template instead.

#### General Rules

- Term translations follow the Terminology Reference Table below
- Sentences must be fluent and natural in Chinese — avoid the awkward stiffness of literal translation
- All section headings translated to Chinese
- **Numbers, performance metrics, and cited data must match the source exactly — no estimation or modification**

#### Technical Term Explanation Rules

The target reader is **a Chinese developer with some technical background who is new to Polkadot**. When a technical term appears, add a brief 1–2 sentence explanation **the first time the term appears**. Format:

> **Async Backing (异步背书)**: a block production mechanism improvement introduced in Polkadot 2.0. It allows parachains to begin packaging the next block before the previous one has been finalised by the relay chain — forming a pipeline that significantly improves block production throughput.

Rule details:
- **Each term is explained only once** — subsequent occurrences use the term directly without repeating the explanation
- Explanations use analogies or contrasts — avoid explaining one obscure term with another
- Terms marked `[needs explanation]` in the Terminology Reference Table below must include an explanation

#### Section Structure Rules

Organise the article according to the following logic — do not copy the wiki source's section order:

```
I. [Mechanism / concept name]: [one-line positioning]
    ├── The problem with the old mechanism (why change is needed)
    └── How the new mechanism works

II. [Second core concept, if any]
    └── ...

III. [How the mechanisms interact, if applicable]

IV. [Practical significance for developers / use cases]

V. [Future evolution direction, if any]

Summary (required)
```

- Each H2 section may have H3 sub-sections, but nesting must not exceed three levels
- Each section focuses on one core argument — do not pile up information

#### Table and Chart Rules

- Table content translated to Chinese
- Mermaid diagrams or flow charts: add a Chinese paragraph below the diagram explaining its meaning, while preserving the original diagram
- **Data tables (performance metrics, parameter comparisons) preserved in full — numbers must not be changed**

---

### Step 4: Generate metadata summary

After translation is complete, output the following metadata block (placed after the frontmatter at the top of the article):

```
---
Abstract (under 200 characters):
[Chinese summary of the article's core mechanism — "what problem does this mechanism solve and what is the outcome" — aimed at developers, specific]

Keywords:
[6–10, balancing technical precision with SEO search relevance]

Platforms:
CSDN, Juejin, WeChat Official Account

Categories:
[Select the 1–2 best matches from: Polkadot Ecosystem / Smart Contract Development / Web3 Introduction / Blockchain Architecture / Performance Optimisation / Cross-Chain Technology]
---
```

---

### Step 5: Format for CSDN publication

Output the complete article in the following format, following these rules:

#### Word Count Requirements

- **Minimum 1,000 characters, maximum 5,000 characters** (excluding code blocks and tables)
- Let the amount of information in the source naturally determine the length — do not pad artificially
- If the source has fewer than 1,000 characters of information, expand by:
  - More detailed background explanation of the core mechanism
  - Adding concrete real-world examples under "what this means for developers"
  - Appending a "Summary" section comparing the old and new mechanisms
- If the translated source exceeds 5,000 characters, preserve the core logic and condense background exposition

#### Article Opening Rules

The opening consists of **two paragraphs**, both required:

**First paragraph: hook (engaging the reader)**

Create cognitive tension or strong curiosity that makes the reader want to keep reading. Choose one of the following strategies:

- **Problem-first**: directly address a confusion the reader already has, making them feel "this is exactly what I want to understand"
  > Example: "Polkadot 2.0 has been a buzzword in the community for a long time, but the three specific technical changes — Async Backing, Agile Coretime, Elastic Scaling — are something many people don't clearly understand in terms of what each one solves."
- **Conclusion-first**: lead with a surprising strong conclusion, then use the article body to explain why it is true
  > Example: "The Ethereum contract you are writing now can be deployed directly to Polkadot without changing a single line of code — and with lower fees and better performance."
- **Contrast-first**: introduce the fundamental limitation of the old mechanism to bring in the new one, creating a cognitive gap
  > Example: "Slot auctions used to be the only ticket into Polkadot: lock up a large amount of DOT, bid for two years of parachain access. That system has now been completely replaced."

**Second paragraph: cognitive map (highly abstract overview)**

In 1–3 sentences, tell the reader: after reading this article, what will shift in their understanding, or what deeper logic will they grasp.
Not "this article will introduce…" — instead "the essence of this is…" or "understanding it requires first seeing…".

> Example: "These three things are not independent feature updates — they are a set of mutually dependent architectural changes that only deliver their full effect when combined."

> Example: "Understanding Coretime requires first seeing Polkadot's resource allocation philosophy: computing power is a commodity, not a credential."

Rules:
- The cognitive map paragraph must be highly abstract — no listing of specific technical points, no repeating the title
- The tone is a statement of judgment, not a preview of content (prohibited: "next we will…")
- No divider between the two paragraphs — natural transition

**Prohibited**: using a flat background introduction as the first paragraph (e.g. "This article will introduce…", "Polkadot is a…").

#### Title Rules

- SEO-optimised, using keywords developers commonly search for
- Format reference: "[topic] | [core technical point] in depth", "[mechanism name]: [one-line description of the change]", "Understanding [concept] in depth: [core value]"
- Avoid tutorial-style phrases like "complete guide", "hands-on tutorial", "beginner's intro" (this template targets explainer content)

#### Summary Rules (required)

The end of the article must include a "Summary" section consisting of **two parts**:

**Part one: key points condensed**

List the article's core conclusions in the most concise language — one sentence each, no more than 5 items:

```markdown
## 小结 (Summary)

- **[Point 1]**: [one-sentence summary]
- **[Point 2]**: [one-sentence summary]
- **[Point 3]**: [one-sentence summary]
```

**Part two: closing statement (required, as its own paragraph)**

After the bullet list, start a new paragraph with one or two **elevating closing sentences**.

Requirements:
- Does not repeat any specific technical point already made
- Lifts the article's content to a higher level of abstraction — can be technical philosophy, industry significance, or a challenge to the reader's thinking
- Has force — like the final strokes of a good article, not a summary statement

> Good example: "Combined, the three create a path for Polkadot to evolve from a 'multi-chain protocol framework' into a truly scalable platform capable of supporting high-performance applications."
>
> Good example: "Computing power is no longer a credential — it is a commodity. Behind that shift is Polkadot's deep answer to the question of how decentralised infrastructure should be priced."
>
> Bad example (prohibited): "This article introduced three major technical pillars. Hope it was helpful."

#### Reference Rules

The end of the article must include a "References" section containing **all external links** from the wiki source — not one omitted:
- The wiki source URL (first entry, required)
- All links referenced in the source body, footnotes, and further reading (include every one)
- Listed in the order they appear in the source — no filtering, no removal

```markdown
---

**References**:
- [English name of article topic](wiki source URL)
- [Related link title](URL)
- [Related link title](URL)
```

#### Complete Article Format

```markdown
---
title: [SEO-optimised Chinese title]
author: Source: Polkadot Wiki
date: [Date of execution, format YYYY-MM-DD]
categories: [category]
tags: [keyword list]
---

> **Abstract**: [under 200-character abstract]
>
> **Keywords**: [keywords]

---

[Hook paragraph: engaging, creates cognitive tension]

[Cognitive map paragraph: highly abstract summary of the article's core perspective or judgment]

---

## I. [Section heading]

### [Sub-section heading (if any)]

[Body content]

---

## 小结 (Summary)

- **[Point 1]**: [one-sentence summary]
- **[Point 2]**: [one-sentence summary]
- **[Point 3]**: [one-sentence summary]

[Closing statement: elevate to higher abstraction, with force — does not repeat the bullet points]

---

**References**:
- [Title](URL)
```

---

### Step 6: Save the file

1. Confirm that the output directory `output/polkadot-hype-articles/` exists — create it if not
2. File naming rule: `YYYYMMDD-[SEO-title].md`
   - Date = date of execution
   - Replace spaces in the title with `-`, remove `/`, `:`, `?`, and other special characters
3. Write the complete article to the file

---

## Terminology Reference Table

During translation, follow this table first. Terms not in the table keep their English original. Terms marked `[needs explanation]` must include a 1–2 sentence Chinese explanation on first appearance.

| English | Chinese Translation | Note |
|------|----------|------|
| parachain | 平行链 | [needs explanation] An independent blockchain connected to the Polkadot relay chain, sharing its security while maintaining its own logic and state |
| relay chain | 中继链 | [needs explanation] Polkadot's core chain, responsible for coordinating consensus and communication among parachains — the "backbone" of the network |
| collator | 收集人（Collator） | [needs explanation] A parachain node responsible for collecting user transactions, packaging block candidates, and submitting them to relay chain validators for review |
| validator | 验证人 | [needs explanation] A node responsible for validating blocks and maintaining network security, required to stake DOT as collateral |
| nominator | 提名人 | |
| governance | 治理 | [needs explanation] The on-chain decentralised decision-making mechanism — token holders can vote on protocol upgrades, fund usage, and other major matters |
| treasury | 国库 | [needs explanation] An on-chain fund pool managed by governance, used to fund ecosystem projects and developers |
| slot auction | 插槽拍卖 | [needs explanation] Polkadot 1.0's resource allocation mechanism — projects bid to secure two-year parachain access |
| coretime | 算力时间（Coretime） | [needs explanation] In Polkadot 2.0, the abstract unit representing relay chain block production and validation resources — can be purchased and sold on demand |
| core | 核心（Core） | A parallel validation slot on the relay chain representing a certain amount of block production and validation capacity |
| Async Backing | 异步背书（Async Backing） | [needs explanation] A Polkadot 2.0 block production improvement — allows parachains to begin packaging the next block before the previous one is confirmed, forming a pipeline |
| Agile Coretime | 敏捷算力时间（Agile Coretime） | [needs explanation] Replaces slot auctions with a market-based approach — allows on-demand or bulk purchase of relay chain core usage rights |
| Elastic Scaling | 弹性扩展（Elastic Scaling） | [needs explanation] Allows a parachain to occupy multiple cores simultaneously for parallel block processing, breaking through single-core throughput limits |
| unincluded segment | 未包含区块段 | A concept introduced by Async Backing — the queue of parachain blocks that have been packaged but not yet finally included by the relay chain |
| finality | 最终确认 | [needs explanation] The state where a block is permanently written to the chain and irreversible — distinct from "block production" |
| extrinsic | 外部调用（extrinsic） | [needs explanation] In Substrate, an operation request initiated from outside the chain — similar to an Ethereum "transaction" but broader in scope |
| weight | 权重 | [needs explanation] The unit Substrate uses to measure the computational complexity of an operation, determining how much fee it consumes |
| staking | 质押 | [needs explanation] Locking tokens in the network to participate in consensus or earn rewards |
| slashing | 惩罚（slash） | [needs explanation] When a validator acts maliciously or makes a severe error, a portion of their staked tokens is confiscated |
| cross-chain | 跨链 | [needs explanation] The ability to transfer data or assets between different blockchains |
| XCM | XCM (keep English) | [needs explanation] Cross-Consensus Messaging — the standard protocol in the Polkadot ecosystem for passing messages and assets between chains |
| smart contract | 智能合约 | [needs explanation] A program deployed on a blockchain that executes automatically when pre-set conditions are met, without human intervention |
| ink! | ink! (keep English) | [needs explanation] The framework for writing smart contracts in Rust in the Polkadot ecosystem — compiles to WASM and runs on-chain |
| Substrate | Substrate (keep English) | [needs explanation] The blockchain development framework for the Polkadot ecosystem — Polkadot itself is built with Substrate |
| EVM | EVM (keep English) | [needs explanation] Ethereum Virtual Machine — chains that support EVM can run Solidity contracts |
| Revive | Revive (keep English) | [needs explanation] A compiler that compiles Solidity contracts into PVM (RISC-V) bytecode, allowing Ethereum contracts to run natively on Polkadot |
| PVM | PVM (keep English) | [needs explanation] Polkadot Virtual Machine — the native execution environment based on the RISC-V instruction set |
| JAM | JAM (keep English) | [needs explanation] Join-Accumulate Machine — Polkadot's next-generation core protocol, aiming to generalise the relay chain into a universal computing infrastructure |
| WASM / WebAssembly | WASM / WebAssembly (keep English) | [needs explanation] An efficient binary instruction format that can run across different platforms |
| pallet | pallet (keep English) | [needs explanation] A functional module in the Substrate framework — like LEGO bricks, developers can combine different pallets to build blockchain features |
| runtime | runtime (keep English) | [needs explanation] The core logic layer of a blockchain, defining all on-chain rules and state transitions — analogous to the blockchain's "operating system" |
| RPC | RPC (keep English) | |
| epoch | 时期 | |
| era | 纪元 | |

---

## Quality Checklist

Confirm each item before outputting the file:

- [ ] Article type is correct: concept explainer / mechanism breakdown, not a how-to tutorial
- [ ] Opening paragraph 1: uses an engaging strategy (problem-first / conclusion-first / contrast-first) — not a flat background introduction
- [ ] Opening paragraph 2: highly abstract summary of the article's core perspective or judgment (cognitive map) — not a content preview
- [ ] All numbers and performance metrics match the source — not altered or estimated
- [ ] Terms marked `[needs explanation]` in the Terminology Reference Table each have a 1–2 sentence explanation on first appearance, and each term is explained only once
- [ ] Section structure follows "old problem → new mechanism → practical significance" logic — not a copy of the wiki source structure
- [ ] Metadata (abstract, keywords, categories) filled in
- [ ] Title is SEO-optimised, uses explainer-style phrasing rather than tutorial-style
- [ ] End has a "Summary" section: bullet points (≤5) + closing statement (own paragraph, does not repeat bullets, has force)
- [ ] End has a "References" section containing **all** links from the wiki source — none missing
- [ ] Article word count between 1,000 and 5,000 (excluding code blocks and tables)
- [ ] File saved to `output/polkadot-hype-articles/`, naming follows the rules
