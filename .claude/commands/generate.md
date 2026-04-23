Generate the Chinese article from the approved outline in `pr_body.md`.

**IMPORTANT: You must show the outline to the user and get explicit confirmation before running phase2. Do not skip this step under any circumstances.**

## Steps

1. Check whether `pr_body.md` exists in the project root.
   - If it does not exist: tell the user to run `/phase1 <urls> <intent>` first.

2. Read `pr_body.md` and extract the outline section (everything under `## ✏️ Outline`, before the final `---`).
   Display it to the user in full.

3. **STOP. Ask the user:**
   > "Above is the outline that will be used to write the article. Does it look right?
   > Edit `pr_body.md` directly if you want to change the angle, sections, or key claims.
   > Reply **yes** to generate, or **no** to cancel."

   Wait for the user's reply. Do not proceed to step 4 until they confirm with **yes** or equivalent.
   If they say no or want edits, help them modify the outline in `pr_body.md`, then ask again.

4. Once the user confirms, run Phase 2:

```bash
python3 scripts/run_skill.py phase2 \
  --pr-body-file pr_body.md
```

5. After the command completes, tell the user the exact filename and path of the saved article:
   - Analytical / opinion → `output/analysis/`
   - Tutorials → `output/tutorials/`
   - Concept explainers → `output/explainers/`
   - Pop-science / YouTube → `output/science-pop/`
   - Monthly recaps → `output/monthly-recap/`
