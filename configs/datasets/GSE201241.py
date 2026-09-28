def dataset_id(row):
    return "GSE201241"


def description(row):
    return "Integrative analysis of intrahepatic cholangiocarcinoma and non-neoplastic bile duct"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Title"].rsplit("_", 1)[-1]
    mapping = {
        "iCCA": "Intrahepatic cholangiocarcinoma",
        "non-neoplastic bile duct": "Non-neoplastic bile duct",
    }
    return mapping[value]


def methylation_class(row):
    if row["Title"].startswith("control"):
        return "CTRL_BD"
    return "CCA_INT"


def sample_site(row):
    return "Liver"


def primary_site(row):
    if row["Title"].startswith("control"):
        return None
    return "Liver"


def sample_type(row):
    if row["Title"].startswith("control"):
        return "control"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Fresh frozen": "FROZEN"}
    return mapping[row["tissue_type"]]


def sex(row):
    return row["gender"]


def age(row):
    value = row["age_years"]
    if value is None:
        return None
    return float(value)
