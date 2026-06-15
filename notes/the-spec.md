# The spec

Reference for `spec/`, pointed to from `../CLAUDE.md`.

- **Where:** `spec/spec.typ`, compiled to `spec/spec.pdf`.
- **What:** the researcher's own **project-independent single source of truth**: the definitions, models, and notation that hold across all of their research, written precisely and once so every project can build on the same foundation. It is **not** part of any hackathon project and is not needed to do the hackathon. It is here for the researcher to explore and grow on their own **after** the workshop.
- **During the hackathon:** do not fill the spec. Just make sure the researcher knows it exists and what it is for.

## How to compile

It is a typst file. Edit `spec.typ`, then compile so the PDF reflects the change. Whenever you edit a file in `spec/`, regenerate the PDF.

- Compile once: `typst compile spec/spec.typ` (produces `spec/spec.pdf`).
- Live preview while editing: `typst watch spec/spec.typ`.
- If `typst` is not installed: get it from https://github.com/typst/typst (or `brew install typst` on macOS). A Python fallback is `pip install typst` then `python3 -c "import typst; typst.compile('spec/spec.typ', output='spec/spec.pdf')"`.
