from __future__ import annotations

import difflib
import re
from dataclasses import dataclass
from functools import lru_cache

import yaml

from methylmeta.paths import TUMOR_TYPES_PATH


@dataclass
class TumorType:
    """One entry from tumor_types.yaml - the WHO-acronym vocabulary."""

    acronym: str
    name: str
    who_volume: str | None = None
    site: str | None = None
    lineage_broad: str | None = None
    lineage_detail: str | None = None
    families: list[str] | None = None
    parent: str | None = None

    def __str__(self) -> str:
        bits = [f"{self.acronym} ({self.name})"]
        if self.site:
            bits.append(f"site={self.site}")
        if self.who_volume:
            bits.append(f"volume={self.who_volume}")
        return " - ".join(bits)


@lru_cache(maxsize=1)
def _load() -> dict[str, TumorType]:
    with TUMOR_TYPES_PATH.open() as f:
        raw = yaml.safe_load(f)
    return {
        acronym: TumorType(acronym=acronym, **entry)
        for acronym, entry in raw.items()
    }


def get_tumor_type(acronym: str) -> TumorType | None:
    """Look up a single WHO acronym's full entry, or None if unknown."""
    return _load().get(acronym)


def all_tumor_types() -> list[TumorType]:
    """Every entry in tumor_types.yaml."""
    return list(_load().values())


def fuzzy_word_score(query: str, text: str) -> float:
    """Score how well query words approximately match words in text."""
    query_words = re.findall(r"\w+", query.lower())
    text_words = re.findall(r"\w+", text.lower())

    if not query_words or not text_words:
        return 0.0

    if len(query_words) == 1:
        return max(
            difflib.SequenceMatcher(None, query_words[0], word).ratio()
            for word in text_words
        )

    scores = [
        max(
            difflib.SequenceMatcher(None, query_word, text_word).ratio()
            for text_word in text_words
        )
        for query_word in query_words
    ]

    return sum(scores) / len(scores)


def search_tumor_types(query: str, limit: int = 10) -> list[TumorType]:
    """Find WHO tumor types matching a free-text query.

    This is the tool for turning a raw diagnosis string (e.g. "Sinonasal
    squamous cell carcinoma") into methylation_class candidates: substring
    matches against name/site/family come first, then fuzzy name matches.
    Not a substitute for judgement on which candidate is actually correct,
    but narrows hundreds of acronyms down to a handful worth checking.
    """
    query_lower = query.lower().strip()
    if not query_lower:
        return []

    substring_hits: list[TumorType] = []
    fuzzy_hits: list[tuple[float, TumorType]] = []

    for tt in all_tumor_types():
        haystack = " ".join(
            filter(
                None,
                [
                    tt.acronym,
                    tt.name,
                    tt.who_volume,
                    tt.site,
                    tt.lineage_broad,
                    tt.lineage_detail,
                    " ".join(tt.families or []),
                    tt.parent,
                ],
            )
        ).lower()

        if query_lower in haystack:
            substring_hits.append(tt)
            continue

        score = fuzzy_word_score(query_lower, tt.name)
        if score >= 0.75:
            fuzzy_hits.append((score, tt))

    fuzzy_hits.sort(key=lambda pair: pair[0], reverse=True)

    results = substring_hits + [tt for _, tt in fuzzy_hits]
    return results[:limit]
