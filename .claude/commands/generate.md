Generate the Chinese article from the approved outline in `pr_body.md`.

**IMPORTANT: You must show the outline to the user and get explicit confirmation before running phase2. Do not skip this step under any circumstances.**

## Steps

1. Find the most recent outline file:
   - Look in the `outlines/` folder for the latest `YYYY-MM-DD-*.md` file (sort by name, take the last one).
   - If `outlines/` is empty or missing: tell the user to run `/phase1 <urls> <intent>` first.

2. Read that outline file and extract the outline section (everything under `## ✏️ Outline`, before the final `---`).
   Show the user which file you're using (e.g. `outlines/2026-04-23-polkadot-smart-contracts.md`).
   Display the outline section in full.

3. **STOP. Ask the user:**
   > "Above is the outline that will be used to write the article. Does it look right?
   > Edit `pr_body.md` directly if you want to change the angle, sections, or key claims.
   > Reply **yes** to generate, or **no** to cancel."

   Wait for the user's reply. Do not proceed to step 4 until they confirm with **yes** or equivalent.
   If they say no or want edits, help them modify the outline in `pr_body.md`, then ask again.

4. Once the user confirms, run Phase 2 with the outline file you found in step 1:

```bash
python3 scripts/run_skill.py phase2 \
  --pr-body-file outlines/YYYY-MM-DD-slug.md
```

(Replace `outlines/YYYY-MM-DD-slug.md` with the actual filename from step 1.)

5. After the command completes, tell the user the exact filename and path of the saved article:
   - Analytical / opinion → `output/analysis/`
   - Tutorials → `output/tutorials/`
   - Concept explainers → `output/explainers/`
   - Pop-science / YouTube → `output/science-pop/`
   - Monthly recaps → `output/monthly-recap/`
