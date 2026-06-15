---
name: zotero-lookup
description: >
  Resolve Zotero citations and item keys to their PDFs, metadata, and notes.
  Use this skill whenever the user's message contains a Zotero citation in any
  of these formats: [(Author et al., Year)](zotero://select/library/items/KEY),
  a bare zotero:// URI, or an 8-character Zotero item key referenced in context.
  Also use when the user asks to "look up", "find", or "read" a paper from their
  Zotero library. The citations tell you which papers to load so you can engage
  with the user's actual request knowledgeably.
---

# Zotero Lookup

This is a **context-loading** skill. Load the papers, then proceed with the user's actual request.

The CLI binary is at `/Users/zhangkai/.local/bin/zotero-cli`.

## Step 1: Extract keys

Parse the message for citations in any of these forms:
1. `[(Author, Year)](zotero://select/library/items/KEY)`
2. `zotero://select/library/items/KEY`
3. Bare 8-character key (when context makes it clear)

Also note the **citation context** (surrounding sentence) for each key — it tells you which aspects of the paper matter.

## Step 2: Resolve keys to files

```bash
python <path-to-this-skill>/scripts/zotero_resolve.py \
  "/Users/zhangkai/Zotero/zotero.sqlite" \
  "/Users/zhangkai/Zotero/storage" \
  KEY1 KEY2 KEY3
```

Output is JSON with `title`, `authors`, `year`, `abstract`, `pdf_paths`, and `notes` per key. Run once with all keys.

## Step 3: Read the PDFs

Use the `Read` tool on each path in `pdf_paths`. Read the full paper. If Zotero notes are attached, read those too — they contain the user's own annotations.

## Step 4: Produce citation-aware summaries

Summarize each paper through the lens of how it was cited — not a generic abstract rehash. If the citation supports a specific claim, focus on the results and formalism behind that claim. Preserve key equations and theorem statements when the conversation is technical; the user is a researcher who needs the actual content, not a high-level gloss.

For context-loading, plain-text math is fine. For written deliverables the user will read directly, use LaTeX (`$...$`, `$$...$$`).

Summary format:
```
**[Title]** ([Authors], [Year])
[Citation-aware summary]
[Your notes: ... (if Zotero notes exist)]
```

## Edge cases

- **Key not found**: tell the user and ask them to double-check.
- **PDF missing**: use the metadata and abstract; mention the file wasn't found.
- **No citation context**: fall back to a general summary (contribution, method, main results).

---

## zotero-cli Reference

Use `zotero-cli` for any library management tasks beyond citation lookup.

### Search

```bash
# Full-text / title search (default)
zotero-cli search "mechanism design"

# Semantic search (requires update-db to have been run)
zotero-cli search --mode semantic "fairness in resource allocation"

# Search by tag
zotero-cli search --mode tag "important,to-read"

# Search notes
zotero-cli search --mode notes "karma"

# Limit results and sort
zotero-cli search "equilibrium" --limit 10 --sort-by date --sort-direction desc
```

### Get item data

```bash
# Metadata for a known key
zotero-cli get metadata ITEM_KEY

# Full extracted text
zotero-cli get fulltext ITEM_KEY

# BibTeX entry
zotero-cli get bibtex ITEM_KEY

# PDF table of contents / outline
zotero-cli outline ITEM_KEY

# Child attachments and notes
zotero-cli get children ITEM_KEY

# Recently added items
zotero-cli get recent --limit 20

# All collections
zotero-cli get collections

# Items in a specific collection
zotero-cli get collection-items COLLECTION_KEY
```

### Annotations and notes

```bash
# List annotations on a paper
zotero-cli annotations list --item-key ITEM_KEY

# List notes on a paper
zotero-cli notes list --item-key ITEM_KEY

# Create a note (pipe text via stdin)
echo "My note content" | zotero-cli notes create --item-key ITEM_KEY --text -

# Update a note
zotero-cli notes update NOTE_KEY --text "Updated content"
```

### Edit metadata

```bash
zotero-cli edit ITEM_KEY --title "New Title"
zotero-cli edit ITEM_KEY --add-tags "reviewed,important"
zotero-cli edit ITEM_KEY --remove-tags "to-read"
zotero-cli edit ITEM_KEY --abstract "New abstract text"
```

### Add items

```bash
zotero-cli add doi 10.1145/1234567.1234568
zotero-cli add url https://arxiv.org/abs/2301.00001
zotero-cli add file /path/to/paper.pdf
```

### Collections

```bash
zotero-cli collections create "New Collection Name"
zotero-cli collections search "Karma"
zotero-cli collections manage --item-key ITEM_KEY --add COLLECTION_KEY
```

### Tags

```bash
# Rename a tag across all items
zotero-cli tags --tag "old-name" --remove "old-name" --add "new-name"

# List all tags
zotero-cli get tags
```

### Semantic DB

```bash
# Build / rebuild the semantic index (needed for --mode semantic)
zotero-cli db update

# Check index status
zotero-cli db status
```
