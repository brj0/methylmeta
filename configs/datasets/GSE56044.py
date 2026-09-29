def dataset_id(row):
    return "GSE56044"


def description(row):
    return (
        "Genome-wide DNA methylation analysis of lung carcinoma: "
        "124 lung carcinomas and 12 normal lung tissues"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    if row["Source"] == "Normal lung tissue":
        return "normal lung tissue"
    return "lung carcinoma"


def methylation_class(row):
    if row["Source"] == "Normal lung tissue":
        return "CTRL_LU"
    return "LU_CA"


def sample_type(row):
    mapping = {
        "Lung tumor": "primary",
        "Normal lung tissue": "control",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
