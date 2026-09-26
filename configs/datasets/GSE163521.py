def dataset_id(row):
    return "GSE163521"


def description(row):
    return (
        "Breast cancers with low hormone receptor expression (LowHR) and "
        "triple negative breast cancers (TNBC) from the GeparSixto and "
        "GeparSepto trials"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "LowHR": (
            "Invasive breast carcinoma with low hormone receptor expression"
        ),
        "TNBC": "Triple negative breast carcinoma",
    }
    return mapping[row["subtype"]]


def methylation_class(row):
    if row["subtype"] == "TNBC":
        return "BR_CA_TN"
    if row["her2"] == "Positive":
        return "BR_CA_HER2"
    return "BR_CA"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return {"Female": "female", "Male": "male"}[row["gender"]]
