---
name: literature-review
description: "Minimal literature review for the AI in Practice hackathon. Trigger on: 'literature review', 'find related work', 'search for papers on', 'what has been done on', 'survey the literature'. Produces a short review note and adds entries to references/references.bib."
---

# Literature Review (minimal)

A lightweight, time-boxed literature review for a hackathon project. Four steps: scope, search, read, write. Aim for one focused session, not an exhaustive survey.

## Say this when the skill is first used

Tell the user, briefly:

- This is a **minimal, generic** literature-review skill. It is a starting point and they will likely want to **tailor it** to their field, preferred sources, and output format.
- For it to actually be available as a skill, it has to be **registered with Claude** (see "Registering this skill" below). Offer to walk them through it.

## Registering this skill

A skill only triggers automatically once Claude knows about it. This `skills/` folder in the workspace is the source copy; it is not yet "installed". How to install depends on which Claude they use:

- **Claude Code (terminal):** copy or symlink the skill folder into a skills directory Claude Code reads.
  - Personal (all projects): `~/.claude/skills/literature-review/`
  - Project (committed with the repo): `.claude/skills/literature-review/`
  - A symlink works and keeps a single source of truth, e.g.
    `ln -s "$(pwd)/skills/literature-review" ~/.claude/skills/literature-review`
  - Claude Code watches these directories, so the skill becomes available in the current session without a restart.
- **Claude desktop / web (Cowork):** skills are uploaded as a ZIP through the UI. Zip the `literature-review` folder (must contain `SKILL.md`), then in the app go to **Customize -> Skills -> + -> Create skill** and upload the ZIP. Make sure the skill's toggle is on, and that **Settings -> Capabilities -> code execution and file creation** is enabled. It then works across chat, projects, and Cowork.
- If unsure which applies, ask the user how they run Claude.

## Step 1 — Scope (quick interview)

Ask the team, briefly:

- **Question:** what exactly are you searching for? (one sentence)
- **Why:** what decision will this review inform?
- **Limits:** rough time range and how many papers to read (default: last ~10 years, 10–15 candidates, read 4–6).

Write these down at the top of the review note (see Step 4).

## Step 2 — Search

1. Turn the question into 2–3 search queries (try synonyms).
2. Use web search; arXiv, Semantic Scholar, and Google Scholar pages often appear in results.
3. For each promising hit, collect: title, authors, year, venue, and a one-line reason it is relevant.
4. Add every candidate to `references/references.bib` with a metadata comment:

```bibtex
% status: candidate
% reason: <one line: why this came up>
@article{author2024keyword,
  title   = {...},
  author  = {...},
  year    = {2024},
  journal = {...}
}
```

5. Show the candidate list to the team and pick which to read (recommend a shortlist).

Status values: `candidate` (found), `selected` (will read), `included` (read, kept), `excluded` (read, dropped — say why), `not-accessed` (paywalled, abstract only).

## Step 3 — Read

For each selected paper:

1. Prefer the open-access / arXiv version. If paywalled and you cannot access it, mark `not-accessed` and assess from the abstract.
2. Read for: the method, the setting, the main result, and the limitation.
3. Be skeptical — does the result actually support the claim? Note anything that contradicts your project's assumptions.
4. Update its status in `references.bib` to `included` or `excluded`.

## Step 4 — Write

Save to `notes/YYYY-MM-DD_lit-review_<topic>.md` (create the `notes/` folder if needed):

```markdown
# Literature Review: <Topic>
Date: YYYY-MM-DD

## Scope
- Question: <...>
- Why: <...>
- Limits: <...>

## Summary
<Half a page. What is the state of the art for our question? Cite as [@citekey].
Where do sources disagree? What does this mean for our project?>

## Papers
| Source | Method | Key result | Limitation | Relevance |
|--------|--------|------------|------------|-----------|
| [@citekey] | ... | ... | ... | high/med/low |
```

## Rules

- Keep the summary to half a page. Detail goes in the table.
- Every claim in the summary cites a specific source.
- Include papers that disagree with you — they matter more, not less.
- Do not delete existing `references.bib` entries; only add or update status comments.

## When done

Append an entry to the project's `LOG.md` (newest at top) noting: question, how many found/read, the review file path, and how many entries were added to `references.bib`. If the review settled the research question, write it into the project's `CLAUDE.md`.
