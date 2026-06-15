# Getting started — workspace setup procedure

This file tells Claude what to do the first time a researcher arrives. It is the procedure behind the **"Hi Claude, I'm \<name\>."** trigger in `../CLAUDE.md`. Follow it step by step. Speak naturally, one topic at a time, and do not dump all the questions at once.

## When to run this

Run this procedure when the user greets you with **"Hi Claude, I'm \<name\>."** and the **About me** section of `../CLAUDE.md` is still empty (placeholders unfilled). If it is already filled, skip this and just greet them.

## Step 1 — Greet and introduce yourself

Say hello back, by name. Introduce yourself as their **research assistant** for this workspace. Mention that you heard they are doing the **AI in Practice hackathon**, and that you will help them set up their research workspace and, later, their hackathon project.

## Step 2 — Explain the workspace (briefly)

Explain how the workspace is structured, then give a 1–2 sentence explanation of each key concept:

- **CLAUDE.md** — the entry point you read at the start of every session; the workspace one holds the researcher's profile, and each project gets its own.
- **spec/** — their own, project-independent source of truth: definitions, models, and notation that span all of their research. Not needed for the hackathon; it is theirs to explore and grow afterwards.
- **LOG.md (per project)** — an append-only diary of changes and decisions inside each project, so the history is never lost.
- **references/** — one `references.bib` collecting every source.

Keep each to one or two sentences. (Note: there is intentionally **no STATE.md** in this workspace.)

## Step 3 — Ask permission to interview

Ask whether they are ready for a **quick interview** to set up the workspace. Make clear this sets up the **workspace CLAUDE.md only** — not a project yet. Wait for them to say yes.

## Step 4 — Run the interview

Go through these topics conversationally, one or a few at a time. Propose a draft where you can, and let them confirm or correct. Fill the **About me** and **Rules for Claude** sections of `../CLAUDE.md` as you go.

1. **Name** — what should I call you?
2. **Research interests** — what topics are you into?
3. **Preferred communication style** — concise vs detailed, language, formatting, math notation, etc.
4. **Basic rules for me** — any standing rules for how I should work? Ask for a short **example** with each rule so the intent is clear (e.g. "no em dashes — write 'A and B', not 'A — B'").

## Step 5 — Summarise and close

When the interview is done:

1. **Summarise** what you now know about them and how you will work with them, based on their stated rules and style.
2. Say it is a **pleasure to meet them** and that you are **excited to work with them**.
3. Tell them that **once they have a group for the hackathon**, you can set up the project CLAUDE.md together. They should say **"Let's start a project."** when they are ready.

The project kickoff procedure itself lives in `starting-a-project.md`.

---

## Design notes

- **Git remote.** We use the manual browser route on purpose (no CLI dependency): create an empty repo in the browser, then `git remote add origin` and push. Claude walks the group through it step by step at kickoff (see "Creating a remote" in `starting-a-project.md`).
- **The spec.** `spec/` is the researcher's project-independent single source of truth (definitions, models, notation) for their research in general, not for any one hackathon project. It is intentionally left for them to explore and grow after the workshop. Claude mentions it during the greeting but does not fill it during the hackathon.
