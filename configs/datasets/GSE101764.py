def dataset_id(row):
    return "GSE101764"


def description(row):
    return (
        "ColoCare Project: DNA methylation in colorectal cancer and "
        "adjacent mucosa tissues (University Hospital of Heidelberg)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    if value == "tumor":
        return row["disease state"]
    if value == "mucosa":
        return "Normal colon mucosa"
    return None


def methylation_class(row):
    mapping = {"tumor": "CR_CA", "mucosa": "CTRL_COL"}
    return mapping[row["tissue"]]


def sample_site(row):
    return "Colon"


def primary_site(row):
    return "Colon"


def sample_type(row):
    mapping = {"tumor": "primary", "mucosa": "control"}
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
