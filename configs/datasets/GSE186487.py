def dataset_id(row):
    return "GSE186487"


def description(row):
    return (
        "Methylation analysis of ALK-positive pediatric anaplastic large cell "
        "lymphoma (diagnosis and relapse samples)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Anaplastic large cell lymphoma, ALK-positive"


def methylation_class(row):
    return "ALCL_ALK_POS"


def sample_site(row):
    return row["sample source"]


def sample_type(row):
    mapping = {
        "ALCL Diagnosis": "primary",
        "ALCL Relapse": "recurrence",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping[row["gender"]]


def age(row):
    return float(row["age at diagnosis"])
