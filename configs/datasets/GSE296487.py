def _is_control(cls):
    if cls is None:
        return False
    return cls.startswith("CTRL_")


def _is_metastatic(cls):
    return cls == "MEL"


def dataset_id(row):
    return "GSE296487"


def description(row):
    return (
        "Pediatric central nervous system tumor cohort classified by DNA "
        "methylation profiling (DKFZ classifier)"
    )


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    code = row["Title"].split("_", 2)[2]
    mapping = {
        "DMG_EGFR": "DMG_EGFR",
        "DMG_K27": "DMG_K27",
        "HGG_E": "HGG_E",
        "pedHGG_MYCN": "HGG_PED_MYCN",
        "GBM_MES_TYP": "GBM_MES",
        # pilocytic astrocytoma by location
        "PA_INF": "LGG_PA_PF",
        "PA_INF_FGFR": "LGG_PA_PF",
        "PA_MID": "LGG_PA_MID",
        "PA_CORT": "LGG_PA_GG_ST",
        "GG": "LGG_GG",
        "DIG_DIA": "LGG_DIG_DIA",
        "DNET": "LGG_DNT",
        "RGNT": "LGG_RGNT",
        "SEGA": "LGG_SEGA",
        "LGG_MYB_B": "LGG_MYB",
        "LGG_MYB_D": "LGG_MYB",
        "AG_MYB": "LGG_MYB",
        "GNT_A": "LGG",
        # ependymoma
        "EPN_PFA_1A": "EPN_PF_A",
        "EPN_PFA_1B": "EPN_PF_A",
        "EPN_PFA_1C": "EPN_PF_A",
        "EPN_PFA_1D": "EPN_PF_A",
        "EPN_PFA_1F": "EPN_PF_A",
        "EPN_PFA_2A": "EPN_PF_A",
        "EPN_PFA_2B": "EPN_PF_A",
        "EPN_PFB_4": "EPN_PF_B",
        "EPN_SPINE_SE_A": "EPN_SPINE",
        "EPN_YAP": "EPN_ST_YAP1",
        "EPN_ST_ZFTA_RELA_A": "EPN_ST_ZFTA",
        # medulloblastoma
        "MB_WNT": "MB_WNT",
        "MB_SHH_1": "MB_SHH",
        "MB_SHH_2": "MB_SHH",
        "MB_SHH_3": "MB_SHH",
        "MB_SHH_4": "MB_SHH",
        "MB_G34_I": "MB",
        "MB_G34_II": "MB",
        "MB_G34_III": "MB",
        "MB_G34_IV": "MB",
        "MB_G34_V": "MB",
        "MB_G34_VII": "MB",
        "MB_G34_VIII": "MB",
        # embryonal and other pediatric tumors
        "ATRT_MYC": "ATRT_MYC",
        "ATRT_SHH": "ATRT_SHH",
        "ATRT_TYR": "ATRT_TYR",
        "CNS_NB_FOXR2": "CNS_NB_FOXR2",
        "PB_FOXR2": "CNS_NB_FOXR2",
        "PB_GRP1A": "PINE_BL",
        "PB_GRP2": "PINE_BL",
        "ET_PLAG": "CNS_EMB_NEC",
        "NET_PLAGL1_FUS": "PLAGL1_NEUEPT",
        "DGONC": "DGONC",
        "MPNST_ATYP": "MPNST",
        # choroid plexus, craniopharyngioma, meningioma
        "CPC_PED": "PLEX_CA_PED",
        "CPP_PED": "PLEX_PED_A",
        "CPH_ADM": "CPH_ADM",
        "CPH_PAP": "CPH_PAP",
        "MNG_BEN_1": "MNG_BEN_1",
        "MNG_BEN_3": "MNG_BEN_3",
        "SCHW": "SCHW",
        "PXA": "PXA",
        "LCH": "LCH",
        # germ cell tumors
        "GCT_TERA": "TER",
        "GCT_GERM_A": "CNS_GERMI",
        "GCT_GERM_KIT": "CNS_GERMI",
        "GCT_YOLKSAC": "YST",
        # non-CNS metastasis
        "MET_MEL": "MEL",
        # control tissue
        "CTRL_HEMI": "CTRL_HEMI",
        "CTRL_CBM": "CTRL_CEBM",
        "CTRL_CORPCAL": "CTRL_WM",
        "CTRL_REACTIVE": "CTRL_REACT",
        "INFLAM_ENV": "CTRL_INFLAM",
    }
    return mapping[code]


def diagnosis(row):
    cls = methylation_class(row)
    if _is_control(cls):
        return "Normal or reactive central nervous system tissue"
    if _is_metastatic(cls):
        return "Metastatic melanoma"
    return "Central nervous system tumor"


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    if _is_metastatic(methylation_class(row)):
        return "Skin"
    return "Central nervous system"


def sample_type(row):
    cls = methylation_class(row)
    if _is_control(cls):
        return "control"
    if _is_metastatic(cls):
        return "metastasis"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
