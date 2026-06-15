# Starting a project

## Steps

1. **Create the project folder** at `projects/<project-name>/`. Inside it, create:
   - **`CLAUDE.md`** — the project definition (template below). No STATE.md.
   - **`LOG.md`** — an append-only log. Newest entry at the top. Record decisions, changes, and dead ends (date/time, focus, what happened, decisions, next).

1. **Initialise version control.** Run `git init` inside the project folder and make a first commit once `CLAUDE.md` and `LOG.md` exist. Then create a remote (see "Creating a remote" below).

2. **Offer a literature review.** Use Claude to find a strong, well-scoped research question by running the **literature-review** skill (adjust as needed). Once the group agrees on a research question, write it into the project's `CLAUDE.md`.

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

1. **Pick a host.** GitHub or GitLab
2. **Create an empty repository.** 
3. **Copy the repository URL**
4. **Connect the local project to it.** In the project folder, run:
   ```
   git remote add origin <paste-the-url>
   git branch -M main
   git push -u origin main
   ```
5. **First push and credentials.** You can create a Personal Access Token (GitHub: Settings -> Developer settings -> Personal access tokens) for Claude to interact with your git if you want.
6. **Confirm it worked.** Refresh the repository page in the browser, the files should be there.
