def dataset_id(row):
    return "GSE242060"


def description(row):
    return (
        "Treatment-naive high-grade serous ovarian cancer methylation "
        "profiles in Black and non-Hispanic White women"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "High-grade serous ovarian carcinoma"


def methylation_class(row):
    return "OVA_HGSC"


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    return "female"
