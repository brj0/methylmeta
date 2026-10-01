def dataset_id(row):
    return "GSE243240"


def description(row):
    return (
        "Molecular characteristics and improved survival prediction in a "
        "cohort of 2023 ependymomas (2024)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["patho diagnosis"]


def methylation_class(row):
    value = row["classification result v12"]
    mapping = {
        "EPN_MPE": "EPN_MPE",
        "EPN_PFA_1A": "EPN_PF_A",
        "EPN_PFA_1B": "EPN_PF_A",
        "EPN_PFA_1C": "EPN_PF_A",
        "EPN_PFA_1D": "EPN_PF_A",
        "EPN_PFA_1E": "EPN_PF_A",
        "EPN_PFA_1F": "EPN_PF_A",
        "EPN_PFA_2A": "EPN_PF_A",
        "EPN_PFA_2B": "EPN_PF_A",
        "EPN_PFA_2C": "EPN_PF_A",
        "EPN_PFB_1": "EPN_PF_B",
        "EPN_PFB_2": "EPN_PF_B",
        "EPN_PFB_3": "EPN_PF_B",
        "EPN_PFB_4": "EPN_PF_B",
        "EPN_PF_SE": "SUBEPN_PF",
        "EPN_SPINE": "EPN_SPINE",
        "EPN_SPINE_MYCN": "EPN_SPINE_MYCN",
        "EPN_SPINE_SE_B": "SUBEPN_SPINE",
        "EPN_ST_SE": "SUBEPN_ST",
        "EPN_ST_ZFTA_FUS_C": "EPN_ST_ZFTA",
        "EPN_ST_ZFTA_RELA_A": "EPN_ST_ZFTA",
        "EPN_YAP": "EPN_ST_YAP1",
    }
    return mapping[value]


def sample_site(row):
    return row["localization"]


def primary_site(row):
    return row["localization"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["Sex"]
    if value is None:
        return None
    mapping = {"F": "female", "M": "male"}
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
