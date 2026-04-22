# Polkadot Docs → Chinese CSDN Article Template

## How to Use

Hand the following instruction to Claude, replacing `$URL` with the target page link before executing:

> Please process this page according to the rules in `templates/polkadot-docs-to-csdn.md`: `$URL`

**URL restriction**: must come from any page under the `https://docs.polkadot.com/` domain.

---

## Execution Steps

### Step 1: Read the source

Use the WebFetch tool to retrieve the full content of the `$URL` page, including:

- All body paragraphs and section structure
- All code blocks (preserve in full — must not be truncated)
- All tables, Mermaid diagrams, illustrations, and captions
- Page title and section headings

If the page contains "Next page" or pagination links, ask the user whether to process subsequent pages in sequence.

---

### Step 2: Full Chinese translation

Translate the entire source into Chinese, following the rules below.

#### General Rules

- Term translations follow the Terminology Reference Table below
- Sentences must be fluent and natural in Chinese — avoid the awkward stiffness of literal translation
- All section headings and sub-headings translated to Chinese

#### Technical Term Explanation Rules

The target reader is **an entry-level developer who has just entered Web3**. When a technical term appears, add a brief 1–2 sentence explanation **the first time the term appears**. Format:

> **EVM** (Ethereum Virtual Machine): the runtime environment Ethereum uses to execute smart contracts — essentially the "interpreter" for contract code. Any blockchain that supports EVM can run contracts written for Ethereum directly.

Rule details:
- **Each term is explained only once** — subsequent occurrences use the term directly without repeating the explanation
- Explanations must be concise — use analogies or contrasts, avoid explaining one obscure term with another
- Terms marked `[needs explanation]` in the Terminology Reference Table below must include an explanation; for other unmarked terms, use judgment based on context — add an explanation if a beginner developer would find the term unfamiliar

#### Code Block Rules

- Code content **preserved in full** — must not delete, modify, or replace any line
- English comments: keep the original, and add a Chinese explanation on a **new line below**, format:
  ```
  // Original English comment
  // 中文：corresponding Chinese explanation
  ```
- Keep the language annotation on the code block (e.g. ` ```rust `, ` ```solidity `)

#### Chart / Table Rules

- Table text translated to Chinese
- Mermaid diagrams or illustrations: add a Chinese explanation paragraph **below** the diagram
- **Preserve the original English version of the chart** — show both Chinese and English side by side in the following format:

  ```
  <!-- Chinese version -->
  [Translated table or diagram]

  <!-- English original -->
  [Original table or diagram]
  ```

---

### Step 3: Generate metadata summary

After translation is complete, output the following metadata block (placed at the end of the translation, before the article body):

```
---
Abstract (under 300 characters):
[Chinese summary of the article's core content, aimed at developers — explain what the article covers and its practical value]

Keywords:
[5–8, comma-separated, balancing technical precision with SEO search relevance, e.g.: Polkadot, 智能合约, ink!, Solidity, Revive, Web3 开发]

Platforms:
CSDN, Juejin, WeChat Official Account

Categories:
[Select the 1–2 best matches from: Polkadot Ecosystem / Smart Contract Development / Web3 Introduction / Rust Development / Solidity / Blockchain Tools]
---
```

---

### Step 4: Format for CSDN publication

Output the complete article in the following format, following these rules:

#### Word Count Requirements

- **Minimum 1,500 characters, maximum 7,000 characters**
- Let the amount of content in the source naturally determine the length — do not artificially compress or pad
- If the translated content falls below 1,500 characters, expand by:
  - More detailed background explanation of core concepts
  - Line-by-line Chinese annotations and explanations for code examples
  - Appending a "Summary" or "Developer Tips" paragraph at the end of sections
- If the translated content exceeds 7,000 characters, condense redundant wording while preserving core information

#### Article Opening Rules

The first body paragraph (after the abstract block) must be engaging — it should make an entry-level developer want to keep reading. Choose one of the following opening strategies:

- **Pain-point resonance**: raise a confusion or barrier that beginners commonly encounter when entering Web3, then lead into the problem this article solves
  > Example: "Just getting into Web3 development? You may already be overwhelmed by chains, tools, and jargon. Ethereum, Polkadot, Solidity, Rust… where do you even start?"
- **Conclusion-first**: lead with a conclusion that surprises or intrigues the reader, then use the body to explain it
  > Example: "The Ethereum contract you are writing now can be deployed directly to Polkadot without changing a single line of code — and with lower fees and better performance."
- **Scenario-based**: guide the reader into the topic through a concrete development scenario
  > Example: "Say you want to deploy a DeFi application on Polkadot. You will find it not only supports the Solidity you already know, but also offers a native execution environment with significantly better performance."

**Prohibited**: using a flat background introduction as the opening (e.g. "This article will introduce…", "Polkadot is a…").

#### Title Rules

- SEO-optimised, using keywords developers commonly search for
- Also appealing to CSDN readers — can reference patterns like "How to…", "Complete guide", "Hands-on tutorial", "Zero-to-one intro"

