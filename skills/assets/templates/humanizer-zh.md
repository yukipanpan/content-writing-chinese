# AI Writing De-Fingerprinting Template (Chinese Edition)

> Based on the [Humanizer-zh](https://github.com/op7418/Humanizer-zh) project, adapted for Chinese writing contexts.
> Core principle: not about "fooling" detectors — it is about making the writing genuinely carry human thought and voice.

---

## How to Use

Hand the following instruction to Claude, replacing `$TEXT` with the text to be processed:

> Please apply AI writing de-fingerprinting to the following text, following the rules in `templates/humanizer-zh.md`:
> $TEXT

**Mode description** (choose based on the calling context):

| Mode | Trigger Context | Output Format |
|------|---------|---------|
| `Full_Compare` (default) | Standalone call to humanizer for a piece of text | Output "Before / After / Summary of Changes" in three-section comparison |
| `Inline` (nested mode) | Called by another template (web-remix, youtube-remix, etc.) | Output the final version directly — **do not output a comparison format** |

When you see the instruction "run humanizer-zh de-fingerprinting check" inside another template, automatically use `Inline` mode.

---

## Execution Steps

### Step 0: Determine the article's style

**Before making any changes, read the full text**, and determine which style type this article belongs to. The style determination will guide the direction and scope of all subsequent rewrites.

#### Style Type Reference

| Style Type | Determination Criteria | Rewrite Direction |
|----------|----------|----------|
| **Beginner developer popular science** | Heavy use of term explanations, step-by-step breakdowns; reader assumed to be a technical newcomer | Maintain accuracy; wording can be more conversational; analogies should be close to everyday life; do not add unnecessary "emotion" |
| **WeChat / community article** | Has viewpoints and narrative; balances popular science and vision-painting; leans toward soft content | Opening needs a hook; narrative has rise and fall; closing can have attitude but must not be preachy; first person allowed |
| **Personal essay** | Has an "I" perspective; casual tone; includes personal experience or feeling | Preserve personalised expression; incomplete sentences allowed; emotion allowed; strict structural integrity not required |
| **Light and playful popular science** | Uses analogies, jokes, rhetorical questions; reader may not be technical | Maintain rhythm; prefer short sentences; exaggerated rhetoric allowed but must not be sycophantic |
| **Formal announcement / official notice** | No personal pronoun; formal tone; mainly facts and conclusions | Only remove AI fingerprints; do not change tone; do not add personal opinion; do not let it become "soft" |
| **Academic / technical in-depth article** | Contains data citations, logical argument; aimed at readers with background knowledge | Preserve technical terminology; rewrites target only hollow wording; do not simplify substantive content |

#### Output the style determination conclusion

Before starting any changes, output a style determination statement in the following format:

```
[Style Determination]
Type: [select the 1–2 best-matching types from the table above]
Rationale: [1–2 sentences explaining the determination, citing specific expressions from the source]
Rewrite direction: [what this round of changes will focus on, and what will be avoided]
```

---

### Step 1: Scan for AI writing patterns

Check the text against the "24 AI Writing Patterns" below, marking every hit.

### Step 2: Rewrite problem passages

For each flagged problem, replace with natural Chinese expression, following these principles:

- **Preserve core meaning**: rewrite phrasing — do not change the information
- **Style consistency first**: the tone after rewriting must match the style determined in Step 0 — do not change the article's overall register in the name of "de-AI-fication"
- **Inject real personality**: let the writing have opinions, warmth, and concrete detail
- **Scale of change follows style**: formal announcements — minimal changes only; personal essays — can be changed more thoroughly; WeChat articles — focus improvement on opening and closing

### Step 3: Overall polish

After completing individual changes, read the full text and ensure:
- Rhythm has variation (long and short sentences alternate — not one single sentence pattern throughout)
- Logic is coherent; transitions at edited passages are natural
- No new AI-flavoured vocabulary has been introduced

### Step 4: Output the comparison

Output format:

```
[Before]
[Original text]

[After]
[Rewritten text]

[Summary of Changes]
- [Change 1: which pattern was triggered, how it was rewritten]
- [Change 2]
- ...
```

---

## 24 AI Writing Patterns Checklist

### Content Patterns (6)

**① Over-emphasising significance, legacy, and trends**
- Symptom: constantly elevating to "profound impact on the entire industry", "historic significance"
- Fix: only write what specifically happened — leave the significance for readers to judge themselves
- Example: ❌ "This innovation will redefine the future of work" → ✅ "This feature saves users two clicks"

**② Over-emphasising fame and media coverage**
- Symptom: "widely acclaimed", "industry-recognised", "widely covered by media"
- Fix: state a specific number or source, or delete entirely

**③ Shallow analysis ending in "-ing / 正在"**
- Symptom: "正在改变……" (currently changing…), "持续探索……" (continuously exploring…), "不断演进……" (constantly evolving…) — sentence ends here with no substantive content
- Fix: say specifically what changed, or delete

**④ Promotional and advertising language**
- Symptom: "无缝体验" (seamless experience), "充满活力" (vibrant), "令人叹为观止" (breathtaking), "革命性的" (revolutionary)
- Fix: replace with concrete descriptions, or delete the adjective

**⑤ Vague attribution and ambiguous phrasing**
- Symptom: "行业专家认为" (industry experts believe), "研究表明" (studies show), "有人认为" (some believe) — no specific source
- Fix: give a specific source, or change to "I think"

**⑥ Outline-style "Challenges and Outlook" closing**
- Symptom: the final paragraph is always "Despite the challenges, the future is full of hope…"
- Fix: end directly, or replace with a specific next step

---

### Language and Grammar Patterns (6)

**⑦ Overuse of "AI vocabulary"**
- High-frequency warning words (see full list at the bottom): 此外、至关重要、深入探讨、强调、持久的、增强、培养、突出、格局、关键性的、展示、证明、宝贵的、充满活力的
- Fix: replace with more direct verbs or concrete nouns, or delete

**⑧ Copula avoidance (avoiding "是" / "is")**
- Symptom: turning "A is B" into roundabout expressions like "A serves as an embodiment of B" or "A represents B"
- Fix: just say "A is B"

**⑨ Negative parallel structure**
- Symptom: "这不仅仅是……，而是……" (this is not just…, it is…), "不只是……，更是……" (not only…, but also…)
- Extended symptom: three-part elimination — "不是……不是……而是……" (not X, not Y, but Z) — AI uses this to mimic "breaking conventional wisdom". The reader sees through it immediately.
- Fix: directly state the most important point — do not build up to it by eliminating decoys

**⑩ Overuse of the rule of three**
- Symptom: descriptions always come in three: "无缝、直观和强大" (seamless, intuitive, and powerful), "高效、精准、可靠" (efficient, precise, reliable)
- Fix: choose the most important one word — delete the rest

**⑪ Deliberate synonym cycling**
- Symptom: in the same passage, "利用", "借助", "依托" are used interchangeably to refer to the same thing
- Fix: use the most direct word consistently — do not pursue "variation"

**⑫ False scope**
- Symptom: "在许多方面" (in many respects), "在很大程度上" (to a large extent), "在某种意义上" (in a sense) — says nothing
- Fix: say specifically which respect, or delete

---

### Style Patterns (6)

**⑬ Overuse of em-dashes**
- Symptom: every paragraph has an insertion like "——这……" (——this…)
- Fix: integrate into the sentence, or start a new sentence

**⑭ Overuse of bold text**
- Symptom: every paragraph has bold words — bold loses its emphasis function
- Fix: only bold truly important items — no more than 3 instances of bold per article

**⑮ Inline-heading vertical lists**
- Symptom: heavy use of "**Point One**: …\n**Point Two**: …" format
- Fix: content that can be written as a flowing paragraph should not be forced into a list

**⑯ Excessive heading formalisation / clickbait headings**
- Symptom: every sub-section uses a very formal heading format
- Fix: informal articles can use ordinary punctuation or low-key headings

**⑰ Emoji overuse**
- Symptom: every paragraph opens with an emoji 🎯✨💡
- Fix: delete, or keep only 1–2 in very conversational contexts

**⑱ Overuse of quotation marks**
- Symptom: heavy use of scare quotes "所谓的", or using quotation marks instead of italics for emphasis
- Fix: express directly — quotation marks are not needed to imply ironic distance

---

### Communication Patterns and Filler Words (6)

**⑲ Collaborative communication traces**
- Symptom: "当然！" (Of course!), "好的，让我来帮你……" (Sure, let me help you…), "这是个好问题" (That's a great question)
- Fix: go straight into the content — delete all opening pleasantries

**⑳ Knowledge cutoff disclaimers**
- Symptom: "请注意，我的知识截止到……" (Please note, my knowledge cuts off at…), "情况可能已经发生变化" (the situation may have changed)
- Fix: if information timeliness needs noting, change to a specific date statement

**㉑ Flattery / fawning tone**
- Symptom: "这是一个很棒的想法" (That's a great idea), "您的问题非常深刻" (Your question is very profound)
- Fix: respond directly to the content — do not evaluate the question itself

**㉒ Filler phrases**
- Symptom: "值得注意的是" (it is worth noting that), "重要的是要理解" (it is important to understand), "不可忽视的是" (what cannot be ignored is)
- Fix: directly state the thing that "is worth noting"

**㉓ Excessive hedging**
- Symptom: every sentence has "可能" (possibly), "或许" (perhaps), "在某些情况下" (in some cases), "通常来说" (generally speaking)
- Fix: state what can be stated with certainty directly — only hedge when genuinely uncertain

**㉔ Generic positive closing**
- Symptom: the article must end with "In summary, this is an exciting field…"
- Fix: use a specific action recommendation or genuine conclusion, or simply end

---

## Key Writing Principles

### Not just "clean" — but "vivid"

Removing AI patterns is only the first step. Genuinely good rewriting also requires:

| Principle | What to Do | Counter-example |
|------|------|------|
| **Have opinions** | React to facts — not just report them | ❌ "AI is changing the industry" → ✅ "I think AI's impact on this industry is overestimated" |
| **Rhythm variation** | Alternate long and short sentences — avoid every sentence being the same length | ❌ Every sentence is a 20-character compound sentence |
| **Acknowledge complexity** | Real people have complex feelings — not always positive | ❌ "This is undoubtedly a positive development" |
| **Use first person appropriately** | "I think" is more honest than "it is believed" | ❌ "It is widely believed in the industry" |
| **Allow some messiness** | Perfect logical structure can feel mechanical | ❌ Every paragraph has a clear setup, development, and resolution |
| **Feelings must be concrete** | Use details instead of abstract descriptions | ❌ "The experience is very good" → ✅ "It is usable in under two seconds of opening" |

---

## High-Frequency AI Vocabulary Warning List

The following words warrant close inspection when they appear (their frequency in Chinese AI writing is abnormally high):

```
此外 / 另外 / 不仅如此        → just start the next sentence
至关重要 / 不可或缺           → say clearly why it is important
深入探讨 / 深入分析           → just "analyse" or "discuss"
强调 / 凸显 / 彰显            → directly state the thing itself
持久的 / 深远的影响           → say specifically what it affected
增强 / 赋能 / 赋予            → use a concrete verb
培养 / 滋养                   → say what specific thing was done
突出 / 彰显                   → same as above
格局（in abstract usage）     → say specifically what the situation is
关键性的 / 关键               → say why it is key
展示 / 证明 / 佐证            → give the evidence directly
宝贵的 / 宝贵经验             → say specifically what the experience is
充满活力的 / 蓬勃发展的       → give specific data or phenomena
无缝 / 直观 / 强大            → describe the specific functionality
革命性的 / 颠覆性的           → say what specifically changed
作为……的证明 / 体现           → change to "is"
```

---

## Quality Checklist

Confirm each item after rewriting is complete:

- [ ] [Style Determination] conclusion has been output, including type, rationale, and rewrite direction
- [ ] The tone after rewriting matches the determined style type — the article's overall register has not been changed by de-AI-fication
- [ ] All 24 patterns have been checked — flagged problems have been addressed
- [ ] No new AI-flavoured vocabulary has been introduced (cross-check against the warning list)
- [ ] The article has concrete details — not just abstract descriptions
- [ ] Sentence lengths vary — not a single uniform rhythm throughout
- [ ] The closing fits the style's expected wrap-up (formal announcements need no attitude; personal essays may)
- [ ] "Before / After / Summary of Changes" comparison format has been output
