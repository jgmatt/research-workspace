## About me

- **Name / what to call me:** [name]
- **Research interests:** [topic]
- **Preferred communication style:** [e.g. concise, no fluff; detailed; English; math in LaTeX]

## Rules for Claude

- No LLM-style language: Don't use em dashes.
- [rule]: [content]

## How this workspace works

Project-based research workspace.

```
research-workspace/
├── CLAUDE.md                     this file: entry point + researcher profile
├── README.md                     overview and how to get started
├── spec/
│   ├── spec.typ                  project-independent source of truth
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

## Basic instructions

- Inside a project, read that project's `CLAUDE.md` first, and append to its `LOG.md` after any substantial work or decision (newest entry on top).
- Put every source in `references/references.bib`
- Skills are inside `skills/`, but need to be actively added so Claude can use them
- The spec is not filled during the hackathon, see `notes/the-spec.md` for what it is and how to compile it.
