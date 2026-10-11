"""Metadata for sinonasal and salivary gland tumors.

Usage:
    python scripts/sinonasal_salivary.py
"""

from __future__ import annotations

import logging
from collections import Counter
from pathlib import Path

import polars as pl

from methylmeta import MetadataMerger
from methylmeta.catalog import find_datasets, load_catalog
from methylmeta.fetch import check_datasets, download_missing
from methylmeta.paths import CONFIGS_DIR
from methylmeta.vocab import all_tumor_types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


TARGET_CLASSES = {
    # ------------------------------------------------------------------
    # Salivary gland tumours
    # ------------------------------------------------------------------
    "ACICC",
    "ADCC",
    "MEC",
    "PLEO_AD",
    "PLEO_MYO",
    "SDC",
    "SG_BC_AD",
    "SG_BC_ADCA",
    "SG_BL",
    "SG_CANL_AD",
    "SG_CRIB_ADCA",
    "SG_CSARC",
    "SG_CYSTAD",
    "SG_DUCT_PAP",
    "SG_EPIMYO_CA",
    "SG_HYAL_CCC",
    "SG_INTERC_AD",
    "SG_IDUCT_CA",
    "SG_KERATOC",
    "SG_LYMPH_AD",
    "SG_MIX_GRP",
    "SG_MSECR_ADCA",
    "SG_MUC_ADCA",
    "SG_MYOEP",
    "SG_MYOEP_5P5Q",
    "SG_MYOEP_CA",
    "SG_ONC",
    "SG_POLYM_ADCA",
    "SG_SCC",
    "SG_SCLMIC_ADCA",
    "SG_SCLP_AD",
    "SG_SEB_AD",
    "SG_SEB_ADCA",
    "SG_SECR_CA",
    "SG_SIALO_LIPO",
    "SG_SIAL_PAP",
    "SG_STR_AD",
    "WARTH",
    "CTRL_ADIPOSE",
    "CTRL_BLOOD",
    "CTRL_BONE",
    "CTRL_DNA_DEG",
    "CTRL_HN",
    "CTRL_INFLAM",
    "CTRL_LYMPH",
    "CTRL_MUSCLE",
    "CTRL_NOS",
    "CTRL_REACT",
    "CTRL_SG",
    "CTRL_SKM",
    "CTRL_SN",
    "CTRL_SOFT",
}

MERGE_MAP = {
    "DLBCL": [
        "DLBCL",
        "DLBCL_ABC",
        "DLBCL_EBV_POS",
        "DLBCL_GCB",
        "DLBCL_MYC_BCL2",
    ],
    "LYMPHOMA_B_OTH": [
        "BURK",
        "BURK_EBV_NEG",
        "BURK_EBV_POS",
        "CLL",
        "MALT",
        "FL",
        "FL_HG",
        "FL_LG",
        "HGBCL",
        "LPL",
        "MCL",
        "MCL_BLAST",
        "MCL_SOX11_POS",
        "MZL",
        "NLPHL",
        "NMZL",
        "PBL",
        "THRLBCL",
    ],
    "LYMPHOMA_TNK": [
        "AITL",
        "ALCL",
        "ALCL_ALK_NEG",
        "ALCL_ALK_POS",
        "PTCL",
        "FTHCL",
        "FTHCL_FOLL",
        "FTHCL_NOS",
        "EBV_NK_TCL",
        "SEBV_TCL",
        "T_ALL",
    ],
    "SN_ADCA": [
        "SN_ADCA",
        "SN_ADCA_INT",
        "SN_ADCA_NONINT",
    ],
    "PLASMA_CELL": ["PLASMACYT", "PCN", "MYELOMA"],
    "HISTIOCYTIC": ["LCH", "FDCS", "HISTSARC"],
    "CTRL_OTH": [
        "CTRL_ADIPOSE",
        "CTRL_BONE",
        "CTRL_DENT_FOL",
        "CTRL_DNA_DEG",
        "CTRL_HN",
        "CTRL_INFLAM",
        "CTRL_MARROW",
        "CTRL_MUSCLE",
        "CTRL_NOS",
        "CTRL_REACT",
        "CTRL_SKM",
        "CTRL_SOFT",
    ],
    "AMBL": [
        "AMBL_AD",
        "AMBL_CA",
        "AMBL_CONV",
        "AMBL_META",
        "AMBL_PERIPH",
        "AMBL_UNICYST",
    ],
    "RMS": [
        "RMS",
        "RMS_ALV",
        "RMS_EMB",
        "RMS_FUSION",
        "RMS_MYOD1",
        "RMS_PLEO",
        "RMS_TFCP2",
        "RMS_VGLL3",
        "RMS_ZFP64",
    ],
    "OR_DYS": ["OR_DYS", "OR_DYS_HPVA"],
    "PLEO_MYO": ["PLEO_AD", "PLEO_MYO"],
    "THYR_CA": ["THYR_PTC", "THYR_FTC"],
    "NSCLC": [
        "LU_ADCA",
        "LU_SCC",
        "NSCLC",
    ],
    "MEL_MET": [
        "ACR_MEL",
        "MEL",
        "MEL_DESMO",
        "SKIN_MEL",
    ],
    "RCC": [
        "RCC",
        "RCC_ACD",
        "RCC_ALK",
        "RCC_CC",
        "RCC_CCP",
        "RCC_CD",
        "RCC_CP",
        "RCC_ELOC",
        "RCC_ESC",
        "RCC_FH",
        "RCC_MCN",
        "RCC_MTSC",
        "RCC_PAP",
        "RCC_RP",
        "RCC_SDH",
        "RCC_SMARCB1",
        "RCC_TFE3",
        "RCC_TFEB",
        "RCC_TR",
        "RCC_TUBULOCYST",
    ],
    "PGL": [
        "HN_PGL",
        "PGL",
    ],
    "BR_CA": [
        "BR_CA",
        "BR_CA_APOCRINE",
        "BR_CA_CRIB",
        "BR_CA_HER2",
        "BR_CA_HRP",
        "BR_CA_INV_PAP",
        "BR_CA_LOB",
        "BR_CA_MALE",
        "BR_CA_META",
        "BR_CA_MICROINV",
        "BR_CA_MICROPAP",
        "BR_CA_MUC",
        "BR_CA_NST",
        "BR_CA_TALL",
        "BR_CA_TN",
        "BR_CA_TUB",
        "BR_CYSTADCA",
        "BR_ENC_PAP_CA",
        "BR_SOL_PAP_CA",
    ],
    "ONB": [
        "ONB",
        "ONB_A",
        "ONB_B",
    ],
}

