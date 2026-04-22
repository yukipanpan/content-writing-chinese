# Monthly Recap Template

**Important**: Before generating, you must first read the style guides:
- `assets/styles/_base.md` (general base style)
- `assets/styles/monthly-recap.md` (style specific to this content type)

---

## Hard Rules (must not be violated during execution)

1. **Do not skip any snippet** — every snippet matching the target month must appear in the article
2. **Do not merge snippets** — each snippet corresponds to an independent entry; merging multiple snippets into one paragraph is prohibited
3. **Every entry must include four required elements** — what it is / current status / who it affects / reference link (none can be omitted)
4. **Opening summary has a strict word limit** — ~200 characters, must not exceed 250

---

## Snippet Discovery Rules

### Filename Matching Method

Snippet filename format: `YYYYMMDD-[topic].md`

Matching logic (using February 2026 as an example):
- First 6 characters of filename are `202602` → belongs to February
- First 6 characters are `202601`, `202603`, etc. → does not belong to February; skip

```
Target month = YYYY-MM (e.g. 2026-02)
Matching prefix = YYYYMM (e.g. 202602)

For all .md files under references/snippets/:
  if filename.startswith(matching prefix) → include in this month
  else → skip
```

### Discovery List Confirmation Step

Before writing begins, list the complete discovery list and confirm each entry, in the following format:

```
## Discovered Snippet List (YYYY Year MM Month)

Total: N items
- [ ] 20YYYYMM-xxx.md — [one-sentence summary]
- [ ] 20YYYYMM-xxx.md — [one-sentence summary]
...

Confirmed: all files read, none missing.
```

Only after the list is confirmed does the writing phase begin.

---

## Article Structure

```
# [Title]

[Opening summary: ~200 characters]

---

## [Category 1]

### [Event sub-heading]
[Entry content]

### [Event sub-heading]
[Entry content]

---

## [Category 2]

### [Event sub-heading]
[Entry content]

---

...

---

## 结语 (Closing)

[Clean wrap-up, 3–5 sentences]
```

---

## Opening Summary Format

**Word count**: ~200 characters (must not exceed 250)

**Purpose**: engaging — makes the reader want to keep reading

**Tone**: flowing narration, concise, insightful, not a chronological list

**Pattern**:
```
[Time period], [core judgment / overall characterisation]:
[chain 3–5 dimensions of change with enumeration marks / semicolons].

[One critical or reflective closing sentence — leaves the reader with "I need to keep reading"]
```

**Example**:
> 2026 年 2 月，Polkadot 的主旋律不是发布，而是清算——核心工具链的资金接连被否，旧平台默默退场，新路径在争议中摸索前行。
> 技术侧，Revive 外部资产缺口悬而未决，RevX 以"临时方案"之名填补 Rust 合约空白；治理侧，PAPI 以 89.7% 反对被拒，Polkassembly 带着累计 $315 万的历史账本申请收尾费。
> 这个月，Polkadot 正在做一道减法题，只是答案还没写完。

(Example kept in Chinese — it demonstrates the target output style.)

**Avoid**:
- ❌ Opening by listing events directly (chronological list)
- ❌ Abstract opening with no informational content
- ❌ Official-sounding "this month saw the following developments"
- ❌ Exceeding 250 characters

---

## Title Format

**Structure**: `subject + action / judgment`, or `from X to Y: core judgment`, or `data / fact + judgment`

**Examples**:
- ✅ `从清算到摸索：Polkadot 2 月的减法题`
- ✅ `工具链动荡，执行层补位：Polkadot 的 2 月`
- ❌ `Polkadot 2 月进展汇总`
- ❌ `2 月更新：技术、治理、生态`

(Title examples kept in Chinese — they demonstrate the target output format.)

---

## Category Order

Ordered by "impact + newsworthiness" from most to least significant:

1. **Core narrative of the month** (the most important 1–2 events, placed first)
2. **Execution layer / technical breakthroughs**
3. **Protocol upgrades / parameter adjustments**
4. **Governance corrections / financial changes**
5. **Ecosystem project developments**
6. **Notable "subtractions"** (shutdowns, rejections, terminations)
7. **Community / developers / education**

> If a category has only 1 entry, it may be merged with a related category under one broader heading — but the entry itself must remain independent.

---

## Sub-heading Format (per entry)

**Level**: `###` (H3 heading)

**Rules**:
- ≤10 characters (in Chinese)
- Carries a judgment or perspective — not a pure statement of fact
- Use verbs or dynamic descriptions

**Comparison examples**:
| Event | ❌ Avoid | ✅ Prefer |
|------|--------|--------|
| Revive external assets not live | Revive 功能待完善 | 跨链资产仍缺席 |
| PAPI funding rejected | PAPI 资金申请失败 | 核心工具断粮危机 |
| Polkassembly closing | Polkassembly 退出 | 旧平台清账收摊 |
| Fellowship retention vote | bkchr 通过留任 | 协议老将原地续命 |
| RevX Beta launched | RevX IDE 发布 | 临时方案填补空白 |

