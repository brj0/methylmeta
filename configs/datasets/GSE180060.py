def dataset_id(row):
    return "GSE180060"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of lung adenocarcinoma samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "lung adenocarcinoma"


def methylation_class(row):
    return "LU_ADCA"


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FRESH"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
        "Unknown": None,
    }
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
