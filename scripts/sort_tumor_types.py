#!/usr/bin/env python3
"""Sort methylmeta's tumor_types.yaml alphabetically by acronym.

Usage:
    python scripts/sort_tumor_types.py            # sort and write in place
    python scripts/sort_tumor_types.py --check     # exit 1 if unsorted (CI)

Caveat: a standalone comment that describes a whole *block* of several
entries below it (e.g. "# --- Added 2026-09: ... ---") gets attached to
just the next entry and moves with that one entry alone once sorted -
review/relocate such section comments by hand afterward if they were
meant to describe more than one entry.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

TUMOR_TYPES_PATH = (
    Path(__file__).resolve().parent.parent
    / "src"
    / "methylmeta"
    / "data"
    / "tumor_types.yaml"
)

# Matches a top-level entry key line, e.g. "  ADCC:" (2-space indent,
# nothing after the colon).
ENTRY_HEADER_RE = re.compile(r"^  ([A-Za-z0-9_\-]+):[ \t]*$")


def split_entries(body: str) -> list[tuple[str, str]]:
    """Split the tumor_types: section body into (acronym, raw_text) blocks.

    We walk the file line by line and only start a new block when we see
    a line matching ENTRY_HEADER_RE (a real "  ACRONYM:" key). Every other
    line - the entry's fields, blank lines, comments - gets appended to
    `buffer` and stays glued to whichever key came before it. That's how
    a comment sitting directly above an entry travels with it when we
    later re-sort: it's just part of that entry's raw text, not a
    separate thing we track.
    """
    lines = body.splitlines(keepends=True)
    entries: list[tuple[str, str]] = []
    buffer: list[str] = []
    current_key: str | None = None

    for line in lines:
        match = ENTRY_HEADER_RE.match(line)
        if match:
            if current_key is not None:
                # Buffer so far (previous entry's fields) is complete.
                entries.append((current_key, "".join(buffer)))
            elif "".join(buffer).strip():
                # Preserve leading comments as a pinned entry.
                entries.append(("", "".join(buffer)))
            current_key = match.group(1)
            buffer = [line]
        else:
            buffer.append(line)

    if current_key is not None:
        entries.append((current_key, "".join(buffer)))
    elif "".join(buffer).strip():
        # Same "leading comment, no entry yet" case, but for a file that ends
        # without ever matching ENTRY_HEADER_RE at all.
        entries.append(("", "".join(buffer)))

    return entries


def sort_tumor_types(text: str) -> str:
    """Return `text` with entries under tumor_types: sorted by acronym."""
    header, sep, rest = text.partition("tumor_types:\n")
    if not sep:
        raise ValueError("Could not find a 'tumor_types:' section header.")

    entries = split_entries(rest)

    # `pinned` holds blocks with key "" - i.e. not a real tumor-type entry,
    # just a leading comment that appeared before the first key.
    pinned = [e for e in entries if not e[0]]
    real_entries = [e for e in entries if e[0]]
    sorted_entries = sorted(real_entries, key=lambda e: e[0].upper())

    # Strip each block down to its content (no leading/trailing blank
    # lines), then rejoin with exactly one blank line between blocks.
    blocks = [raw.strip("\n") for _, raw in pinned + sorted_entries]
    body = "\n\n".join(blocks) + "\n"

    return f"{header}tumor_types:\n{body}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if the file isn't already sorted; don't write.",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=TUMOR_TYPES_PATH,
        help="Path to tumor_types.yaml (default: package data file).",
    )
    args = parser.parse_args()

    original = args.path.read_text(encoding="utf-8")
    sorted_text = sort_tumor_types(original)

    # Safety net: re-sorting must never change the parsed data, only the
    # order entries appear in the file. If this trips, split_entries()
    # mis-parsed something (e.g. a comment containing a line that looks
    # like an entry header) - fix the parser, don't silently write.
    before = yaml.safe_load(original)["tumor_types"]
    after = yaml.safe_load(sorted_text)["tumor_types"]
    if before != after:
        raise SystemExit(
            "Sorting would change the parsed data - aborting without "
            "writing. This means split_entries() mis-parsed an entry "
            "(e.g. a comment line matched the entry-header pattern)."
        )

    if sorted_text == original:
        print(f"{args.path}: already sorted ({len(after)} entries).")
        return

    if args.check:
        print(f"{args.path}: NOT sorted alphabetically.")
        sys.exit(1)

    args.path.write_text(sorted_text, encoding="utf-8")
    print(f"{args.path}: sorted {len(after)} entries.")


if __name__ == "__main__":
    main()
