def dataset_id(row):
    return "GSE193196"


def description(row):
    return (
        "Microdissected low-grade and high-grade areas of desmoplastic "
        "infantile astrocytoma / ganglioglioma (DIA/DIG)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "desmoplastic infantile astrocytoma / ganglioglioma"


def methylation_class(row):
    return "LGG_DIG_DIA"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["Title"]
    mapping = {"H": "high-grade", "L": "low-grade"}
    return mapping[value[-1:]]
