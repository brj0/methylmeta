def dataset_id(row):
    return "GSE66313"


def description(row):
    return (
        "DNA methylation in ductal carcinoma in situ related with future "
        "development of invasive breast cancer"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "DCIS": "Ductal carcinoma in situ of the breast",
        "Adjacent-Normal": "Adjacent normal breast tissue",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "DCIS": "DCIS",
        "Adjacent-Normal": "CTRL_BR",
    }
    return mapping[value]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "DCIS": "primary",
        "Adjacent-Normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female"}
    return mapping[value]


def age(row):
    return float(row["subject age"])
