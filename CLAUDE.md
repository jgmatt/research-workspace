<!--
========================================================================
  CLAUDE.md — WORKSPACE ENTRY POINT (AI in Practice)
========================================================================
  Read this file at the start of every session. It has two parts:

    1. ABOUT ME — a profile of the researcher who owns this workspace.
       This is a SCAFFOLD with empty <placeholders>. It is filled once,
       by interview, the first time the user arrives.

    2. INSTRUCTIONS — how Claude behaves here, plus two triggers:
       the greeting (sets up the workspace) and the project kickoff.

  Trigger summary (details below):
    - "Hi Claude, I'm <name>."  -> follow notes/getting-started.md
    - "Let's start a project."  -> follow "Starting a project" below
========================================================================
-->

# CLAUDE.md — AI in Practice workspace

## About me

<!--
SCAFFOLD. Empty until the first session. Do NOT invent content — it is
filled by the getting-started interview (see notes/getting-started.md).
-->

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

<!--
SCAFFOLD. Filled during the interview. Each rule should come with a
short example so the intent is unambiguous. Examples below show the
format; replace them.
-->

- <rule> — e.g. "<example>"
- <rule> — e.g. "<example>"

## How this workspace works

This is a project-based research workspace for the AI in Practice hackathon. The pieces:

- **This CLAUDE.md** — the workspace entry point and the researcher's profile. Read first, every session.
- **`spec/`** — the researcher's own, **project-independent** single source of truth: the definitions, models, and notation that hold across all of their research (typst). It is not needed for the hackathon. It is here for the researcher to grow and explore on their own after the workshop.
- **`references/`** — `references.bib` holding all sources, plus any review notes.
- **`skills/`** — reusable procedures Claude can run (e.g. a minimal literature review).
- **`notes/`** — workspace notes, including `getting-started.md` (the setup procedure).
- **`projects/`** — one folder per hackathon project. Each project has its **own CLAUDE.md** (the project definition) and a **LOG.md** (an append-only record of changes and decisions). There is no STATE.md anywhere.

## Standing instructions

- Read this CLAUDE.md at the start of every session.
- When working inside a project, read that project's `CLAUDE.md` first, and append to its `LOG.md` after any substantial work or decision (newest entry at the top).
- `spec/` is the researcher's project-independent source of truth (definitions, models, notation). Do not fill it during the hackathon. Point the researcher to it as something to explore and grow after the workshop.
- Put every source in `references/references.bib`. Use the **literature-review** skill when searching for related work.
- When uncertain, flag the uncertainty and continue. When a change has large downstream consequences, stop and ask first.

## The spec

- **Where:** `spec/spec.typ`, compiled to `spec/spec.pdf`.
- **What:** the researcher's own **project-independent single source of truth**: the definitions, models, and notation that hold across all of their research, written precisely and once so every project can build on the same foundation. It is **not** part of any hackathon project and is not needed to do the hackathon. It is here for the researcher to explore and grow on their own **after** the workshop.
- **How to use it:** it is a typst file. Edit `spec.typ`, then compile it to see the PDF. Whenever you edit a file in `spec/`, regenerate the PDF so the change is visible.
  - Compile once: `typst compile spec/spec.typ` (produces `spec/spec.pdf`).
  - Live preview while editing: `typst watch spec/spec.typ`.
  - If `typst` is not installed: get it from https://github.com/typst/typst (or `brew install typst` on macOS). A Python fallback is `pip install typst` then `python3 -c "import typst; typst.compile('spec/spec.typ', output='spec/spec.pdf')"`.
- **During the hackathon:** do not fill the spec. Just make sure the researcher knows it exists and what it is for.

## Trigger: "Hi Claude, I'm <name>."

When the user greets you this way **and the "About me" section above is still empty**, follow the procedure in **`notes/getting-started.md`**: introduce yourself, explain the workspace, and run the setup interview to fill in this CLAUDE.md. If "About me" is already filled, just greet them normally and ask what they would like to work on.

## Trigger: "Let's start a project."

When the user says this, run the project kickoff below.

### Starting a project

1. **Say hello to the project.** Tell the group you are excited to work with them. Explain that you will run a short interview to set up the project, and that they should do it together on one laptop so everyone is on the same page.

2. **Interview the group.** Capture:
   - Group name.
   - Members, and each member's research interests and expertise.
   - The topic they want to work on.
   - The methods they want to use.

3. **Create the project folder** at `projects/<group-name>/` (kebab-case). Inside it, create:
   - **`CLAUDE.md`** — the project definition (template below). This replaces the workspace "About me" with project facts. No STATE.md.
   - **`LOG.md`** — an append-only log. Newest entry at the top. Record decisions, changes, and dead ends. Use the format from the workspace skills (date/time, focus, what happened, decisions, next).

4. **Initialise version control.** Run `git init` inside the project folder and make a first commit once `CLAUDE.md` and `LOG.md` exist. Then walk the group through creating a remote (see "Creating a remote" below).

5. **Offer a literature review.** Tell the group you can help them find a strong, well-scoped research question by running the **literature-review** skill. Once the group agrees on a research question, write it into the project's `CLAUDE.md`.

### Project CLAUDE.md template

```markdown
# Project: <group / project name>

## Group
- **Name:** <group name>
- **Members & expertise:**
  - <member> — <interests / expertise>

## Topic
<one or two sentences>

## Methods
<the approaches / tools the group plans to use>

## Research question
<filled in after the literature review, once the group agrees>

## Pointers
- Log of changes and decisions: ./LOG.md
- Sources: ../../references/references.bib
```

### Creating a remote

Guide the group through this manually, one step at a time. Wait for them to finish each step before giving the next. Use the actual group name and paste-ready commands.

1. **Pick a host.** Ask whether the group uses GitHub or GitLab, and have one member open it in the browser and sign in.
2. **Create an empty repository.** On GitHub: top-right "+" -> "New repository". Name it `<group-name>`, choose Private, and **do not** add a README, .gitignore, or license (the local folder already has files). Click "Create repository". (GitLab: "New project" -> "Create blank project", same idea, no README.)
3. **Copy the repository URL** from the page (the HTTPS URL ending in `.git`).
4. **Connect the local project to it.** In the project folder, run:
   ```
   git remote add origin <paste-the-url>
   git branch -M main
   git push -u origin main
   ```
5. **First push and credentials.** When prompted, they sign in. GitHub no longer accepts account passwords over HTTPS, so if it asks for a password they need a Personal Access Token (GitHub: Settings -> Developer settings -> Personal access tokens). Help them generate one if needed.
6. **Confirm it worked.** Refresh the repository page in the browser; the files should be there. From now on the group commits and runs `git push` as they work.

Always confirm with the group before pushing, and keep the repo Private unless they choose otherwise.
