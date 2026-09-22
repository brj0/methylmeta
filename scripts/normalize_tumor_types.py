#!/usr/bin/env python3
"""Validate and normalize tumor_types.yaml against vocabulary.yaml.

Two modes:

    --check   (default) Validate. Print every violation. Exit non-zero if any.
    --fix               Rewrite tumor_types.yaml applying only explicit maps.

Design rules:

* No fuzzy matching. Every mapping is explicit.
* ``null`` is preserved as-is; not conflated with ``"Unspecified"``.
* ``families`` is never silently emptied. Unmappable values are kept and
  reported.
* Case-insensitive matching is used for who_volume, site, lineage_detail.

Usage:
    python scripts/normalize_tumor_types.py
    python scripts/normalize_tumor_types.py --fix
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]
VOCAB_PATH = ROOT / "src/methylmeta/data/vocabulary.yaml"
TUMOR_PATH = ROOT / "src/methylmeta/data/tumor_types.yaml"


# ---------------------------------------------------------------------------
# Explicit alias maps. Add entries here when a new non-canonical value shows
# up; do NOT rely on fuzzy matching.
# ---------------------------------------------------------------------------

LINEAGE_BROAD_ALIASES: dict[str, str] = {
    # Composite lineage values → "Mixed"
    "Epithelial / mesenchymal": "Mixed",
    "Mixed epithelial / mesenchymal": "Mixed",
    "Epithelial / stromal": "Mixed",
    "Epithelial / myoepithelial": "Epithelial",
    "Neural / glial": "Mixed",
    "Neural / Schwannian": "Mixed",
    "Vascular / lymphatic": "Mixed",
    "Stromal / vascular": "Mixed",
    "Immune / stromal": "Mixed",
    "Pineal / neuronal": "Neural",
    "Multiple": "Unknown",
}

LINEAGE_DETAIL_ALIASES: dict[str, str] = {
    "plasma cell": "Plasma cell",
    "t-cell": "T-cell",
    "b-cell": "B-cell",
    "nk-cell": "NK-cell",
    "t/nk": "T/NK",
    "dendritic/stromal": "Dendritic/Stromal",
    "hematopoietic": "Hematopoietic",
    "plasmacytoid dendritic cell": "Plasmacytoid Dendritic Cell",
    "chondrogenic": "Chondrogenic",
}

SITE_ALIASES: dict[str, str] = {
    "Lymph Node": "Lymph node",
    "Salivary glands": "Salivary gland",
    "Bone (surface, in osteochondroma)": "Bone (surface)",
    "Sinonasal": "Sinonasal tract",
}

FAMILY_ALIASES: dict[str, str] = {
    "Myo-fibroblastic tumor": "myofibroblastic_tumor",
}


def slugify(value: str) -> str:
    """Convert a human-readable family name to canonical snake_case."""
    return (
        value.lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace("::", "_")
    )


def _ci_lookup(value: str, canonical: set[str]) -> str | None:
    """Case-insensitive lookup against a set of canonical strings."""
    if value in canonical:
        return value
    lowered = value.lower()
    for c in canonical:
        if c.lower() == lowered:
            return c
    return None


class Report:
    """Collect and print normalization violations."""

    def __init__(self) -> None:
        self.errors: list[tuple[str, str, str, str]] = []

    def add(self, acronym: str, field: str, value: Any, msg: str) -> None:
        self.errors.append((acronym, field, repr(value), msg))

    def emit(self) -> None:
        if not self.errors:
            return
        print(f"{len(self.errors)} violation(s) found:", file=sys.stderr)
        current = None
        for acronym, field, value, msg in self.errors:
            if acronym != current:
                print(f"\n  {acronym}:", file=sys.stderr)
                current = acronym
            print(f"    {field}: {value} — {msg}", file=sys.stderr)

    def __bool__(self) -> bool:
        return bool(self.errors)


def check_entry(
    acronym: str,
    entry: dict[str, Any],
    lookups: tuple,
    report: Report,
) -> dict[str, Any]:
    """Validate (and in fix mode, rewrite) a single tumor_type entry."""
    broad_set, detail_map, detail_union, who_set, site_set, family_set = (
        lookups
    )

    # ---- who_volume ----
    wv = entry.get("who_volume")
    if wv is not None and wv not in who_set:
        canonical = _ci_lookup(wv, who_set)
        if canonical is not None:
            entry["who_volume"] = canonical
        else:
            report.add(acronym, "who_volume", wv, "not in vocabulary")

    # ---- site ----
    site = entry.get("site")
    if site is not None and site not in site_set:
        canonical = _ci_lookup(site, site_set) or SITE_ALIASES.get(site)
        if canonical is not None:
            entry["site"] = canonical
        else:
            report.add(acronym, "site", site, "not in vocabulary")

    # ---- lineage_broad ----
    broad = entry.get("lineage_broad")
    if broad is not None and broad not in broad_set:
        canonical = LINEAGE_BROAD_ALIASES.get(broad) or _ci_lookup(
            broad, broad_set
        )
        if canonical is not None:
            entry["lineage_broad"] = canonical
            broad = canonical
        else:
            report.add(acronym, "lineage_broad", broad, "not in vocabulary")

    # ---- lineage_detail ----
    detail = entry.get("lineage_detail")
    if detail is not None:
        canonical_detail: str | None = None
        if detail in detail_union:
            canonical_detail = detail
        else:
            ci = _ci_lookup(detail, detail_union)
            if ci is not None:
                canonical_detail = ci
            elif detail.lower() in LINEAGE_DETAIL_ALIASES:
                canonical_detail = LINEAGE_DETAIL_ALIASES[detail.lower()]

        if canonical_detail is None:
            report.add(acronym, "lineage_detail", detail, "not in vocabulary")
        else:
            entry["lineage_detail"] = canonical_detail
            if broad in detail_map:
                allowed = {d.lower() for d in detail_map[broad]}
                if canonical_detail.lower() not in allowed:
                    report.add(
                        acronym,
                        "lineage_detail",
                        canonical_detail,
                        f"not valid under lineage_broad={broad!r}",
                    )

    # ---- families ----
    families = entry.get("families")
    if families:
        new_families: list[str] = []
        for fam in families:
            if fam in family_set:
                new_families.append(fam)
                continue
            if fam in FAMILY_ALIASES:
                new_families.append(FAMILY_ALIASES[fam])
                continue
            slug = slugify(fam)
            if slug in family_set:
                new_families.append(slug)
                continue
            # Unresolvable — keep the original and report.
            report.add(acronym, "families", fam, "not in vocabulary")
            new_families.append(fam)
        entry["families"] = new_families

    return entry


def normalize(mode: str) -> int:
    yaml = YAML()
    yaml.allow_duplicate_keys = True
    yaml.preserve_quotes = True
    yaml.width = 120
    yaml.representer.add_representer(
        type(None),
        lambda r, _: r.represent_scalar("tag:yaml.org,2002:null", "null"),
    )

    with VOCAB_PATH.open() as fh:
        vocab = yaml.load(fh)
    with TUMOR_PATH.open() as fh:
        data = yaml.load(fh)

    lineages = vocab["lineages"]
    broad_set = set(lineages.keys())
    detail_map = {k: list(v) for k, v in lineages.items()}
    detail_union = {d for values in lineages.values() for d in values}
    who_set = set(vocab["who_volumes"])
    site_set = set(vocab["sites"])
    family_set = set(vocab["families"])

    lookups = (
        broad_set,
        detail_map,
        detail_union,
        who_set,
        site_set,
        family_set,
    )
    report = Report()

    for acronym, entry in data["tumor_types"].items():
        check_entry(acronym, entry, lookups, report)

    report.emit()

    if mode == "fix":
        with TUMOR_PATH.open("w") as fh:
            yaml.dump(data, fh)
        return 1 if report else 0

    return 1 if report else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--check",
        action="store_true",
        default=True,
        help="Validate only (default).",
    )
    group.add_argument(
        "--fix",
        action="store_true",
        help="Rewrite tumor_types.yaml applying the explicit mappings.",
    )
    args = parser.parse_args()
    sys.exit(normalize("fix" if args.fix else "check"))


if __name__ == "__main__":
    main()
