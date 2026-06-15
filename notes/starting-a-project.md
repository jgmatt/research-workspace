# Starting a project — kickoff procedure

This is the procedure behind the **"Let's start a project."** trigger in `../CLAUDE.md`. Follow it step by step.

## Steps

1. **Say hello to the project.** Tell the group you are excited to work with them. Explain that you will run a short interview to set up the project, and that they should do it together on one laptop so everyone is on the same page.

2. **Interview the group.** Capture:
   - Group name.
   - Members, and each member's research interests and expertise.
   - The topic they want to work on.
   - The methods they want to use.

3. **Create the project folder** at `projects/<group-name>/` (kebab-case). Inside it, create:
   - **`CLAUDE.md`** — the project definition (template below). No STATE.md.
   - **`LOG.md`** — an append-only log. Newest entry at the top. Record decisions, changes, and dead ends (date/time, focus, what happened, decisions, next).

4. **Initialise version control.** Run `git init` inside the project folder and make a first commit once `CLAUDE.md` and `LOG.md` exist. Then walk the group through creating a remote (see "Creating a remote" below).

5. **Offer a literature review.** Tell the group you can help them find a strong, well-scoped research question by running the **literature-review** skill. Once the group agrees on a research question, write it into the project's `CLAUDE.md`.

## Project CLAUDE.md template

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

## Creating a remote

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
