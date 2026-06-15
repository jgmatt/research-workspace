<!--
========================================================================
  CLAUDE.md — WORKSPACE ENTRY POINT (AI in Practice)
========================================================================
  Read this file at the start of every session.

  It holds the researcher's profile (a SCAFFOLD filled once, by
  interview) plus basic instructions and two triggers. Detailed
  procedures live in notes/ and are linked below — read the linked
  file when a trigger fires.
========================================================================
-->

# CLAUDE.md — AI in Practice workspace

## About me

<!-- SCAFFOLD. Empty until the first session. Do NOT invent content — it is filled by the getting-started interview. -->

- **Name / what to call me:** <name>
- **Position:** <e.g. master's student, PhD student, postdoc, PI>
- **Lab / group:** <lab>
- **Supervisors / PIs:** <names, or "I am the PI">
- **Related institutes / affiliations:** <list>
- **Research interests:** <topics>
- **Skills / strengths:** <what I am good at>
- **Weaknesses / where I want support:** <what I find hard>
- **Preferred communication style:** <e.g. concise, no fluff; detailed; English; math in LaTeX>

## Rules for Claude

<!-- SCAFFOLD. Filled during the interview. Give each rule a short example so the intent is clear. -->

- <rule> — e.g. "<example>"
- <rule> — e.g. "<example>"

## How this workspace works

Project-based research workspace for the AI in Practice hackathon.

- `CLAUDE.md` — this file: the entry point and the researcher's profile.
- `spec/` — the researcher's project-independent source of truth (definitions, models, notation). Not part of the hackathon. See `notes/the-spec.md`.
- `references/` — `references.bib` with all sources.
- `skills/` — reusable procedures (e.g. a minimal literature review).
- `notes/` — workspace notes and the detailed procedures linked below.
- `projects/` — one folder per project, each with its own `CLAUDE.md` and `LOG.md`. No STATE.md anywhere.

## Basic instructions

- Read this file at the start of every session.
- Inside a project, read that project's `CLAUDE.md` first, and append to its `LOG.md` after any substantial work or decision (newest entry on top).
- Put every source in `references/references.bib`; use the **literature-review** skill for related work.
- The spec is not filled during the hackathon — see `notes/the-spec.md` for what it is and how to compile it.
- When uncertain, flag it and continue. When a change has large downstream consequences, stop and ask first.

## Triggers

- **"Hi Claude, I'm <name>."** — if **About me** above is still empty, follow `notes/getting-started.md` (introduce yourself, explain the workspace, run the setup interview to fill in this file). If it is already filled, just greet them and ask what they want to work on.
- **"Let's start a project."** — follow `notes/starting-a-project.md` (interview the group, create the project folder with its `CLAUDE.md` + `LOG.md`, init git, help connect a remote, offer a literature review).
