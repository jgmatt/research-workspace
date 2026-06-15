#!/usr/bin/env python3
"""
Resolve Zotero item keys to metadata and PDF paths.

Usage:
    python zotero_resolve.py <db_path> <storage_dir> KEY1 [KEY2 ...]

Output: JSON array, one object per key.

Each object has:
    key         - the item key
    found       - bool
    title       - str
    authors     - list of str
    year        - str
    abstract    - str
    pdf_paths   - list of str (absolute paths to PDF files)
    notes       - list of str (text content of note attachments)
    error       - str (only present on failure)
"""
import sys
import json
import sqlite3
import os


def resolve(db_path: str, storage_dir: str, keys: list[str]) -> list[dict]:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro&immutable=1", uri=True)
    c = conn.cursor()
    results = []

    for key in keys:
        result = {"key": key, "found": False}
        try:
            # Look up the item
            c.execute("SELECT itemID, itemTypeID FROM items WHERE key = ?", (key,))
            row = c.fetchone()
            if row is None:
                result["error"] = f"Key {key} not found in database"
                results.append(result)
                continue

            item_id, item_type_id = row
            result["found"] = True

            # Metadata fields
            c.execute(
                """SELECT f.fieldName, idv.value
                   FROM itemData id
                   JOIN itemDataValues idv ON id.valueID = idv.valueID
                   JOIN fields f ON id.fieldID = f.fieldID
                   WHERE id.itemID = ?""",
                (item_id,),
            )
            meta = dict(c.fetchall())
            result["title"] = meta.get("title", "")
            result["year"] = meta.get("date", "")[:4] if meta.get("date") else ""
            result["abstract"] = meta.get("abstractNote", "")

            # Authors
            c.execute(
                """SELECT c.firstName, c.lastName
                   FROM itemCreators ic
                   JOIN creators c ON ic.creatorID = c.creatorID
                   JOIN creatorTypes ct ON ic.creatorTypeID = ct.creatorTypeID
                   WHERE ic.itemID = ? AND ct.creatorType = 'author'
                   ORDER BY ic.orderIndex""",
                (item_id,),
            )
            result["authors"] = [
                f"{r[0]} {r[1]}".strip() if r[0] else r[1]
                for r in c.fetchall()
            ]

            # Attachments (children)
            c.execute(
                """SELECT i.itemID, i.key, ia.contentType, ia.path
                   FROM itemAttachments ia
                   JOIN items i ON ia.itemID = i.itemID
                   WHERE ia.parentItemID = ?""",
                (item_id,),
            )
            attachments = c.fetchall()

            pdf_paths = []
            notes = []

            for att_id, att_key, content_type, att_path in attachments:
                if content_type and "pdf" in content_type.lower():
                    # Zotero stores files as storage/<KEY>/<filename>
                    candidate = os.path.join(storage_dir, att_key)
                    if os.path.isdir(candidate):
                        for fname in os.listdir(candidate):
                            if fname.lower().endswith(".pdf"):
                                pdf_paths.append(os.path.join(candidate, fname))
                    # Also try att_path if it's an absolute path
                    if att_path and os.path.isfile(att_path):
                        pdf_paths.append(att_path)

                # Note items have itemTypeID for 'note'
                c.execute(
                    "SELECT itemTypeID FROM items WHERE itemID = ?", (att_id,)
                )
                type_row = c.fetchone()
                if type_row:
                    c.execute(
                        "SELECT typeName FROM itemTypes WHERE itemTypeID = ?",
                        (type_row[0],),
                    )
                    type_name_row = c.fetchone()
                    if type_name_row and type_name_row[0] == "note":
                        c.execute(
                            "SELECT note FROM itemNotes WHERE itemID = ?", (att_id,)
                        )
                        note_row = c.fetchone()
                        if note_row and note_row[0]:
                            notes.append(note_row[0])

            result["pdf_paths"] = pdf_paths
            result["notes"] = notes

        except Exception as e:
            result["error"] = str(e)

        results.append(result)

    conn.close()
    return results


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: zotero_resolve.py <db_path> <storage_dir> KEY1 [KEY2 ...]",
            file=sys.stderr,
        )
        sys.exit(1)

    db_path = sys.argv[1]
    storage_dir = sys.argv[2]
    keys = sys.argv[3:]
    print(json.dumps(resolve(db_path, storage_dir, keys), indent=2))
