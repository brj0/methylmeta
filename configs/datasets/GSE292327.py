def dataset_id(row):
    return "GSE292327"


def description(row):
    return "Meningioma FFPE cohort profiled for recurrence-risk methylation"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Meningioma"


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {"1": "G1", "2": "G2", "3": "G3"}
    return mapping[str(row["who grade"])]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]
