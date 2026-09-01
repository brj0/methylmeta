"""Fetch and cache public study descriptions for GEO and ArrayExpress.

Both GEO and ArrayExpress  expose the study title/summary/design as structured
text or JSON.

- GEO (``GSE...``): a plain ``key: value`` text dump at
  ``acc.cgi?...&form=text&view=quick`` - series-level fields only, no
  per-sample rows.
- ArrayExpress (``E-MTAB-...`` etc.): a JSON document from the BioStudies
  REST API.

Results are cached to disk (one small text file per dataset_id) so a
dataset is only fetched once, even across separate agent runs.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import httpx

from methylmeta.paths import CACHE_DIR

STUDY_INFO_CACHE_DIR = CACHE_DIR / "study_descriptions"
STUDY_INFO_CACHE_DIR.mkdir(parents=True, exist_ok=True)

_GEO_RE = re.compile(r"^GSE\d+$")
_ARRAYEXPRESS_RE = re.compile(r"^E-[A-Z]+-\d+$")

_TIMEOUT = 15.0

# Fields worth keeping from a GEO series text record; everything else
# (contributors, contact info, supplementary file lists, ...) is noise
# for the purpose of picking a methylation_class / diagnosis mapping.
_GEO_FIELDS_OF_INTEREST = (
    "Series_title",
    "Series_summary",
    "Series_overall_design",
    "Series_type",
)

# BioStudies attribute names worth surfacing.
_BIOSTUDIES_ATTRS_OF_INTEREST = {
    "title",
    "description",
    "study type",
    "organism",
}


def _cache_path(dataset_id: str) -> Path:
    return STUDY_INFO_CACHE_DIR / f"{dataset_id}.txt"


def _fetch_geo(dataset_id: str) -> str:
    url = (
        "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi"
        f"?acc={dataset_id}&targ=self&form=text&view=quick"
    )
    response = httpx.get(url, timeout=_TIMEOUT, follow_redirects=True)
    response.raise_for_status()
    text = response.text

    if not text.strip() or text.lstrip().startswith("<"):
        raise ValueError(f"GEO returned no record for {dataset_id!r}.")

    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("!"):
            continue
        key, _, value = line[1:].partition(" = ")
        if key in _GEO_FIELDS_OF_INTEREST and value:
            lines.append(f"{key.replace('Series_', '')}: {value}")

    if not lines:
        raise ValueError(f"GEO record for {dataset_id!r} had no summary.")

    return "\n".join(lines)


def _collect_biostudies_attrs(node: object, out: dict[str, str]) -> None:
    """Recursively pull interesting name/value attributes from JSON."""
    if isinstance(node, dict):
        attrs = node.get("attributes")
        if isinstance(attrs, list):
            for attr in attrs:
                name = str(attr.get("name", "")).strip().lower()
                value = attr.get("value")
                if (
                    name in _BIOSTUDIES_ATTRS_OF_INTEREST
                    and isinstance(value, str)
                    and value
                    and name not in out
                ):
                    out[name] = value
        for value in node.values():
            _collect_biostudies_attrs(value, out)
    elif isinstance(node, list):
        for item in node:
            _collect_biostudies_attrs(item, out)


def _fetch_arrayexpress(dataset_id: str) -> str:
    url = f"https://www.ebi.ac.uk/biostudies/api/v1/studies/{dataset_id}"
    response = httpx.get(url, timeout=_TIMEOUT, follow_redirects=True)
    response.raise_for_status()
    payload = response.json()

    attrs: dict[str, str] = {}
    _collect_biostudies_attrs(payload, attrs)

    if not attrs:
        raise ValueError(
            f"BioStudies record for {dataset_id!r} had no usable attributes."
        )

    return "\n".join(f"{key}: {value}" for key, value in attrs.items())


def fetch_study_description(dataset_id: str, *, refresh: bool = False) -> str:
    """Return a short public description of a GEO/ArrayExpress study.

    Cached on disk after the first successful fetch, so repeated agent
    runs (and repeated tool calls within one run) don't hit the network
    again. Returns a human-readable "not available" message instead of
    raising when the dataset_id isn't a recognized public accession, or
    when the fetch fails - a missing description shouldn't block the
    agent, it's just extra context when available.
    """
    cache_path = _cache_path(dataset_id)
    if cache_path.exists() and not refresh:
        return cache_path.read_text(encoding="utf-8")

    if _GEO_RE.match(dataset_id):
        fetcher = _fetch_geo
    elif _ARRAYEXPRESS_RE.match(dataset_id):
        fetcher = _fetch_arrayexpress
    else:
        return (
            f"{dataset_id!r} is not a recognized GEO or ArrayExpress "
            "accession; no public study description available."
        )

    try:
        description = fetcher(dataset_id)
    except (httpx.HTTPError, ValueError, json.JSONDecodeError) as exc:
        return (
            f"Could not fetch a public study description for "
            f"{dataset_id!r}: {type(exc).__name__}: {exc}"
        )

    cache_path.write_text(description, encoding="utf-8")
    return description
