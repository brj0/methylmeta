def dataset_id(row):
    return "E-MTAB-7804"


def description(row):
    return (
        "Infant high grade gliomas comprise multiple subgroups "
        "characterised by novel targetable gene fusions "
        "(Clarke et al., 2020)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Factor Value[methylation_class]"]
    mapping = {
        "CONTR_CEBM": "normal cerebellar hemisphere",
        "CONTR_HEMI": "normal cerebral cortex",
        "CONTR_INFLAM": "inflammatory tumor microenvironment",
        "CONTR_PONS": "normal pons",
    }
    return mapping.get(value, row["Characteristics[disease]"])


def methylation_class(row):
    value = row["Factor Value[methylation_class]"]
    mapping = {
        "ATRT_SHH": "ATRT_SHH",
        "DMG_K27": "DMG_K27",
        "EPN_MPE": "EPN_MPE",
        "EPN_PF_A": "EPN_PF_A",
        "ETMR": "ETMR",
        "GBM_MES": "GBM_MES",
        "GBM_MID": "GBM_MID",
        "GBM_MYCN": "GBM_MYCN",
        "GBM_RTK_III": "GBM_RTK3",
        "HGNET_MN1": "HGNET_MN1",
        "HMB": "HMB",
        "IHG": "IHG",
        "LGG_DIG_DIA": "LGG_DIG_DIA",
        "LGG_DNT": "LGG_DNT",
        "LGG_GG": "LGG_GG",
        "LGG_MYB": "LGG_MYB",
        "LGG_PA_GG_ST": "LGG_PA_GG_ST",
        "LGG_PA_MID": "LGG_PA_MID",
        "LGG_PA_PF": "LGG_PA_PF",
        "LGG_SEGA": "LGG_SEGA",
        "MNG": "MNG",
        "PLEX_PED_A": "PLEX_PED_A",
        "PLEX_PED_B": "PLEX_PED_B",
        "PXA": "PXA",
        "CONTR_CEBM": "CTRL_CEBM",
        "CONTR_HEMI": "CTRL_HEMI",
        "CONTR_INFLAM": "CTRL_INFLAM",
        "CONTR_PONS": "CTRL_PONS",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    value = row["Factor Value[methylation_class]"]
    mapping = {
        "CONTR_CEBM": "control",
        "CONTR_HEMI": "control",
        "CONTR_INFLAM": "control",
        "CONTR_PONS": "control",
    }
    return mapping.get(value, "primary")


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {"female": "female", "male": "male"}
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if value is None or value.strip() == "":
        return None
    return float(value)
