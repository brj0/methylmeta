def dataset_id(row):
    return "GSE256413"


def description(row):
    return (
        "DNA methylation profiles of lymph node tissue of head and neck "
        "cancer of unknown primary"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Head and neck squamous cell carcinoma of unknown primary (hnCUP)"


def methylation_class(row):
    return "HN_SCC"


def sample_site(row):
    return "Cervical lymph node"


def primary_site(row):
    return "Head and neck"


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["g"]
    mapping = {"1": "G1", "2": "G2", "3": "G3"}
    return mapping[str(value)]


def sex(row):
    value = row["gender (0 = male, 1 = female)"]
    mapping = {"0": "male", "1": "female"}
    return mapping[str(value)]


def age(row):
    return float(row["age at diagnosis"])
