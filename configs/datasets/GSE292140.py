def dataset_id(row):
    return "GSE292140"


def description(row):
    return (
        "Tubo-ovarian high-grade serous carcinoma methylomes of long-term "
        "survivors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "High-grade serous ovarian carcinoma"


def methylation_class(row):
    return "OVA_HGSC"


def sample_site(row):
    return "ovary"


def primary_site(row):
    return "ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    return "female"
