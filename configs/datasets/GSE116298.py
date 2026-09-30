def dataset_id(row):
    return "GSE116298"


def description(row):
    return (
        "Intra-tumor DNA methylation heterogeneity in glioblastoma, "
        "with meningioma samples as homogeneous reference"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "High-grade glioma": "High-grade glioma",
        "high-grade glioma": "High-grade glioma",
        "Meningioma": "Meningioma",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "High-grade glioma": "GBM_NOS",
        "high-grade glioma": "GBM_NOS",
        "Meningioma": "MNG",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]


def tumor_grade(row):
    mapping = {
        "High-grade glioma": "high-grade",
        "high-grade glioma": "high-grade",
        "Meningioma": None,
    }
    return mapping[row["tissue"]]
