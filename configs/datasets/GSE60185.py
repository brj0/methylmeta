def dataset_id(row):
    return "GSE60185"


def description(row):
    return (
        "Breast cancer progression to in situ and invasive carcinoma "
        "(Fleischer et al. 2014)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["disease state"] == "normal":
        return "Normal breast tissue"
    value = row["sample tissue"]
    mapping = {
        "DCIS": "Ductal carcinoma in situ of the breast",
        "invasive": "Invasive breast carcinoma",
        "mixed DCIS-invasive": (
            "Mixed ductal carcinoma in situ and invasive breast carcinoma"
        ),
        "mammoplastic reduction": "Normal breast tissue",
        "needle biopsy": "Breast carcinoma, needle biopsy",
    }
    return mapping[value]


def methylation_class(row):
    if row["disease state"] == "normal":
        return "CTRL_BR"
    mapping = {
        "mammoplastic reduction": "CTRL_BR",
        "DCIS": "DCIS",
        "invasive": "BR_CA_NST",
        "mixed DCIS-invasive": "BR_CA",
        "needle biopsy": "BR_CA",
    }
    return mapping[row["sample tissue"]]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    mapping = {"breast cancer": "primary", "normal": "control"}
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def sex(row):
    return "female"


def age(row):
    value = row["age"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
