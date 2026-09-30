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

WANTED_DATASETS = sorted(
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
    # "SNUC", # NOTE: Clusters in subtypes
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
    "DFB",
    "DGCT",
    "EMCMT",
    "FGC",
    "GCOC",
    "GCG",
    "JPOF",
    "JTOF",
    "MNTI",
    "ODCS",
    "ODFIB",
    "ODSARC",
    "ODT",
    "OMY",
    "OPHP",
    "OPMD",
    "ORAL_SCC_VERR",
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
    "HNSCC_EBV_POS",
    "HNSCC_HPVA",
    "HNSCC_HPVI",
    "HN_NET",
    "LEC",
    "NUT",
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
    "CPH_ADM",
    "DFSP",
    "EWS",
    "GRAN_CELL",
    "HNPGL",
    "KAPOSI_SARC",
    "LPS",
    "MCC",
    "MPNST",
    "NFIB",
    "PGG",
    "RMM",
    "RMS",
    "RMS_ALV",
    "RMS_EMB",
    "RMS_TFCP2",
    "SCHW",
    "SFT",
    "SYNSARC",
    "UPS",
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
}

ACRONYMS = {
    # ------------------------------------------------------------------
    # WHO Head and Neck Tumours + salivary / sinonasal / odontogenic
    # ------------------------------------------------------------------
    "ADCC",
    "AMBL",
    "AMBL_AD",
    "AMBL_CA",
    "AMBL_CONV",
    "AMBL_META",
    "AMBL_PERIPH",
    "AMBL_UNICYST",
    "AMELOFIB",
    "AOT",
    "BCA",
    "BCAC",
    "BSNS",
    "CARC_CUNIC",
    "CCOC",
    "CEOT",
    "CERA",
    "CERAC",
    "CHERUB",
    "COD",
    "COD_COF",
    "COF",
    "CXPA",
    "DFB",
    "DGCT",
    "EAC_OSTEO",
    "EAC_SCC",
    "EAR_ADCA",
    "EAR_SCC",
    "EMCMT",
    "EPMYOC",
    "FGC",
    "GCOC",
    "GCG",
    "HAIRP",
    "HCCC",
    "HMSC",
    "HNPGL",
    "HNSCC",
    "HNSCC_DEK_AFF2",
    "HNSCC_EBV_POS",
    "HNSCC_HPVA",
    "HNSCC_HPVI",
    "HN_NET",
    "HTAC",
    "IDA",
    "ITAC",
    "JPOF",
    "JTOF",
    "KERACYS",
    "LAR_ASC",
    "LAR_DYS",
    "LAR_SCC",
    "LAR_SCC_BAS",
    "LAR_SCC_CONV",
    "LAR_SCC_PAP",
    "LAR_SCC_SPIN",
    "LAR_SCC_VERR",
    "LAR_SQ_PAP",
    "LEC",
    "LYMPHAD",
    "MEC",
    "MNTI",
    "NCMH",
    "NITAC",
    "NP_CA",
    "NPPA_LG",
    "NUT",
    "ODCS",
    "ODFIB",
    "ODSARC",
    "ODT",
    "OMY",
    "ONB",
    "ONB_A",
    "ONB_B",
    "OPHP",
    "OPMD",
    "ORAL_SCC_VERR",
    "OR_DYS",
    "OR_DYS_HPVA",
    "OSMF",
    "PIOC",
    "PLEO_AD",
    "PLEO_AD_MYO",
    "PMA",
    "POT",
    "PVL",
    "RANULA",
    "REAH",
    "RMS_TFCP2",
    "SBC",
    "SBL",
    "SDC",
    "SDA",
    "SEA",
    "SEAD",
    "SGAT",
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
    "SMH",
    "SNUC",
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
    "SOC",
    "SOD",
    "SOT",
    "SPAP",
    "SSP",
    "SSPA",
    "TCS",
    "TGDC",
    "WARTH",
    # ------------------------------------------------------------------
    # Cross-cutting carcinoma / SCC / adenosquamous / etc.
    # ------------------------------------------------------------------
    "SCC",
    "ASC",
    "HNSCC",
    "HNSCC_HPVA",
    "HNSCC_HPVI",
    "HNSCC_EBV_POS",
    "HNSCC_DEK_AFF2",
    "LEC",
    "NUT",
    "MEC",
    "ADCC",
    "EPMYOC",
    "SDC",
    "BCAC",
    "CARC_CUNIC",
    "ORAL_SCC_VERR",
    "LAR_SCC",
    "LAR_SCC_BAS",
    "LAR_SCC_CONV",
    "LAR_SCC_PAP",
    "LAR_SCC_SPIN",
    "LAR_SCC_VERR",
    "SN_SCC",
    "SNUC",
    "SN_ADCA",
    "ITAC",
    "NITAC",
    "NP_CA",
    "NPPA_LG",
    "EAC_SCC",
    "EAR_SCC",
    "EAR_ADCA",
    "CCOC",
    "GCOC",
    "SOC",
    "PIOC",
    "AMBL_CA",
    "SOT",
    "CEOT",
    "DGCT",
    "ODCS",
    "ODSARC",
    "TCS",
    "HMSC",
    "BSNS",
    "SN_SMARCB1",
    "SN_NEC_IDH2",
    "SN_NEC_SMARCA4",
    "HN_NET",
    "HNPGL",
    # ------------------------------------------------------------------
    # Common lymphoma / hematolymphoid differentials in neck nodes
    # ------------------------------------------------------------------
    "LYMPHO",
    "DLBCL",
    "DLBCL_ABC",
    "DLBCL_GCB",
    "DLBCL_EBV_POS",
    "DLBCL_MYC_BCL2",
    "FL",
    "FL_HG",
    "FL_LG",
    "MZL",
    "MZL_LN",
    "ENMZL_MALT",
    "NMZL",
    "SMZL",
    "CLL",
    "CLL_IGHV_MUT",
    "CLL_IGHV_UNMUT",
    "MCL",
    "MCL_BLAST",
    "MCL_SOX11N",
    "MCL_SOX11P",
    "BURK",
    "BURK_EBVN",
    "BURK_EBVP",
    "HODG",
    "HODG_CL",
    "HODG_NS",
    "NLPHL",
    "ALCL",
    "ALCL_ALK_NEG",
    "ALCL_ALK_POS",
    "PTCL",
    "AITL",
    "FTHCL",
    "FTHCL_FOLL",
    "FTHCL_NOS",
    "ENKTL",
    "ITCL_NOS",
    "ITCL_GI",
    "MEITL",
    "SPTCL",
    "MYCOSIS_FUNG",
    "SEZARY",
    "LYP",
    "PCMZL",
    "PC_ALCL",
    "PC_CD30_PED",
    "PC_CD4_SMTCLD",
    "PC_CD8_AECTCL",
    "IVLBCL",
    "PEL",
    "PBL",
    "LPL",
    "SBLPN",
    "SDRPL",
    "THRLBCL",
    "PMBCL",
    "MGZL",
    "KSHV_DLBCL",
    "FA_LBCL",
    "FO_LBCL",
    "EBV_NK_TCL",
    "EBVTCL",
    "SEBV_TCL",
    "HTLV1_ATL",
    "ANKL",
    "NK_LGL",
    "TLGLL",
    "TPLL",
    # ------------------------------------------------------------------
    # Melanoma / skin / soft tissue / neuroendocrine / paraganglioma
    # ------------------------------------------------------------------
    "MEL",
    "SKIN_MEL",
    "MEL_CSD",
    "MEL_DESMO",
    "MEL_NOD",
    "MEL_SS",
    "MEL_SPITZ",
    "NEV_BNG",
    "NEV_JCD",
    "NEV_DYS",
    "NEV_SPITZ",
    "BCC",
    "SKIN_SCC",
    "SKIN_AK",
    "NEC",
    "SCNEC",
    "LCNEC",
    "NET",
    "PGG",
    "PHEO",
    "SARC_NOS",
    "SYNSARC",
    "UPS",
    "MPNST",
    "SCHW",
    "NFIB",
    "GRAN_CELL",
    "HEM",
    "LYMPHANG_SUP",
    "KAPOSI_SARC",
    "DFSP",
    "SFT",
    "LPS",
    "LMS",
    "RMM",
    "RMS",
    # ------------------------------------------------------------------
    # Thyroid / parathyroid neck-FNA differentials (optional)
    # ------------------------------------------------------------------
    "THYR_AD",
    "THYR_FOL_AD",
    "THYR_FAD_PAP",
    "THYR_ONC_AD",
    "THYR_CA",
    "THYR_PTC",
    "THYR_FTC",
    "THYR_HG_FCD_CA",
    "THYR_PDC",
    "THYR_ANA_CA",
    "THYR_MTC",
    "THYR_HTT",
    "NIFTP",
    "THYR_UTMP",
    "THYR_CMTC",
    "THYR_SECR_CA",
    "THYR_MEC",
    "THYR_SMECE",
    "THYR_MEDFOL_CA",
    "THYR_BL",
    "THYR_FND",
    "MTC",
    "PARA_AD",
    "PARA_ATYP",
    "PARA_CA",
    "PARA_HYP",
    "PARA_LIPOAD",
    # ------------------------------------------------------------------
    # Controls / normal / reactive / technical
    # ------------------------------------------------------------------
    "CTRL_ADENOPIT",
    "CTRL_ADIPOSE",
    "CTRL_ADREN",
    "CTRL_ANAL",
    "CTRL_APP",
    "CTRL_BD",
    "CTRL_BLA",
    "CTRL_BLOOD",
    "CTRL_BONE",
    "CTRL_BR",
    "CTRL_BRAIN",
    "CTRL_BRAIN_GBM",
    "CTRL_CEBM",
    "CTRL_CERV",
    "CTRL_COL",
    "CTRL_DENT_FOL",
    "CTRL_DNA_DEG",
    "CTRL_ENDOM",
    "CTRL_ESO",
    "CTRL_GAST",
    "CTRL_GREY",
    "CTRL_HEMI",
    "CTRL_HN",
    "CTRL_HYPTHAL",
    "CTRL_INFLAM",
    "CTRL_LIV",
    "CTRL_LU",
    "CTRL_LYMPH",
    "CTRL_MARROW",
    "CTRL_MELCYT",
    "CTRL_MUSCLE",
    "CTRL_MYOMETR",
    "CTRL_NERVE",
    "CTRL_NOS",
    "CTRL_OMENT",
    "CTRL_OVA",
    "CTRL_PAN",
    "CTRL_PERIT",
    "CTRL_PINE",
    "CTRL_PLEURA",
    "CTRL_PONS",
    "CTRL_PROST",
    "CTRL_REACT",
    "CTRL_REN",
    "CTRL_SG",
    "CTRL_SI",
    "CTRL_SKIN",
    "CTRL_SKM",
    "CTRL_SN",
    "CTRL_SOFT",
    "CTRL_SPINAL",
    "CTRL_TES",
    "CTRL_THYR",
    "CTRL_TUB",
    "CTRL_URO",
    "CTRL_WM",
    "BARRETT",
    "OLP",
    "OML",
    "SKIN_SEBK",
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
