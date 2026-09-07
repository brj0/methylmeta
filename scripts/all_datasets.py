"""Fetch, harmonize, and merge all available datasets into one table.

Edit WANTED_DATASETS (and the paths below) and run:

    python scripts/example.py
"""

from __future__ import annotations

import logging
from pathlib import Path

from methylmeta import MetadataMerger
from methylmeta.fetch import check_datasets, download_missing
from methylmeta.paths import CONFIGS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


WANTED_DATASETS = sorted(
    path.stem
    for path in CONFIGS_DIR.glob("*.py")
    if path.name != "__init__.py"
)

DATASET_DIR = Path("~/methylmeta/data").expanduser()
OUTPUT = Path("~/methylmeta/merged_metadata_all.tsv").expanduser()

DOWNLOAD_MISSING = True  # set False to only report what's missing
DOWNLOAD_IDAT = False  # idats are large - opt in explicitly
COMPUTE_ARRAY_TYPES = False  # requires idats on disk; slow on large merges

# -------------------------------------------------------------------


def main() -> None:
    merger = MetadataMerger(config_dir=CONFIGS_DIR, dataset_dir=DATASET_DIR)

    # 1. Every wanted dataset needs a harmonizer config before it can be
    # merged - fail fast and say which ones are missing, rather than
    # discovering it mid-merge.
    missing_configs = merger.missing_configs(WANTED_DATASETS)
    if missing_configs:
        raise SystemExit(
            "No config yet for: "
            f"{missing_configs}\n"
            "Write configs/datasets/<id>.py for these first "
            "(see `methylmeta agent` or `methylmeta profile`)."
        )

    # 2. Check what's already on disk, fetch what's missing.
    statuses = check_datasets(
        WANTED_DATASETS, DATASET_DIR, check_idat=DOWNLOAD_IDAT
    )
    for status in statuses:
        logger.info(status)

    incomplete = [s for s in statuses if not s.is_complete]
    if incomplete:
        if DOWNLOAD_MISSING:
            download_missing(incomplete, DATASET_DIR)
        else:
            raise SystemExit(
                f"{len(incomplete)} dataset(s) missing data and "
                "DOWNLOAD_MISSING is False: "
                f"{[s.dataset_id for s in incomplete]}"
            )

    # 3. Harmonize and merge.
    df = merger.merge(dataset_ids=WANTED_DATASETS)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(OUTPUT, separator="\t")
    logger.info("Wrote %d samples -> %s", len(df), OUTPUT)

    # 4. Optional: fill in array_type from each sample's IDAT header.
    if COMPUTE_ARRAY_TYPES:
        df = merger.add_array_types(df)
        df.write_csv(OUTPUT, separator="\t")
        logger.info(
            "Wrote %d samples -> %s (with array_type)", len(df), OUTPUT
        )


if __name__ == "__main__":
    main()
