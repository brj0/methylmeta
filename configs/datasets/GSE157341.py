def dataset_id(row):
    return "GSE157341"


def description(row):
    return (
        "DNA methylation signatures reveal the diversity of processes "
        "remodeling liver cancer methylomes"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease"]


def methylation_class(row):
    mapping = {
        "early hepatocellular carcinoma": "HCC",
        "fibrolamellar carcinoma": "HCC",
        "hepatocellular carcinoma": "HCC",
        "non-tumor liver tissue": "CTRL_LIV",
    }
    return mapping[row["disease"]]


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    mapping = {
        "early hepatocellular carcinoma": "primary",
        "fibrolamellar carcinoma": "primary",
        "hepatocellular carcinoma": "primary",
        "non-tumor liver tissue": "control",
    }
    return mapping[row["disease"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age at sampling"])
