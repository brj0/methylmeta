#!/usr/bin/env python
"""Find datasets in configs/datasets/ that have NO raw IDAT files online.

Nothing big is downloaded; only small listings are queried:

  GSE*      1. ftp.ncbi.nlm.nih.gov/geo/series/<grp>/<acc>/suppl/filelist.txt
               (GEO's index of what is inside <acc>_RAW.tar)
            2. fallback: GEO text API (per-sample supplementary file names),
               stopped at the first .idat found
            3. fallback: HEAD on <acc>_RAW.tar (reported as UNKNOWN)
  E-MTAB-*  BioStudies file list API, counting *.idat entries
  others    GDC files API (data_format == IDAT) for that project

NCBI throttles aggressive clients (HTTP 403/429/503), so requests are
retried with exponential backoff and few workers are used by default.

Usage:
    python scripts/check_idats.py                    # all configs
    python scripts/check_idats.py GSE90496 GSE109381 # only these
    python scripts/check_idats.py --recheck          # only UNKNOWN rows
                                                     # of the previous report
    python scripts/check_idats.py --workers 2 --out idat_report.tsv

Verdicts:
    OK       n IDAT files found
    MISSING  listing was read fine, but contains zero IDATs
    UNKNOWN  could not decide (throttled, custom cohort, network error)
"""

from __future__ import annotations

import argparse
import http.client
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CONFIGS = Path(__file__).resolve().parent.parent / "configs" / "datasets"
TIMEOUT = 60
RETRIES = 5
RETRY_CODES = {403, 429, 500, 502, 503, 504}
UA = {"User-Agent": "methylmeta-check-idats/1.1 (research; urllib)"}

Result = tuple[str, int | None, str]

# Errors worth retrying: network trouble and truncated bodies.
TRANSIENT = (
    urllib.error.URLError,
    http.client.HTTPException,  # incl. IncompleteRead
    ConnectionError,
    TimeoutError,
)


def _backoff(attempt: int) -> None:
    time.sleep(2**attempt)  # 1, 2, 4, 8 s


def _open(
    url: str,
    method: str = "GET",
) -> http.client.HTTPResponse:
    """Open a URL, retrying with backoff on throttling / server errors."""
    for attempt in range(RETRIES):
        req = urllib.request.Request(url, method=method, headers=UA)
        try:
            return urllib.request.urlopen(req, timeout=TIMEOUT)
        except urllib.error.HTTPError as exc:
            if exc.code not in RETRY_CODES or attempt == RETRIES - 1:
                raise
        except TRANSIENT:
            if attempt == RETRIES - 1:
                raise
        _backoff(attempt)
    raise RuntimeError("unreachable")


def _get_text(url: str) -> str:
    """GET a URL and read the whole body, retrying truncated reads too."""
    for attempt in range(RETRIES):
        try:
            with _open(url) as resp:
                return resp.read().decode("utf-8", "replace")
        except (http.client.HTTPException, ConnectionError, TimeoutError):
            if attempt == RETRIES - 1:
                raise
        _backoff(attempt)
    raise RuntimeError("unreachable")


def geo_group(acc: str) -> str:
    """GSE90496 -> GSE90nnn, GSE1234 -> GSEnnn."""
    return acc[:-3] + "nnn"


def _geo_samples_have_idat(acc: str) -> int:
    """Count .idat lines in GEO's per-sample records (stops at first hit)."""
    url = (
        "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?"
        f"acc={acc}&targ=gsm&form=text&view=brief"
    )
    for attempt in range(RETRIES):
        try:
            with _open(url) as resp:
                for raw in resp:
                    if b".idat" in raw.lower():
                        return 1
            return 0
        except (http.client.HTTPException, ConnectionError, TimeoutError):
            if attempt == RETRIES - 1:
                raise
        _backoff(attempt)
    raise RuntimeError("unreachable")


def check_geo(acc: str) -> Result:
    """Check a GEO series via filelist.txt, then sample records."""
    base = (
        f"https://ftp.ncbi.nlm.nih.gov/geo/series/{geo_group(acc)}/{acc}"
        "/suppl/"
    )
    err = ""
    try:
        text = _get_text(base + "filelist.txt")
        n = sum(1 for ln in text.splitlines() if ".idat" in ln.lower())
        if n:
            return "OK", n, "RAW.tar filelist (Grn+Red counted separately)"
        return "MISSING", 0, "RAW.tar has no .idat files"
    except urllib.error.HTTPError as exc:
        err = f"HTTP {exc.code} on filelist.txt"
    except TRANSIENT as exc:
        err = f"{type(exc).__name__} on filelist.txt"

    # filelist.txt unavailable: ask GEO's sample records instead.
    try:
        if _geo_samples_have_idat(acc):
            return "OK", None, "IDAT file names in GEO sample records"
        # No IDAT anywhere in sample records. Without RAW.tar listing we
        # can still be sure there is nothing to download.
        return "MISSING", 0, "no .idat in GEO sample records"
    except TRANSIENT as exc:
        err += f"; sample records: {type(exc).__name__}"

    try:
        with _open(base + f"{acc}_RAW.tar", method="HEAD") as resp:
            size = int(resp.headers.get("Content-Length", 0))
        return "UNKNOWN", None, f"RAW.tar exists ({size / 1e6:.0f} MB); {err}"
    except urllib.error.HTTPError as exc:
        return "UNKNOWN", None, f"{err}; HTTP {exc.code} on RAW.tar"
    except TRANSIENT as exc:
        return "UNKNOWN", None, f"{err}; {type(exc).__name__} on RAW.tar"


