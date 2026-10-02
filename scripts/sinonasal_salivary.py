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
from methylmeta.fetch import check_datasets, download_missing
from methylmeta.paths import CONFIGS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


ALL_DATASETS = sorted(
    path.stem
    for path in CONFIGS_DIR.glob("*.py")
    if path.name != "__init__.py"
)

TUMOR_TYPES = {
    # ------------------------------------------------------------------
    # Salivary gland tumours
    # ------------------------------------------------------------------
    "ADCC",
    "BCA",
    "BCAC",
    # "CXPA", #  NOTE:Does cluster according to subtypes
    "EPMYOC",
    "HCCC",
    "IDA",
    "KERACYS",
    "LYMPHAD",
    "MEC",
    "MSA",
    "PLEO_AD",
    "PLEO_AD_MYO",
    "PMA",
    "SBL",
    "SDC",
    "SDA",
    "SEA",
    "SEAD",
    "SG_ACICC",
    "SG_CAN_AD",
    "SG_CRIB_CA",
    "SG_CSARC",
    "SG_CYSTAD",
    "SG_DUCT_PAP",
    "SG_IDCA",
    "SG_MIX",
    "SG_MUC_ADCA",
    "SG_MYO",
    "SG_MYOEP_5P5Q",
    "SG_MYOEP_CA",
    "SG_ONC",
    "SG_SCC",
    "SG_SECR_CA",
    "SIALOLIPO",
    "SMA",
    "SSP",
    "SSPA",
    "WARTH",
    # ------------------------------------------------------------------
    # Sinonasal / nasal cavity tumours
    # ------------------------------------------------------------------
    "BSNS",
    "HAIRP",
    "HMSC",
    "ITAC",
    "NCMH",
    "NITAC",
    "NPPA_LG",
    "ONB",
    "ONB_A",
    "ONB_B",
    "REAH",
    "SGAT",
    "SMH",
    # "SNUC", # NOTE: Clusters on subtypes
    "SN_ADCA",
    "SN_ANGFIB",
    "SN_BCAT",
    "SN_GPC",
    "SN_NEC_IDH2",
    "SN_NEC_SMARCA4",
    "SN_PAP_EXO",
    "SN_PAP_INV",
    "SN_PAP_ONC",
    "SN_SCC",
    "SN_SMARCB1",
    "TCS",
    # ------------------------------------------------------------------
    # Oral cavity / mouth / jaw / odontogenic
    # ------------------------------------------------------------------
    "AMBL",
    "AMBL_AD",
    "AMBL_CA",
    "AMBL_CONV",
    "AMBL_META",
    "AMBL_PERIPH",
    "AMBL_UNICYST",
    "AMELOFIB",
    "AOT",
    "CARC_CUNIC",
    "CCOC",
    "CEOT",
    "COD",
    "COD_COF",
    "COF",
    "DGCT",
    "EMCMT",
    "FGC",
    "GCOC",
    "JPOF",
    "JTOF",
    "MNTI",
    "ODFIB",
    "ODSARC",
    "ODT",
    "OMY",
    "OPHP",
    "OPMD",
    # "ORAL_SCC_VERR",
    "OR_DYS",
    "OR_DYS_HPVA",
    "PIOC",
    "POT",
    "RANULA",
    "SOC",
    "SOD",
    "SOT",
    "SPAP",
    # ------------------------------------------------------------------
    # Head-and-neck carcinoma / SCC / neuroendocrine
    # ------------------------------------------------------------------
    "HNSCC",
    "HNSCC_DEK_AFF2",
    "HNSCC_EBVP",
    "HNSCC_HPVA",
    "HNSCC_HPVI",
    "HN_NET",
    "NUT",
    "HN_PGG",
    "PGG",
    "NP_CA",
    # ------------------------------------------------------------------
    # Head/neck-relevant haematolymphoid tumours
    # ------------------------------------------------------------------
    "AITL",
    "ALCL",
    "ALCL_ALK_NEG",
    "ALCL_ALK_POS",
    "BURK",
    "BURK_EBVN",
    "BURK_EBVP",
    "CLL",
    "DLBCL",
    "DLBCL_ABC",
    "DLBCL_EBV_POS",
    "DLBCL_GCB",
    "DLBCL_MYC_BCL2",
    "EBV_NK_TCL",
    "ENKTL",
    "ENMZL_MALT",
    "FDCS",
    "FL",
    "FL_HG",
    "FL_LG",
    "FTHCL",
    "FTHCL_FOLL",
    "FTHCL_NOS",
    "HGBCL",
    "HISTSARC",
    "LCH",
    "LPL",
    "MCL",
    "MCL_BLAST",
    "MCL_SOX11P",
    "MYELOMA",
    "MZL",
    "MZL_LN",
    "NLPHL",
    "NMZL",
    "PBL",
    "PLASMACYT",
    "PLASMACYT_CELL",
    "PTCL",
    "SEBV_TCL",
    "THRLBCL",
    "T_ALL",
    # ------------------------------------------------------------------
    # Mucosal melanoma
    # ------------------------------------------------------------------
    "MUC_MEL",
    # ------------------------------------------------------------------
    # Other head/neck soft tissue, bone, neural, endocrine
    # (borderline; keep only if in scope)
    # ------------------------------------------------------------------
    "CHORD",
    "CHORD_DD",
    "EWS",
    "GRAN_CELL",
    "KAPOSI_SARC",
    "LPS",
    "MPNST",
    "NFIB",
    "RMM",
    "RMS",
    "RMS_ALV",
    "RMS_EMB",
    "RMS_FUSION",
    "RMS_MYOD1",
    "RMS_PLEO",
    "RMS_TFCP2",
    "RMS_VGLL3",
    "RMS_ZFP64",
    "SCHW",
    "SFT",
    "SYNSARC",
    # "UPS",
    # ------------------------------------------------------------------
    # Controls / normal / reactive / technical
    # Relevant to FNA of mouth, nose, sinonasal, salivary gland
    # ------------------------------------------------------------------
    "CTRL_ADIPOSE",
    "CTRL_BLOOD",
    "CTRL_BONE",
    "CTRL_DENT_FOL",
    "CTRL_DNA_DEG",
    "CTRL_HN",
    "CTRL_INFLAM",
    "CTRL_LYMPH",
    "CTRL_MARROW",
    "CTRL_MUSCLE",
    "CTRL_NOS",
    "CTRL_REACT",
    "CTRL_SG",
    "CTRL_SKM",
    "CTRL_SN",
    "CTRL_SOFT",
    # ------------------------------------------------------------------
    # Metastasis
    # ------------------------------------------------------------------
    # Skin
    "SKIN_SCC",
    "SKIN_MEL",
    "MEL_DESMO",
    "MEL",
    "ACR_MEL",
    "MCC",
    # Thyr
    "THYR_PTC",
    "THYR_FTC",
    # Lung
    "LU_ADCA",
    "LU_SCC",
    "NSCLC",
    "SCLC",
    # Ren
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
    # Breast
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
    # Col
    "CR_CA",
    # Other
    "PROST_ADCA",
    "URO_CA",
    "PAN_CA",
    "CCA",
    "GAST_CA",
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
        "BURK_EBVN",
        "BURK_EBVP",
        "CLL",
        "ENMZL_MALT",
        "FL",
        "FL_HG",
        "FL_LG",
        "HGBCL",
        "LPL",
        "MCL",
        "MCL_BLAST",
        "MCL_SOX11P",
        "MZL",
        "MZL_LN",
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
        "ITAC",
        "NITAC",
    ],
    "PLASMA_CELL": ["PLASMACYT", "PLASMACYT_CELL", "MYELOMA"],
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
    "PLEO_AD_MYO": ["PLEO_AD", "PLEO_AD_MYO"],
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
    "PGG": [
        "HN_PGG",
        "PGG",
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
    missing_configs = merger.missing_configs(ALL_DATASETS)
    if missing_configs:
        raise SystemExit(
            "No config yet for: "
            f"{missing_configs}\n"
            "Write configs/datasets/<id>.py for these first "
            "(see `methylmeta agent` or `methylmeta profile`)."
        )

    # 2. Check what's already on disk, fetch what's missing.
    statuses = check_datasets(
        ALL_DATASETS, DATASET_DIR, check_idat=DOWNLOAD_IDAT
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
    df = merger.merge(dataset_ids=ALL_DATASETS)
    df = df.filter(pl.col("methylation_class").is_in(TUMOR_TYPES))
    merge_lookup = {
        tumor_type: group
        for group, tumor_types in MERGE_MAP.items()
        for tumor_type in tumor_types
    }
    df = df.with_columns(
        pl.col("methylation_class")
        .replace(merge_lookup)
        .alias("methylation_class")
    )
    for key, count in Counter(df["methylation_class"]).most_common():
        print(f"{key}: {count}")

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
