"""All GCTB (giant cell tumour of bone) samples.

Usage:
    python scripts/gctb.py
"""

from __future__ import annotations

from pathlib import Path

import polars as pl

from methylmeta import MetadataMerger
from methylmeta.catalog import find_datasets, load_catalog
from methylmeta.fetch import check_datasets, download_missing
from methylmeta.paths import CONFIGS_DIR

DATASET_DIR = Path("~/methylmeta/data").expanduser()
OUTPUT = Path("~/methylmeta/gctb_metadata.tsv").expanduser()


def main() -> None:
    catalog = load_catalog(CONFIGS_DIR)
    datasets = sorted(
        {m.entry.dataset_id for m in find_datasets(catalog, {"GCTB"})}
    )
    print(f"Datasets with GCTB: {datasets}")

    incomplete = [
        s for s in check_datasets(datasets, DATASET_DIR) if not s.is_complete
    ]
    if incomplete:
        download_missing(incomplete, DATASET_DIR)

    merger = MetadataMerger(config_dir=CONFIGS_DIR, dataset_dir=DATASET_DIR)
    df = merger.merge(dataset_ids=datasets)
    df = df.filter(pl.col("methylation_class") == "GCTB")

    df.write_csv(OUTPUT, separator="\t")
    print(f"Wrote {len(df)} samples -> {OUTPUT}")


if __name__ == "__main__":
    main()
