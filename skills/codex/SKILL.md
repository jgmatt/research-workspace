---
name: codex
description: "Delegate tasks to OpenAI Codex CLI. Use this skill whenever the user wants to hand off a task to Codex, do web search, run Codex on a project, use `codex exec` to implement or review code, automate coding with Codex, or delegate general work to Codex. Trigger even if the user just says \"use Codex\", \"run this with Codex\", \"let Codex handle it\", or \"ask Codex to fix this\"."
---

# Delegate Tasks to OpenAI Codex CLI

## ⚠️ STOP — Session tracking is mandatory. Do this FIRST, before writing any codex command.

**Step 1.** Extract the active session UUID — use `grep 'Active session'`, NOT `-A1` on the heading (blank lines will fool it):
```sh
grep 'Active session' /path/to/project/CLAUDE.md
```
The output will be `- Active session: <uuid>` if one exists, or empty if none.

**Step 2.**
- **If a UUID is found**: ALWAYS resume that session. Do not start a new one.
  ```sh
  # Read-only inspection
  codex -C /path -s read-only exec resume <UUID> "[prompt]"
  # Making changes
  codex -C /path -s workspace-write exec resume <UUID> "[prompt]"
  # Long prompt via stdin
  cat prompt.txt | codex -C /path -s workspace-write exec resume <UUID> -
  ```
  Do NOT replace the UUID in CLAUDE.md with any new session id that appears in Codex output.

- **If no UUID is found** (grep returned empty): start a fresh run, capture the new session id from the output line `session id: <uuid>`, then write it to CLAUDE.md under the `## Codex` section **without a blank line** between the heading and the entry:
  ```md
  ## Codex
  - Active session: <uuid>
  ```
  Keep this format exactly — no blank line — so future greps always find it.

**Never skip this step.** Failing to resume loses all session context. If you wrote a codex command without first running the grep, discard it and redo from Step 1.

Note: `/rename` requires an interactive TTY and cannot be automated — always track sessions by UUID.

## Interface

- **`codex exec`** — preferred for all delegation; stable, non-interactive, scriptable.
- **`codex`** (interactive) — only when you need live slash commands.
- **`codex mcp-server`** — exposes Codex over stdio to MCP clients (experimental).

## Preflight

```sh
codex login status          # check auth
codex login                 # or --device-auth, or: printenv OPENAI_API_KEY | codex login --with-api-key
codex exec --help           # verify available flags before relying on them
```

## Key flags

| Flag | When to use |
|------|-------------|
| `-C <path>` | always — set working directory |
| `-s read-only` | inspection / review |
| `-s workspace-write` | making changes inside the workspace |
| `--add-dir <path>` | writing outside the workspace |
| `-m <model>` / `-p <profile>` | specific model or config |
| `--search` | only when live web search is needed |
| `--ephemeral` | don't persist session rollout files |
| `--json` | newline-delimited JSON event stream |
| `-o <file>` | write final assistant message to file |
| `--output-schema <schema.json>` | enforce a JSON shape on the final answer |
| `--skip-git-repo-check` | directory is not a git repo |
| `--yolo` | only in hardened envs, user explicitly requested |

Note: `-a/--ask-for-approval` exists in some builds but not all — check `--help` before using it.

## Delegation patterns

All commands use the resume form (UUID from CLAUDE.md, obtained in the mandatory Step 1 above):

```sh
# Read-only analysis
codex -C /path -s read-only exec resume <UUID> "[prompt]"

# Implement changes
codex -C /path -s workspace-write exec resume <UUID> "[prompt]"

# Long prompt via stdin
cat prompt.txt | codex -C /path -s workspace-write exec resume <UUID> -

# Fork the session (creates a new branch; update CLAUDE.md with the new UUID)
codex -C /path fork <UUID>
```

## Interactive slash commands

`/model` · `/fast` · `/permissions` · `/plan` · `/status` · `/compact` · `/diff` · `/review` · `/mention <file>` · `/mcp` · `/agent` · `/new` · `/resume` · `/fork` · `/init`

## Prompting tips

Include: working directory, desired outcome, files to inspect first, constraints, tests to run, output format. Tell Codex to inspect before editing and keep changes minimal.

**When resuming an existing session, keep prompts short.** A resumed session already has context from prior tasks — files Codex read, code it wrote, decisions it made. Do not re-specify what Codex already knows. Instead, reference it: "You built `spare_bus_tabular.py` in this session. Now implement the figure script following the same style. Key differences: ..." Re-explaining prior context wastes tokens with no benefit.

## Avoid

- Don't use interactive `codex` when `codex exec` suffices.
- Don't use `--yolo` unless explicitly intended.
- Don't use `--full-auto` for non-interactive runs where an approval prompt could deadlock.
