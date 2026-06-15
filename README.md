# Research Workspace — AI in Practice

A clean, project-based structure for running a research project with Claude during the **AI in Practice** workshop and hackathon, plus a personal spec you can grow long after the workshop ends.

## Getting started

1. **Fill in `CLAUDE.md`** with your profile (name, research interests, communication style) and any standing rules for Claude. This file is read at the start of every session, so Claude works the way you want.
2. **Open this folder with Claude** and start working.

## Starting a project

When you have your group and topic, create a project under `projects/`. The quickest way is to copy `projects/example/` and rename it, or follow the short procedure in `notes/starting-a-project.md`. Each project gets:

- its own `CLAUDE.md` — the project definition (group, topic, methods, research question),
- a `LOG.md` — an append-only record of changes and decisions.

Then initialise git in the project folder and connect a remote (steps in `notes/starting-a-project.md`). Claude can run the `literature-review` skill to help you find a strong research question; write it into the project's `CLAUDE.md` once agreed.

## What's in here

| Path | What it is |
|------|------------|
| `CLAUDE.md` | Workspace entry point and your researcher profile. Fill it in yourself. |
| `projects/` | One folder per project, each with its own `CLAUDE.md` and `LOG.md`. `projects/example/` is a template to copy. |
| `spec/` | Your **project-independent** source of truth: definitions, models, and notation that span all your research (typst). Not needed for the hackathon — explore and grow it afterwards. See `notes/the-spec.md`. |
| `references/` | `references.bib` collecting every source. |
| `skills/` | Reusable skills for Claude, including a minimal `literature-review` skill. Skills must be registered with Claude before use — see the skill file. |
| `notes/` | Short procedures: `starting-a-project.md` and `the-spec.md`. |

## Key ideas

- **CLAUDE.md** is read first every session — the workspace one is your profile, each project has its own.
- **LOG.md** (per project) is an append-only diary of changes and decisions so nothing gets lost.
- **spec/** is your standing, project-independent reference, separate from any single project.
- There is intentionally **no STATE.md** anywhere.