(Heading examples kept in Chinese — they demonstrate the target output format.)

---

## Entry Content Format (four required elements)

Each entry must cover the following four elements in natural, flowing prose (do not use labels / tables / bullet lists — weave them into the narrative):

| Element | Description |
|------|------|
| **What it is** | Core content of the event — 1–2 sentences to establish the facts clearly |
| **Current status** | Already live / passed / rejected / in progress / pending deliberation, etc. |
| **Who it affects** | Developers / validators / token holders / a specific project / the entire ecosystem |
| **Reference link** | Last line of the entry: `了解更多：[Source title](URL)` |

**Word count**: 100–250 characters (adjust based on event importance — core narratives may run longer)

**Format example**:

```
### 核心工具断粮危机

Polkadot-API（PAPI）的 2026 年 415K USDC 资金申请于 2 月 27 日被 89.7% 反对票拒绝。
PAPI 是 Polkadot 生态用于替代逐步退场的 Polkadot.js 的核心开发者 SDK，内置轻客户端支持，
被社区称为"OpenGov 资助过的最出色项目之一"。
争议核心不在于项目质量，而在于定价——W3F 在截止前一天要求削减 66%，团队视之为非真诚谈判，
选择原价提交。结果是：最核心的开发者工具，2026 年的资金来源现在悬而未决。
这直接影响到所有在 Polkadot 上构建 dApp 的开发者。

了解更多：[Polkadot-API 2026 开发资金申请](https://polkadot.subsquare.io/referenda/1836)
```

(Example kept in Chinese — it demonstrates the target output style.)

**Avoid**:
- ❌ Missing any of the four elements
- ❌ Entries that are too short (below 100 characters has too little information)
- ❌ Pure positive narrative that ignores problems or controversy
- ❌ Reference link placed in the middle — it must be at the end

---

## Closing Format

**Word count**: 3–5 sentences, concise and punchy — no dragging

**Pattern**:
```
[Summarise the 1–2 most core trends of the month].

[Point to a signal or contradiction worth continued attention].

If Polkadot is entering a [new phase], its keyword is not [A], but [B].
```

**Example**:
> 这个月，Polkadot 更换了一批人，终止了一些账单，也打开了几扇还不确定通向哪里的门。
> 最值得关注的，不是哪个功能上线了，而是谁在为基础设施买单这件事，正在变得越来越没有答案。
> 如果说 Polkadot 正在进入一个新阶段，那它的关键词不是扩张，而是清算。

(Example kept in Chinese — it demonstrates the target output style.)

---

## Execution Workflow

### Step 0: Snippet Discovery

1. List all `.md` filenames under `references/snippets/`
2. Filter for files whose first 6 characters match the target month (e.g. `202602`)
3. Output the discovery list (filename + one-sentence summary)
4. Read all matching snippets one by one
5. Confirm the list is complete and nothing is missing — then proceed to the next step

### Step 1: Theme Identification

- After reading all snippets, distil 1–2 core judgment words for the month (e.g. "清算" / "补位" / "断粮")
- These judgment words will run through the title, opening summary, and closing

### Step 2: Category and Sort

- Assign all snippets to the corresponding categories in the category order
- Each snippet is independent — do not merge

### Step 3: Write the Opening Summary

- ~200 characters, flowing narration
- Use the core judgment words to unify the article

### Step 4: Write Each Entry

- Follow the category order — write each entry one by one
- Each entry covers the four elements, with a reference link at the end
- After completing a category, check: are all snippets in that category present?

### Step 5: Write the Closing

- 3–5 sentences, clean wrap-up
- Echo the judgment words from the opening summary

### Step 6: Write the Title

- Based on the core judgment words, write a "from X to Y" or "action + judgment" structure title

### Step 7: Output

- Path: `output/monthly-recap/YYYY-MM.md`
- Before outputting, do one final checklist check: are all snippets present in the article?

---

## Complete Output Format

```md
# [Title: from X to Y / action + judgment]

[Opening summary: ~200 characters, flowing narration, engaging]

---

## [Category name 1]

### [Event sub-heading 1]

[Entry content: what it is + status + who it affects, 100–250 characters]

了解更多：[Source title](URL)

---

### [Event sub-heading 2]

[Entry content]

了解更多：[Source title](URL)

---

## [Category name 2]

### [Event sub-heading 3]

[Entry content]

了解更多：[Source title](URL)

---

...（every snippet has its own independent entry — none skipped, none merged）...

---

## 结语 (Closing)

[3–5 sentences, clean wrap-up]
```