DATASET_DIR = Path("~/methylmeta/data").expanduser()
OUTPUT = Path(
    "~/methylmeta/merged_metadata_salivary_glands.tsv"
).expanduser()

DOWNLOAD_MISSING = True  # set False to only report what's missing
DOWNLOAD_IDAT = False  # idats are large - opt in explicitly
COMPUTE_ARRAY_TYPES = True  # requires idats on disk; slow on large merges
ADD_IDAT_PATHS = True  # idat_path column; null if no IDAT on disk
DROP_INVALID = True  # drop rows w/o IDAT or array_type invalid_array
ADD_PURITIES = True  # RFpurify; requires idats on disk, slow, cached

# -------------------------------------------------------------------


def select_datasets() -> list[str]:
    """Datasets whose config can produce any of TARGET_CLASSES.

    Reads the configs statically (no metadata needed), so only the relevant
    datasets are fetched instead of the whole catalog. Datasets without raw
    IDATs are dropped up front.
    """
    catalog = load_catalog(CONFIGS_DIR)
    matches = find_datasets(catalog, TARGET_CLASSES)
    selected = {m.entry.dataset_id for m in matches}

    # Configs whose classes are computed dynamically (e.g. `return
    # row["class"]`) can't be analysed statically. Keep them rather than
    # silently dropping them; the class filter after merging removes
    # irrelevant rows anyway.
    undetectable = {
        dataset_id
        for dataset_id, entry in catalog.items()
        if not entry.classes
    }
    if undetectable:
        logger.warning(
            "Keeping %d dataset(s) with no statically detectable classes: %s",
            len(undetectable),
            sorted(undetectable),
        )
    selected |= undetectable

    logger.info(
        "Selected %d of %d datasets containing the requested classes",
        len(selected),
        len(catalog),
    )
    return sorted(selected)


def main() -> None:
    merger = MetadataMerger(config_dir=CONFIGS_DIR, dataset_dir=DATASET_DIR)
    datasets = select_datasets()

    # 1. Every wanted dataset needs a harmonizer config before it can be
    # merged - fail fast and say which ones are missing, rather than
    # discovering it mid-merge.
    missing_configs = merger.missing_configs(datasets)
    if missing_configs:
        raise SystemExit(
            "No config yet for: "
            f"{missing_configs}\n"
            "Write configs/datasets/<id>.py for these first "
            "(see `methylmeta agent` or `methylmeta profile`)."
        )

    # 2. Check what's already on disk, fetch what's missing.
    statuses = check_datasets(datasets, DATASET_DIR, check_idat=DOWNLOAD_IDAT)
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
    df = merger.merge(dataset_ids=datasets)
    df = df.filter(pl.col("methylation_class").is_in(TARGET_CLASSES))

    # Exclude cell lines
    df = df.filter(pl.col("material_type").ne_missing("cell_line"))

    # Add full name
    full_name_map = {tum.acronym: tum.name for tum in all_tumor_types()}
    df = df.with_columns(
        pl.col("methylation_class")
        .replace(full_name_map)
        .alias("methylation_class_name")
    )

    for key, count in Counter(df["methylation_class"]).most_common():
        print(f"{key}: {count}")

    print("\nUsed datasets:")
    for dset in sorted(df["dataset_id"].unique()):
        print(f"{dset}")

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

    # 5. Optional: IDAT paths, drop unusable rows, purities. Runs on the
    # class-filtered table, so purity is only computed for selected samples.
    if ADD_IDAT_PATHS or DROP_INVALID or ADD_PURITIES:
        df = merger.add_idat_paths(df)
        if DROP_INVALID:
            df = merger.drop_invalid(df)
        if ADD_PURITIES:
            df = merger.add_purities(df)
        df.write_csv(OUTPUT, separator="\t")
        logger.info("Wrote %d samples -> %s (with idat_path)", len(df), OUTPUT)


if __name__ == "__main__":
    main()
