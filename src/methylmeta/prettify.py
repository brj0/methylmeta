from __future__ import annotations

import re

import pandas as pd


def prettify_str(text: str | None) -> str | None:
    """Clean diagnosis / site strings."""
    if pd.isna(text):
        return None
    if not isinstance(text, str):
        text = str(text)
    text = text.strip()
    if not text:
        return None

    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*[,;]+\s*", ", ", text)
    text = re.sub(r"\s*/\s*", " / ", text)
    text = re.sub(r"\s*&\s*", " & ", text)
    text = text.rstrip(",; ")

    fixes = {
        "Craniopharyngeoma": "Craniopharyngioma",
        "Craniopharyngiom": "Craniopharyngioma",
        "craniopharyngeoma": "Craniopharyngioma",
        "sinunasal": "sinonasal",
        "sinunasal ": "sinonasal ",
        "scull": "skull",
        "maxilary": "maxillary",
        "nassal": "nasal",
        "bonemarrow": "bone marrow",
    }
    for wrong, right in fixes.items():
        text = text.replace(wrong, right)

    if text:
        text = text[0].upper() + text[1:]
    return text
