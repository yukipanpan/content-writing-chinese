Fetch sources and generate an English outline for review.

Accepts manual URLs, a topic for auto-discovery, or both combined.

**Arguments:** `$ARGUMENTS` — any combination of URLs, a topic keyword, and intent description.

## Parsing $ARGUMENTS

Extract three things from `$ARGUMENTS`:

1. **URLs** — any tokens starting with `http://` or `https://`
2. **Topic** — text after `topic:` label (e.g. `topic: Polkadot JAM upgrade 2025`)
3. **Intent** — remaining free text describing what to write

At least one of URLs or topic must be present. If neither is found, ask the user before proceeding.

## Examples

```
/phase1 https://polkadot.com/blog/jam-update intent: analytical piece on JAM for developers
/phase1 topic: Polkadot JAM upgrade 2025 intent: analytical piece for Chinese Web3 audience
/phase1 https://graypaper.com topic: Polkadot JAM intent: deep dive for developers
```

## Running the command

**URLs only:**
```bash
python3 scripts/run_skill.py phase1 \
  --urls "<comma-separated URLs>" \
  --intent "<intent>" \
  --generate-snippets \
  --pr-body-file pr_body.md
```

**Topic only (auto-discover sources):**
```bash
python3 scripts/run_skill.py phase1 \
  --topic "<topic>" \
  --intent "<intent>" \
  --top-n 5 \
  --generate-snippets \
  --pr-body-file pr_body.md
```

**Both (manual + auto-discovery for richer source mix):**
```bash
python3 scripts/run_skill.py phase1 \
  --urls "<URLs>" \
  --topic "<topic>" \
  --intent "<intent>" \
  --top-n 5 \
  --generate-snippets \
  --pr-body-file pr_body.md
```

## After the command

1. Read `pr_body.md` and show the outline section to the user.
2. Show the Sources section so the user can see which URLs were manual, auto-discovered, and loaded from the knowledge base.
3. Ask: "Does this outline look right? Edit any section or angle, then run `/generate` to produce the Chinese article."

## Notes

- YouTube and Twitter/X URLs work locally but are blocked in GitHub Actions CI.
- Auto-discovery uses DuckDuckGo by default (free, no key). Set `SEARCH_API_KEY` in `.env` for Google results via Serper.
- URLs already in the knowledge base (references/snippets/) are loaded from cache — no re-fetch needed.
- If only pasted text with no URLs or topic: use the Layer 0 path — open `skills/SKILL.MD` in any AI chat and paste the text directly.
