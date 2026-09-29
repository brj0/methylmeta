def dataset_id(row):
    return "GSE226569"


def description(row):
    return (
        "Tumor DNA methylation in the Women's Circle of Health Study breast "
        "cancer cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "BR_CA"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return {"Female": "female", "Male": "male"}[row["Sex"]]