```markdown
---
title: [SEO-optimised Chinese title]
author: Source author: PaperMoon team
date: [Date of execution, format YYYY-MM-DD]
categories: [category]
tags: [keyword list]
---

> **Abstract**: [under 300-character abstract]
>
> **Keywords**: [keywords]

---

[Engaging opening paragraph]

[Article body: translated Chinese content, with term explanations, section structure, code blocks, charts]

---

**Read original**: [$URL]
```

---

### Step 5: Save the file

1. Confirm that the output directory `output/CSDN tutorials/` exists — create it if not
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
| validator | 验证人 | [needs explanation] A node responsible for validating blocks and maintaining network security, required to stake DOT as collateral |
| nominator | 提名人 | |
| governance | 治理 | [needs explanation] The on-chain decentralised decision-making mechanism — token holders can vote on protocol upgrades, fund usage, and other major matters |
| treasury | 国库 | [needs explanation] An on-chain fund pool managed by governance, used to fund ecosystem projects and developers |
| smart contract | 智能合约 | [needs explanation] A program deployed on a blockchain that executes automatically when pre-set conditions are met, without human intervention |
| extrinsic | 外部调用（extrinsic） | [needs explanation] In Substrate, an operation request initiated from outside the chain — similar to an Ethereum "transaction" but broader in scope |
| dispatchable | 可调度函数 | |
| weight | 权重 | [needs explanation] The unit Substrate uses to measure the computational complexity of an operation, determining how much fee it consumes |
| fee | 费用 | |
| epoch | 时期 | |
| era | 纪元 | |
| block | 区块 | |
| transaction | 交易 | |
| account | 账户 | |
| address | 地址 | |
| staking | 质押 | [needs explanation] Locking tokens in the network to participate in consensus or earn rewards — similar to a "deposit" |
| bonding | 绑定 | |
| unbonding | 解绑 | |
| slashing | 惩罚（slash） | [needs explanation] When a validator acts maliciously or makes a severe error, a portion of their staked tokens is confiscated as a penalty |
| cross-chain | 跨链 | [needs explanation] The ability to transfer data or assets between different blockchains |
| interoperability | 互操作性 | |
| dispatch | 调度 | |
| storage | 存储 | |
| event | 事件 | |
| error | 错误 | |
| call | 调用 | |
| origin | 来源 | |
| pallet | pallet (keep English) | [needs explanation] A functional module in the Substrate framework — like LEGO bricks, developers can combine different pallets to build blockchain features |
| runtime | runtime (keep English) | [needs explanation] The core logic layer of a blockchain, defining all on-chain rules and state transitions — analogous to the blockchain's "operating system" |
| ink! | ink! (keep English) | [needs explanation] The framework for writing smart contracts in Rust in the Polkadot ecosystem — compiles to WASM and runs on-chain |
| Substrate | Substrate (keep English) | [needs explanation] The blockchain development framework for the Polkadot ecosystem — developers can use it to quickly build custom blockchains; Polkadot itself is built with Substrate |
| XCM | XCM (keep English) | [needs explanation] Cross-Consensus Messaging — the standard protocol in the Polkadot ecosystem for passing messages and assets between chains |
| EVM | EVM (keep English) | [needs explanation] Ethereum Virtual Machine — Ethereum's runtime environment for executing smart contracts; chains that support EVM can run Solidity contracts |
| Revive | Revive (keep English) | [needs explanation] A compiler that compiles Solidity contracts into PVM (RISC-V) bytecode, allowing Ethereum contracts to run natively on Polkadot |
| PVM | PVM (keep English) | [needs explanation] Polkadot Virtual Machine — the native execution environment based on the RISC-V instruction set; higher performance and lower fees |
| JAM | JAM (keep English) | [needs explanation] Join-Accumulate Machine — Polkadot's next-generation core protocol, aiming to further improve network performance and flexibility |
| WASM / WebAssembly | WASM / WebAssembly (keep English) | [needs explanation] An efficient binary instruction format that can run across different platforms; used in the early Polkadot ecosystem to execute contract code |
| RPC | RPC (keep English) | |
| API | API (keep English) | |
| CLI | CLI (keep English) | |
| precompile | 预编译合约（precompile） | [needs explanation] A special contract pre-built into the chain to access native chain features (e.g. cross-chain transfers) — called in the same way as ordinary contracts |
| JSON-RPC | JSON-RPC (keep English) | [needs explanation] A remote call protocol using JSON format; both Ethereum nodes and Polkadot nodes expose interfaces through it |

---

## Quality Checklist

Confirm each item before outputting the file:

- [ ] All paragraphs translated — none missed
- [ ] Code blocks complete and untruncated — Chinese annotations added
- [ ] Charts have Chinese explanations — English original preserved
- [ ] Metadata (abstract, keywords, categories) filled in
- [ ] Title is SEO-optimised
- [ ] Article opening uses an engaging strategy (pain-point resonance / conclusion-first / scenario-based) — flat background introduction not used
- [ ] Terms marked `[needs explanation]` in the Terminology Reference Table each have a 1–2 sentence explanation on first appearance
- [ ] Article word count between 1,500 and 7,000 (excluding code blocks)
- [ ] "Read original" link at the end
- [ ] File saved to `output/CSDN tutorials/`, naming follows the rules
