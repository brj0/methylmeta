def dataset_id(row):
    return "GSE291237"


def description(row):
    return (
        "Genome-wide DNA methylation of HER2-low and HER2-zero "
        "triple-negative breast cancer (multi-institutional cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Triple-Negative Breast Cancer"


def methylation_class(row):
    return "BR_CA_TN"


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
    return "female"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
