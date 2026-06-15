# Research Workspace — AI in Practice

A project-based research workspace for the **AI in Practice** workshop and hackathon. It gives you a clean, opinionated structure for running a research project with Claude as your research assistant, plus a personal spec you can grow long after the workshop ends.

## Getting started

Open this folder with Claude, then say:

> **Hi Claude, I'm \<name\>.**

Claude will introduce itself, explain how the workspace is organised, and run a short interview to set up your workspace profile (it fills in `CLAUDE.md`).

When you have your hackathon group together, say:

> **Let's start a project.**

Claude will interview the group, create a project folder under `projects/` with its own `CLAUDE.md` and `LOG.md`, initialise git, help you connect a remote, and offer a literature review to find a strong research question.

## What's in here

| Path | What it is |
|------|------------|
| `CLAUDE.md` | The workspace entry point and your researcher profile. Read by Claude at the start of every session. Holds the two triggers above. |
| `notes/getting-started.md` | The setup procedure Claude follows for the greeting interview. |
| `projects/` | One folder per hackathon project. Each gets its own `CLAUDE.md` (project definition) and `LOG.md` (append-only record of changes and decisions). No STATE.md. |
| `spec/` | Your **project-independent** single source of truth: definitions, models, and notation that span all your research (typst). Not needed for the hackathon — it's here for you to explore and grow afterwards. Compile with `typst compile spec/spec.typ`. |
| `references/` | `references.bib` collecting every source. |
| `skills/` | Reusable procedures for Claude, including a minimal `literature-review` skill (tailor it to your needs and register it with Claude — see the skill for how). |

## Key ideas

- **CLAUDE.md** is the entry point Claude reads first, every session — the workspace one is your profile, and each project has its own.
- **LOG.md** (per project) is an append-only diary of changes and decisions so nothing gets lost.
- **spec/** is your standing, project-independent reference, separate from any single project.
- There is intentionally **no STATE.md** anywhere.
