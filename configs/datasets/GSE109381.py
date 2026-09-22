def dataset_id(row):
    return "GSE109381"


def description(row):
    return "DNA methylation-based classification of human central nervous system tumors, Capper 2018"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # The study labels each reference/validation sample with its tumor entity.
    return row["methylation class"]


def methylation_class(row):
    mapping = {
        # Glioblastoma, IDH-wildtype
        "GBM, RTK I": "GBM_RTK1",
        "GBM, RTK II": "GBM_RTK2",
        "GBM, RTK III": "GBM_RTK3",
        "GBM, MES": "GBM_MES",
        "GBM, MID": "GBM_MID",
        "GBM, MYCN": "GBM_MYCN",
        "GBM, G34": "DHG_G34",
        "GBM, PNC": "GBM_PNC",
        "GBM, LOW": "GBM_LOW",
        # Diffuse midline glioma
        "DMG, K27": "DMG_K27",
        # Adult-type diffuse gliomas, IDH-mutant
        "A IDH": "ASTRO_IDH",
        "A IDH, HG": "ASTRO_IDH_HG",
        "O IDH": "OLIGO_IDH",
        "O IDH, HG": "OLIGO_IDH_ANA",
        # Pediatric-type low-grade gliomas / glioneuronal tumors
        "LGG, PA PF": "LGG_PA_PF",
        "LGG, PA MID": "LGG_PA_MID",
        "LGG, PA/GG ST": "LGG_PA_GG_ST",
        "LGG, GG": "LGG_GG",
        "LGG, DNT": "LGG_DNT",
        "LGG, RGNT": "LGG_RGNT",
        "LGG, MYB": "LGG_MYB",
        "LGG, SEGA": "LGG_SEGA",
        "LGG, DIG/DIA": "LGG_DIG_DIA",
        "ANA PA": "ANA_PA",
        "DLGNT": "DLGNT",
        "LIPN": "LIPN",
        "CN": "CNEUROCYT",
        # Ependymal tumors
        "EPN, PF A": "EPN_PF_A",
        "EPN, PF B": "EPN_PF_B",
        "EPN, RELA": "EPN_ST_ZFTA",
        "EPN, YAP": "EPN_ST_YAP1",
        "EPN, SPINE": "EPN_SPINE",
        "EPN, MPE": "EPN_MPE",
        "SUBEPN, PF": "SUBEPN_PF",
        "SUBEPN, SPINE": "SUBEPN_SPINE",
        "SUBEPN, ST": "SUBEPN_ST",
        # Medulloblastoma
        "MB, WNT": "MB_WNT",
        "MB, SHH INF": "MB_SHH_INF",
        "MB, SHH CHL AD": "MB_SHH_CHL_AD",
        "MB, G3": "MB_G3",
        "MB, G4": "MB_G4",
        # Embryonal / high-grade embryonal tumors
        "ATRT, SHH": "ATRT_SHH",
        "ATRT, MYC": "ATRT_MYC",
        "ATRT, TYR": "ATRT_TYR",
        "ETMR": "ETMR",
        "CNS NB, FOXR2": "CNS_NB_FOXR2",
        "EFT, CIC": "EFT_CIC",
        "EWS": "EWS",
        "HGNET, BCOR": "CNS_BCOR_ITD",
        "HGNET, MN1": "HGNET_MN1",
        "IHG": "IHG",
        "RETB": "RB",
        # Sellar region tumors
        "CPH, ADM": "CPH_ADM",
        "CPH, PAP": "CPH_PAP",
        "PITAD, ACTH": "PIT_AD_ACTH",
        "PITAD, FSH LH": "PIT_AD_FSH_LH",
        "PITAD, PRL": "PIT_AD_PRL",
        "PITAD, TSH": "PIT_AD_TSH",
        "PITAD, STH SPA": "PIT_AD_STH_SPA",
        "PITAD, STH DNS A": "PIT_AD_STH_DGA",
        "PITAD, STH DNS B": "PIT_AD_STH_DGB",
        "PITUI": "PIT_SCO_GCT",
        "CONTR, ADENOPIT": "CTRL_ADENOPIT",
        # Pineal region tumors
        "PIN T,  PB A": "PINE_PB_A",
        "PIN T,  PB B": "PINE_PB_B",
        "PIN T, PB B": "PINE_PB_B",
        "PIN T, PPT": "PINE_PPT",
        "PIN_CYT": "PINE_CYT",
        "PTPR, A": "PTPR_A",
        "PTPR, B": "PTPR_B",
        # Choroid plexus tumors
        "PLEX, AD": "PLEX_ADULT",
        "PLEX, PED A": "PLEX_PED_A",
        "PLEX, PED B": "PLEX_PED_B",
        # Other CNS tumors
        "MNG": "MNG",
        "HMB": "HMB",
        "PXA": "PXA",
        "CHGL": "CHGL",
        "CHORDM": "CHORD",
        "PGG, nC": "PGG_NC",
        "ENB, A": "ONB_A",
        "ENB, B": "ONB_B",
        "LYMPHO": "CNS_LYMPHO",
        "PLASMA": "PLASMACYT",
        # Peripheral nerve sheath / mesenchymal / melanocytic tumors
        "SCHW": "SCHW",
        "SCHW, MEL": "SCHW_MEL",
        "SFT HMPC": "SFT",
        "MELAN": "MEL",
        "MELCYT": "MELCYT",
        # Non-tumoral / control classes
        "CONTR, CEBM": "CTRL_CEBM",
        "CONTR, HEMI": "CTRL_HEMI",
        "CONTR, WM": "CTRL_WM",
        "CONTR, PONS": "CTRL_PONS",
        "CONTR, HYPTHAL": "CTRL_HYPTHAL",
        "CONTR, PINEAL": "CTRL_PINE",
        "CONTR, INFLAM": "CTRL_INFLAM",
        "CONTR, REACT": "CTRL_REACT",
    }
    return mapping[row["methylation class"]]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["material"]
    mapping = {
        "Frozen": "FROZEN",
        "DNA_KRYO": "FROZEN",
        "FFPE": "FFPE",
        "DNA_FFPE": "FFPE",
    }
    return mapping[value]