def check_ae(acc: str) -> Result:
    """Count .idat entries in the BioStudies file listing."""
    n = total = offset = 0
    limit = 100
    while True:
        url = (
            f"https://www.ebi.ac.uk/biostudies/api/v1/studies/{acc}/files"
            f"?limit={limit}&offset={offset}"
        )
        data = json.loads(_get_text(url))
        items = data.get("items", []) if isinstance(data, dict) else []
        total += len(items)
        n += sum(
            1
            for it in items
            if str(it.get("path", "")).lower().endswith(".idat")
        )
        offset += len(items)
        if len(items) < limit:
            break
    if n:
        return "OK", n, f"{total} files listed"
    return "MISSING", 0, f"{total} files listed, none .idat"


def check_gdc(project: str) -> Result:
    """Count IDAT files of a GDC project."""
    filters = {
        "op": "and",
        "content": [
            {
                "op": "=",
                "content": {
                    "field": "cases.project.project_id",
                    "value": project,
                },
            },
            {
                "op": "=",
                "content": {"field": "data_format", "value": "IDAT"},
            },
        ],
    }
    url = "https://api.gdc.cancer.gov/files?size=0&filters=" + (
        urllib.parse.quote(json.dumps(filters))
    )
    total = json.loads(_get_text(url))["data"]["pagination"]["total"]
    if total:
        return "OK", total, "GDC IDAT files"
    return "UNKNOWN", 0, "not a GDC project with IDATs (custom cohort?)"


def check(dataset_id: str) -> tuple[str, str, int | None, str]:
    """Dispatch to the right source for one dataset id."""
    try:
        if dataset_id.startswith("GSE"):
            res = check_geo(dataset_id)
        elif dataset_id.startswith("E-MTAB"):
            res = check_ae(dataset_id)
        else:
            res = check_gdc(dataset_id)
    except Exception as exc:  # noqa: BLE001
        res = ("UNKNOWN", None, f"{type(exc).__name__}: {exc}")
    return (dataset_id, *res)


def _read_report(path: Path) -> dict[str, tuple[str, str, str]]:
    rows = {}
    with path.open(encoding="utf-8") as fh:
        next(fh)  # header
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 4:  # noqa: PLR2004
                rows[parts[0]] = (parts[1], parts[2], parts[3])
    return rows


def main() -> None:
    """Run the checks and write the report."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("datasets", nargs="*", help="ids (default: all configs)")
    ap.add_argument("--configs", type=Path, default=CONFIGS)
    ap.add_argument("--out", type=Path, default=Path("idat_report.tsv"))
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument(
        "--recheck",
        action="store_true",
        help="only re-query UNKNOWN rows of the existing --out report",
    )
    args = ap.parse_args()

    old: dict[str, tuple[str, str, str]] = {}
    if args.recheck:
        old = _read_report(args.out)
        ids = sorted(d for d, r in old.items() if r[0] == "UNKNOWN")
    else:
        ids = args.datasets or sorted(
            p.stem for p in args.configs.glob("*.py")
        )
    print(f"Checking {len(ids)} datasets ...", file=sys.stderr)

    new: dict[str, tuple[str, str, str]] = {}
    with ThreadPoolExecutor(args.workers) as ex:
        for i, (d, v, n, note) in enumerate(ex.map(check, ids), 1):
            new[d] = (v, "" if n is None else str(n), note)
            print(f"[{i}/{len(ids)}] {d}: {v} {note}", file=sys.stderr)

    rows = {**old, **new}
    with args.out.open("w", encoding="utf-8") as fh:
        fh.write("dataset_id\tverdict\tn_idat\tnote\n")
        for d in sorted(rows):
            fh.write("\t".join((d, *rows[d])) + "\n")

    for verdict in ("MISSING", "UNKNOWN"):
        sel = [(d, r[2]) for d, r in sorted(rows.items()) if r[0] == verdict]
        print(f"\n== {verdict} ({len(sel)}) ==")
        for d, note in sel:
            print(f"{d}\t{note}")
    print(f"\nFull report: {args.out}")


if __name__ == "__main__":
    main()
