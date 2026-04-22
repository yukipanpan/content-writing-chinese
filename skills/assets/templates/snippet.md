# Snippet Template
Name: Information Capture Template
Description: Organises captured information into systematic snippets, supports multiple updates while retaining an update log

## Naming Rules

Filename format: `YYYYMMDD-keyword[-outcome-status].md`

### Date Part

**Basic rule**: YYYYMMDD = the date of the most recent source in the `sources` list

**Event-change rollback rule**: When an event changes state (e.g. a proposal executes, passes, is rejected, or a project goes live), but the most recent source link's date has not been updated, set the filename date to the **actual date the state change occurred**, not the source date.

Decision logic:
- If there is a new source with an updated date → filename date = new source date (basic rule)
- If there is no new source, but the event state changed (observable from on-chain data, vote results, etc.) → filename date = actual date the change occurred
- Note in the update log: "on-chain observation: executed/passed/rejected on YYYY-MM-DD, no independent source"

Typical scenarios:
- Proposal submitted 2/4 (source date 2/4), executed on-chain 2/8 but no new article → rename filename date to 20260208
- Proposal submitted 2/16 (source date 2/16), vote result on 3/1 but no independent announcement → rename filename date to 20260301
- Runtime upgrade submitted 2/4, recovery observed 2/19 with only on-chain record → rename filename date to 20260219

### Keyword Part

- Concise description of the event's core content; generally unchanged after creation

### Outcome Status Part (optional)

- When an event's outcome / state changes, append a status suffix after the keyword
- Common status suffixes:
  - Governance: `-已通过` / `-已拒绝` / `-已执行` / `-已超时` / `-审议中`
  - Project: `-已上线` / `-已停止` / `-Beta` / `-已恢复`
  - Incident: `-已修复` / `-进行中`
- If the outcome is already clear at first creation, include the status suffix immediately
- If the event is still in progress and outcome is unknown, the suffix may be omitted

### Evolution Examples

```
# ink! Alliance stops development
First creation (based on Twitter 1/28):
  20260128-ink-Alliance停止开发.md

Add Forum original post (Forum date 1/27, but Twitter 1/28 is newer):
  → Filename unchanged (latest source date is still 1/28)
  → Content updated, update log appended

If community takes over in the future (new source date 3/15):
  → 20260315-ink-Alliance停止后社区接手.md (date + keyword + status all change)

# Bloque Stage 3 Proposal
First creation (proposal in progress, source date 2/13):
  20260213-Bloque-Stage3-Card扩展.md

Proposal passes (new source 3/1):
  → 20260301-Bloque-Stage3-Card扩展-已通过.md

# Hyperbridge Incident
First creation (incident announcement 2/15):
  20260215-Runtime-v207-Hyperbridge中断.md

Recovery announcement (2/19):
  → 20260219-Runtime-v207-Hyperbridge中断-已恢复.md

# Runtime Upgrade (event-change rollback rule example)
First creation (source date 2/4, proposal just submitted):
  20260204-Runtime-v206升级.md

On-chain execution observed on 2/8, but no new article / announcement:
  → 20260208-Runtime-v206升级-已执行.md
  → Date changes from 0204 → 0208 (use actual execution date, not source date)
  → Update log notes "on-chain observation: executed on 2026-02-08, no independent source"

# Collator Bounty Proposal (event-change rollback rule example)
First creation (source date 1/22, proposal in progress):
  20260122-System-Collator-Bounty-Topup.md

Vote ends with rejection observed on 2/19, but no new article:
  → 20260219-System-Collator-Bounty-Topup-已拒绝.md
  → Date changes from 0122 → 0219 (use the date when the actual result was confirmed)
```

## ID Rules

- `id` uses the first creation date, format `S-YYYYMMDD-XXXX`, never changes after creation
- `id` is the snippet's unique stable identifier, used for cross-snippet references
- The filename may change on updates, but the `id` does not

---
id: S-YYYYMMDD-XXXX
created: YYYY-MM-DD
updated: YYYY-MM-DD

sources:
  - title: ""
    url: ""
    author: ""
    date: ""
    note: "Initial source"
  - title: ""
    url: ""
    author: ""
    date: ""
    note: "Supplementary source (describe what new information it adds)"

topic:
  - MonthlyRecap | RecentDevelopments | PolkadotHub

tags:
  - technical
  - ecosystem
  - governance
  - performance
  - funding
  - adoption
  - developer
  - market

---

## Title

> Source: [Source Name](URL) | Last updated: YYYY-MM-DD (date of most recent source)

## Key Points (核心要点)

(Always reflects the latest state; update in sync each time)

-
-
-

## Summary (一句话总结)

(Under 50 characters — concise summary of the current latest state; update in sync each time)

## Key Quote (关键引用)

> "Original quoted passage" —— Source, Date

## Update Log (更新日志)

<!-- Reverse chronological order — newest entry at the top -->

### YYYY-MM-DD ｜ Update title (brief description of change)

**Source**: [Source Name](URL)
**Changes**:
- What was added / modified
- Impact on Key Points
- Whether the outcome / state changed (if so, update the filename too)

---

### YYYY-MM-DD ｜ Initial creation

**Source**: [Source Name](URL)
**Content**: First capture, includes……

## Use Cases (适用场景)

(What arguments / sections can this information be used to support)

## Overview (段落总结) (under 400 characters)

(Single-paragraph summary, always reflects the latest state. Rewrite on each update — do not append. The final sentence should prompt the reader's interest in reading the full article.)

Read full article: [Article Title](original URL)

## Related (关联内容)

- Related snippet IDs (use S-YYYYMMDD-XXXX format, not filenames)

## Template Usage Guide

### When creating a snippet
1. `id` uses today's date (S-YYYYMMDD-XXXX)
2. `created` uses today's date
3. `updated` is the same as `created`
4. **Filename date = the source's date** (not the date the snippet was created)
5. Append an outcome status suffix to the filename keyword if applicable
6. `sources` list has only one entry
7. The Update Log has only one "Initial creation" entry

### When updating a snippet
1. `id` and `created` do not change
2. `updated` changes to today's date
3. Append the new source to the `sources` list
4. **Rename the file**:
   - Date prefix = the `date` of the most recent entry in the `sources` list
   - **Event-change rollback**: if the event state changed but there is no new source, date = actual date the change occurred
   - If the outcome / state changed → update the status suffix in the filename
   - If the fundamental nature of the event changed → update the keyword in the filename
5. Prepend a new entry to the Update Log (reverse chronological)
6. **Rewrite** Key Points, Summary, and Overview to reflect the latest state
7. Key Quote may be appended; retain valuable older quotes
8. The "Last updated" date in the title line = most recent source date

### Fields that must be updated on every update
- `updated` (change to today's date)
- Filename (date = most recent source date; status suffix updated as needed)
- "Last updated" date in the title line
- Key Points
- Summary
- Overview

### Fields that never change
- `id`
- `created`
- Existing `sources` entries (append only, never delete or modify)
- Existing Update Log entries (append only, never delete or modify)

### Date Field Quick Reference

| Field | Meaning | When it changes |
|------|------|----------|
| Date in `id` | Date snippet was first created | Never |
| `created` | Date snippet was first created | Never |
| `updated` | Date snippet was most recently edited | Update to today on every edit |
| Filename date | Date of the most recent development in the event | Changes when a new source date appears; or when no new source but event state changes, use the change date |
| "Last updated" in title line | Matches the filename date | Stays in sync with filename date |
| `sources[].date` | Original date of each source | Never (only append new sources) |
