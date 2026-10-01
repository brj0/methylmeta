def dataset_id(row):
    return "GSE211686"


def description(row):
    return "High-grade serous ovarian cancer methylome of long-term survivors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["cell type"]


def methylation_class(row):
    return "OVA_HGSC"


def sample_type(row):
    mapping = {"Primary Tumor": "primary", "Relapse Tumor": "recurrence"}
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    return "female"


def primary_site(row):
    return "ovary"
