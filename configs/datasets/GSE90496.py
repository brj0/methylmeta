def _is_control(cls):
    return cls.startswith("CTRL_")


def dataset_id(row):
    return "GSE90496"


def description(row):
    return "CNS tumor DNA methylation reference set (Capper et al. 2018)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["methylation class"]


def methylation_class(row):
    mapping = {
        "GBM, RTK II": "GBM_RTK2",
        "GBM, RTK I": "GBM_RTK1",
        "GBM, RTK III": "GBM_RTK3",
        "GBM, MES": "GBM_MES",
        "GBM, MID": "GBM_MID",
        "GBM, MYCN": "GBM_MYCN",
        "GBM, G34": "DHG_G34",
        "MB, G3": "MB_G3",
        "MB, G4": "MB_G4",
        "MB, WNT": "MB_WNT",
        "MB, SHH INF": "MB_SHH_CHL_AD",
        "MB, SHH CHL AD": "MB_SHH_INF",
        "LGG, PA PF": "LGG_PA_PF",
        "LGG, PA MID": "LGG_PA_MID",
        "LGG, PA/GG ST": "LGG_PA_GG_ST",
        "LGG, GG": "LGG_GG",
        "LGG, DNT": "LGG_DNT",
        "LGG, DIG/DIA": "LGG_DIG_DIA",
        "LGG, RGNT": "LGG_RGNT",
        "LGG, MYB": "LGG_MYB",
        "LGG, SEGA": "LGG_SEGA",
        "A IDH": "ASTRO_IDH",
        "A IDH, HG": "ASTRO_IDH_HG",
        "O IDH": "OLIGO_IDH",
        "DMG, K27": "DMG_K27",
        "ANA PA": "ANA_PA",
        "PXA": "PXA",
        "EPN, PF A": "EPN_PF_A",
        "EPN, PF B": "EPN_PF_B",
        "EPN, RELA": "EPN_ST_ZFTA",
        "EPN, YAP": "EPN_ST_YAP1",
        "EPN, MPE": "EPN_MPE",
        "EPN, SPINE": "EPN_SPINE",
        "SUBEPN, PF": "SUBEPN_PF",
        "SUBEPN, ST": "SUBEPN_ST",
        "SUBEPN, SPINE": "SUBEPN_SPINE",
        "ATRT, SHH": "ATRT_SHH",
        "ATRT, TYR": "ATRT_TYR",
        "ATRT, MYC": "ATRT_MYC",
        "ETMR": "ETMR",
        "CNS NB, FOXR2": "CNS_NB_FOXR2",
        "HGNET, BCOR": "CNS_BCOR_ITD",
        "HGNET, MN1": "HGNET_MN1",
        "IHG": "IHG",
        "HMB": "HMB",
        "PITUI": "PITUICYTOMA",
        "PITAD, ACTH": "PIT_AD_ACTH",
        "PITAD, FSH LH": "PIT_AD_FSH_LH",
        "PITAD, PRL": "PIT_AD_PRL",
        "PITAD, STH SPA": "PIT_AD_STH_SPA",
        "PITAD, STH DNS A": "PIT_AD_STH_DGA",
        "PITAD, STH DNS B": "PIT_AD_STH_DGB",
        "PITAD, TSH": "PIT_AD_TSH",
        "CPH, ADM": "CPH_ADM",
        "CPH, PAP": "CPH_PAP",
        "PIN T,  PB A": "PINE_BL_A",
        "PIN T,  PB B": "PINE_BL_B",
        "PIN T, PPT": "PINE_PPT",
        "PTPR, A": "PTPR_A",
        "PTPR, B": "PTPR_B",
        "CHGL": "CHGL",
        "CN": "CNEUROCYT",
        "LIPN": "LIPN",
        "DLGNT": "DLGNT",
        "PLEX, AD": "PLEX_ADULT",
        "PLEX, PED A": "PLEX_PED_A",
        "PLEX, PED B": "PLEX_PED_B",
        "PGG, nC": "PGG_NC",
        "SCHW": "SCHW",
        "SCHW, MEL": "SCHW_MEL",
        "MNG": "MNG",
        "MELCYT": "MELCYT",
        "MELAN": "MEL",
        "ENB, A": "ONB_A",
        "ENB, B": "ONB_B",
        "SFT HMPC": "SFT_MAL",
        "EWS": "EWS",
        "EFT, CIC": "SARC_CIC",
        "RETB": "RB",
        "LYMPHO": "CNSL",
        "PLASMA": "PLASMACYT",
        "CHORDM": "CHORD",
        "CONTR, ADENOPIT": "CTRL_ADENOPIT",
        "CONTR, CEBM": "CTRL_CEBM",
        "CONTR, HEMI": "CTRL_HEMI",
        "CONTR, HYPTHAL": "CTRL_HYPTHAL",
        "CONTR, INFLAM": "CTRL_INFLAM",
        "CONTR, PINEAL": "CTRL_PINE",
        "CONTR, PONS": "CTRL_PONS",
        "CONTR, REACT": "CTRL_REACT",
        "CONTR, WM": "CTRL_WM",
    }
    return mapping[row["methylation class"]]


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    if _is_control(methylation_class(row)):
        return "control"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["material"]]
