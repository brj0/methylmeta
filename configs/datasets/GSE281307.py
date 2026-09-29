def dataset_id(row):
    return "GSE281307"


def description(row):
    return (
        "Multimodal genome-wide survey of progressing and non-progressing "
        "breast ductal carcinoma in situ"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Progressor": "Ductal carcinoma in situ of the breast",
        "Non-progressor": "Ductal carcinoma in situ of the breast",
        "Adjacent_normal": "Adjacent normal breast tissue",
        "Normal": "Normal breast tissue",
    }
    return mapping[row["classification"]]


def methylation_class(row):
    mapping = {
        "Progressor": "DCIS",
        "Non-progressor": "DCIS",
        "Adjacent_normal": "CTRL_BR",
        "Normal": "CTRL_BR",
    }
    return mapping[row["classification"]]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    mapping = {
        "Progressor": "primary",
        "Non-progressor": "primary",
        "Adjacent_normal": "control",
        "Normal": "control",
    }
    return mapping[row["classification"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["nuclear_grade"]
    if value is None:
        return None
    mapping = {"1": "G1", "2": "G2", "3": "G3"}
    return mapping[str(value)]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
