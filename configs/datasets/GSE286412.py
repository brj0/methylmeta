def dataset_id(row):
    return "GSE286412"


def description(row):
    return "Melanoma and Normal lymph node"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "Melanoma": "CMEL",
        "Lymph node - healthy": "CONTR_LYMPH",
        "Lymph node - melanoma": "CMEL",
    }
    return mapping[value]


def sample_site(row):
    value = row["tissue"]
    mapping = {
        "Melanoma": "Skin",
        "Lymph node - healthy": "Lymph node",
        "Lymph node - melanoma": "Lymph node",
    }
    return mapping[value]


def primary_site(row):
    value = row["tissue"]
    mapping = {
        "Melanoma": "Skin",
        "Lymph node - healthy": None,
        "Lymph node - melanoma": "Skin",
    }
    return mapping[value]


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "Melanoma": "primary",
        "Lymph node - healthy": "control",
        "Lymph node - melanoma": "metastasis",
    }
    return mapping[value]


def preservation(row):
    value = row["tissue type"]
    mapping = {
        "Fresh frozen": "FROZEN",
    }
    return mapping[value]
