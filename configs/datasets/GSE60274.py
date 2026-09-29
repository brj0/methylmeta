def dataset_id(row):
    return "GSE60274"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of 68 glioblastoma specimens "
        "(primary and recurrent), 4 glioma sphere lines and 5 non-tumor brain "
        "samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "GBM": "Glioblastoma",
        "Non-tumor brain": "Non-tumor brain tissue",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    mapping = {
        "GBM": "GBM_NOS",
        "Non-tumor brain": "CTRL_BRAIN",
    }
    return mapping[row["disease state"]]


def sample_type(row):
    mapping = {
        "Surgical": "primary",
        "cultured": "primary",
        "recurrent": "recurrence",
        "Lobectomy": "control",
        "Craniotomy": "control",
    }
    return mapping[row["Source"].split()[0]]


def material_type(row):
    mapping = {
        "Surgical": "tissue",
        "cultured": "cell_line",
        "recurrent": "tissue",
        "Lobectomy": "tissue",
        "Craniotomy": "tissue",
    }
    return mapping[row["Source"].split()[0]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sex(row):
    mapping = {"F": "female", "M": "male", "U": None}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
