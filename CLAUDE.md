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
- **Research interests:** <topics>
- **Preferred communication style:** <e.g. concise, no fluff; detailed; English; math in LaTeX>

## Rules for Claude

<!-- SCAFFOLD. Filled during the interview. Give each rule a short example so the intent is clear. -->

- <rule> — e.g. "<example>"
- <rule> — e.g. "<example>"

## How this workspace works

Project-based research workspace for the AI in Practice hackathon.

```
research-workspace/
├── CLAUDE.md                     this file: entry point + researcher profile
├── README.md                     overview and how to get started
├── notes/
│   ├── getting-started.md        procedure for the "Hi Claude, I'm <name>." trigger
│   ├── starting-a-project.md     procedure for the "Let's start a project." trigger (incl. git remote)
│   └── the-spec.md               what the spec is and how to compile it
├── spec/
│   ├── spec.typ                  project-independent source of truth (definitions, models, notation)
│   └── spec.pdf                  compiled output
├── references/
│   └── references.bib            all sources
├── skills/
│   └── literature-review/
│       └── SKILL.md              minimal, generic literature-review skill
└── projects/                     one folder per project, created at kickoff
    └── <group-name>/
        ├── CLAUDE.md             project definition (group, topic, methods, research question)
        └── LOG.md                append-only record of changes and decisions
```

Note: there is intentionally **no STATE.md** anywhere. The spec is not part of the hackathon (see `notes/the-spec.md`).

## Basic instructions

- Read this file at the start of every session.
- Inside a project, read that project's `CLAUDE.md` first, and append to its `LOG.md` after any substantial work or decision (newest entry on top).
- Put every source in `references/references.bib`; use the **literature-review** skill for related work.
- The spec is not filled during the hackathon — see `notes/the-spec.md` for what it is and how to compile it.
- When uncertain, flag it and continue. When a change has large downstream consequences, stop and ask first.

## Triggers

- **"Hi Claude, I'm <name>."** — if **About me** above is still empty, follow `notes/getting-started.md` (introduce yourself, explain the workspace, run the setup interview to fill in this file). If it is already filled, just greet them and ask what they want to work on.
- **"Let's start a project."** — follow `notes/starting-a-project.md` (interview the group, create the project folder with its `CLAUDE.md` + `LOG.md`, init git, help connect a remote, offer a literature review).
