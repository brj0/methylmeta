def dataset_id(row):
    return "GSE77954"


def description(row):
    return (
        "Global methylation analysis of development and progression of "
        "colorectal carcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = " ".join(row["tissue type"].split())
    mapping = {
        "Adenoma": "Colorectal adenoma",
        "Carcinoma": "Colorectal carcinoma",
        "Metastasis": "Colorectal carcinoma metastasis",
    }
    return mapping.get(value, value)


def methylation_class(row):
    value = " ".join(row["tissue type"].split())
    mapping = {
        "Adenoma": "CR_AD",
        "Carcinoma": "CR_CA",
        "Metastasis": "CR_CA",
        "Normal colon adjacent to adenoma": "CTRL_COL",
        "Normal colon adjacent to carcinoma": "CTRL_COL",
        "Normal liver adjacent to liver metastasis": "CTRL_LIV",
    }
    return mapping[value]


def sample_site(row):
    return row["site"]


def primary_site(row):
    if row["tissue type"] == "Metastasis":
        return "Colon / rectum"
    return row["site"]


def sample_type(row):
    mapping = {
        "Adenoma": "primary",
        "Carcinoma": "primary",
        "Metastasis": "metastasis",
        "Normal colon adjacent to  adenoma": "control",
        "Normal colon adjacent to  carcinoma": "control",
        "Normal liver adjacent to liver metastasis": "control",
    }
    return mapping[row["tissue type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]


def age(row):
    return float(row["age (yrs)"])
