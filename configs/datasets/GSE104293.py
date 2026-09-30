def dataset_id(row):
    return "GSE104293"


def description(row):
    return "IDH-mutant low-grade glioma WHO grade II, EORTC 22033 trial"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Low-grade glioma, IDH-mutant, WHO grade II"


def methylation_class(row):
    return "LGG"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["tissue_type"]
    mapping = {
        "FFPE": "FFPE",
        "FROZEN": "FROZEN",
    }
    return mapping[value]


def tumor_grade(row):
    return "G2"


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
