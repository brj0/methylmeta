def dataset_id(row):
    return "GSE212621"


def description(row):
    return "DNA methylation profiling of the novel CNS embryonal tumor type ET, PLAGL"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "PLAGL1": "CNS embryonal tumor with PLAGL1 amplification",
        "PLAGL2": "CNS embryonal tumor with PLAGL2 amplification",
        "no PLAGL1/2 amplification": (
            "CNS embryonal tumor, PLAGL1/PLAGL2 amplification-negative"
        ),
    }
    return mapping[row["tumor subgroup"]]


def methylation_class(row):
    mapping = {
        "PLAGL1": "PLAGL1_NEUEPT",
        "PLAGL2": "CNS_EMB_NEC",
        "no PLAGL1/2 amplification": "CNS_EMB_NEC",
    }
    return mapping[row["tumor subgroup"]]


def sample_site(row):
    return row["location"]


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
