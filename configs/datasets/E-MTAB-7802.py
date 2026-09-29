def dataset_id(row):
    return "E-MTAB-7802"


def description(row):
    return (
        "Infant high grade gliomas comprise multiple methylation subgroups "
        "characterised by novel targetable gene fusions"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Factor Value[methylation_class]"]
    mapping = {
        "CONTR_CEBM": "normal cerebellar hemisphere",
        "CONTR_HYPTHAL": "normal hypothalamus",
        "CONTR_INFLAM": "inflammatory tumor microenvironment",
    }
    return mapping.get(value, row["Characteristics[disease]"])


def methylation_class(row):
    value = row["Factor Value[methylation_class]"]
    mapping = {
        "IHG": "IHG",
        "DMG_K27": "DMG_K27",
        "PXA": "PXA",
        "GBM_MES": "GBM_MES",
        "GBM_MID": "GBM_MID",
        "GBM_MYCN": "GBM_MYCN",
        "LGG_DIG_DIA": "LGG_DIG_DIA",
        "LGG_PA_GG_ST": "LGG_PA_GG_ST",
        "LGG_PA_MID": "LGG_PA_MID",
        "LGG_SEGA": "LGG_SEGA",
        "PLEX_PED_B": "PLEX_PED_B",
        "MNG": "MNG",
        "SCHW": "SCHW",
        "DLGNT": "DLGNT",
        "EPN_RELA": "EPN_ST_ZFTA",
        "HGNET_BCOR": "CNS_BCOR_ITD",
        "CONTR_CEBM": "CTRL_CEBM",
        "CONTR_HYPTHAL": "CTRL_HYPTHAL",
        "CONTR_INFLAM": "CTRL_INFLAM",
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
        "CONTR_HYPTHAL": "control",
        "CONTR_INFLAM": "control",
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
    if value is None or value.strip() == "not available":
        return None
    return float(value)
