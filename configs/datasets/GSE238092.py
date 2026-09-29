def dataset_id(row):
    return "GSE238092"


def description(row):
    return (
        "Epigenome-wide DNA methylation analysis in inflammatory breast cancer"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "inflammatory breast cancer tissue": "inflammatory breast cancer",
        "normal adjacent breast tissue": "normal breast tissue",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "inflammatory breast cancer tissue": "BR_CA",
        "normal adjacent breast tissue": "CTRL_BR",
    }
    return mapping[value]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "inflammatory breast cancer tissue": "primary",
        "normal adjacent breast tissue": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
