"""Fetch, harmonize, and merge a chosen set of datasets into one table.

Edit WANTED_DATASETS (and the paths below) and run:

    python scripts/example.py
"""

from __future__ import annotations

import logging
from pathlib import Path

import polars as pl

from methylmeta import MetadataMerger
from methylmeta.fetch import check_datasets, download_missing
from methylmeta.paths import CONFIGS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Edit this ---------------------------------------------------------

WANTED_DATASETS = [
    "E-MTAB-10576",
    "E-MTAB-10577",
    "E-MTAB-10578",
    "E-MTAB-15178",
    "E-MTAB-2926",
    "E-MTAB-7468",
    "E-MTAB-7478",
    "GSE124052",
    "GSE124617",
    "GSE125399",
    "GSE135672",
    "GSE136704",
    "GSE156546",
    "GSE171994",
    "GSE178216",
    "GSE178218",
    "GSE178219",
    "GSE178416",
    "GSE196228",
    "GSE197094",
    "GSE197675",
    "GSE204943",
    "GSE205331",
    "GSE211634",
    "GSE212937",
    "GSE214948",
    "GSE217337",
    "GSE218549",
    "GSE221745",
    "GSE222042",
    "GSE234379",
    "GSE237299",
    "GSE239695",
    "GSE239715",
    "GSE240130",
    "GSE243075",
    "GSE272656",
    "GSE277841",
    "GSE278138",
    "GSE279837",
    "GSE286412",
    "GSE293967",
    "GSE306846",
    "GSE308314",
    "GSE308436",
    "GSE308517",
    "GSE315367",
    "GSE49031",
    "GSE73549",
    "GSE79556",
    "GSE94769",
    "GSE95036",
    "Jurmeister_HN_tumors",
]

ACRONYM_TRANSLATOR = {
    # Chordoma
    "CHORD": "CHD",
    "CHORD_DD": "CHD_D",
    # Controls
    "CTRL_HN": "CHEADNECK",
    "CTRL_SG": "CSALIVARY",
    "CTRL_LYMPH": "CLYMPH",
    "CTRL_SN": "CSINONASAL",
    "CTRL_THYM": "CTHYMUS",
    # Salivary gland
    "ADCC": "ADCCA",
    "EPMYOC": "EMC",
    "BCA": "SBCA",
    "HCCC": "HCCC",
    "IDA": "IDA",
    "KERACYS": "KC",
    "LYMPHAD": "LA",
    "MEC": "MEC",
    "PLEO_AD_MYO": "MYO_PA",
    "PLEO_AD": "MYO_PA",
    "PMA": "PAD",
    "SG_ACICC": "SACC",
    "BCAC": "SBCAD",
    "SBL": "SBL",
    "SG_MYOEP_5P5Q": "SBMC5P5Q",
    "SG_CAN_AD": "SCA",
    "SG_CRIB_CA": "SCADC",
    "SDA": "SDA",
    "SDC": "SDC",
    "SG_DUCT_PAP": "SDP",
    "SEA": "SEA",
    "SEAD": "SEAD",
    "SG_CYSTAD": "SGCA",
    "SG_SCC": "SGSCC",
    "SG_IDCA": "SIDC",
    "SIALOLIPO": "SL",
    "SMA": "SMA",
    "SG_MUC_ADCA": "SMAD",
    "MSA": "SMSAD",
    "SG_MYOEP_CA": "SMYOC",
    "SG_ONC": "SONCO",
    "SSC": "SG_SECR_CA",
    "SSP": "SSP",
    "SSPA": "SSPA",
    "TCS": "TCS",
    "WARTH": "WARTH",
    # Sinonasal
    "BSNS": "BSNS",
    "SN_GPC": "GPC",
    "HMSC": "HMSC",
    "SN_NEC_IDH2": "NECIDH2",
    "SN_ADCA": "SNAD",
    "SN_ANGFIB": "SNAF",
    "SMARCB1": "SNC_SMARCB1",
    "SN_PAP_EXO": "SNEP",
    "SN_PAP_INV": "SNIP",
    "SN_NEC_SMARCA4": "SNNEC_SMARCA4",
    "SN_PAP_ONC": "SNOP",
    # Varia"
    "BR_CA": "BC",
    "BURK": "BL",
    "HISTSARC": "HS",
    "CPH_ADM": "ACPH",
    "LU_SCC": "LSCC",
}

DATASET_DIR = Path("~/methylmeta/data").expanduser()
OUTPUT = Path(
    "~/methylmeta/merged_metadata_sinonasal_salivary.tsv"
).expanduser()

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
    df = df.with_columns(
        pl.col("methylation_class").replace(ACRONYM_TRANSLATOR)
    )
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
