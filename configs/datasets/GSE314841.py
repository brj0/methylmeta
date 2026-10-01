def dataset_id(row):
    return "GSE314841"


def description(row):
    return (
        "DNA methylation of adjacent normal lung tissue from non-smoking "
        "East Asian lung adenocarcinoma patients"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Normal lung tissue"


def methylation_class(row):
    return "CTRL_LU"


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
