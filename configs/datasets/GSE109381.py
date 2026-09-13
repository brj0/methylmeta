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
        "GBM, RTK I": "GBM_RTK_I",
        "GBM, RTK II": "GBM_RTK_II",
        "GBM, RTK III": "GBM_RTK_III",
        "GBM, MES": "GBM_MES",
        "GBM, MID": "GBM_MID",
        "GBM, MYCN": "GBM_MYCN",
        "GBM, G34": "GBM_G34",
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
        "CN": "CN",
        # Ependymal tumors
        "EPN, PF A": "EPN_PF_A",
        "EPN, PF B": "EPN_PF_B",
        "EPN, RELA": "EPN_RELA",
        "EPN, YAP": "EPN_YAP",
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
        "HGNET, BCOR": "HGNET_BCOR",
        "HGNET, MN1": "HGNET_MN1",
        "IHG": "IHG",
        "RETB": "RB",
        # Sellar region tumors
        "CPH, ADM": "CPH_ADM",
        "CPH, PAP": "CPH_PAP",
        "PITAD, ACTH": "PITAD_ACTH",
        "PITAD, FSH LH": "PITAD_FSH_LH",
        "PITAD, PRL": "PITAD_PRL",
        "PITAD, TSH": "PITAD_TSH",
        "PITAD, STH SPA": "PITAD_STH_SPA",
        "PITAD, STH DNS A": "PITAD_STH_DNS_A",
        "PITAD, STH DNS B": "PITAD_STH_DNS_B",
        "PITUI": "PITUI_SCO_GCT",
        "CONTR, ADENOPIT": "CONTR_ADENOPIT",
        # Pineal region tumors
        "PIN T,  PB A": "PIN_T_PB_A",
        "PIN T,  PB B": "PIN_T_PB_B",
        "PIN T, PB B": "PIN_T_PB_B",
        "PIN T, PPT": "PIN_T_PPT",
        "PIN_CYT": "PIN_CYT",
        "PTPR, A": "PTPR_A",
        "PTPR, B": "PTPR_B",
        # Choroid plexus tumors
        "PLEX, AD": "PLEX_AD",
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
        "PLASMA": "PLASMA",
        # Peripheral nerve sheath / mesenchymal / melanocytic tumors
        "SCHW": "SCHW",
        "SCHW, MEL": "SCHW_MEL",
        "SFT HMPC": "SFT",
        "MELAN": "MEL",
        "MELCYT": "MELCYT",
        # Non-tumoral / control classes
        "CONTR, CEBM": "CONTR_CEBM",
        "CONTR, HEMI": "CONTR_HEMI",
        "CONTR, WM": "CONTR_WM",
        "CONTR, PONS": "CONTR_PONS",
        "CONTR, HYPTHAL": "CONTR_HYPTHAL",
        "CONTR, PINEAL": "CONTR_PINEAL",
        "CONTR, INFLAM": "CONTR_INFLAM",
        "CONTR, REACT": "CONTR_REACT",
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
