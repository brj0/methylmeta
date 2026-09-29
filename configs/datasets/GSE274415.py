def dataset_id(row):
    return "GSE274415"


def description(row):
    return (
        "WSG-ADAPT validation cohort 2: DNA methylation of luminal breast "
        "cancer after short-term pre-operative endocrine therapy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "BR_CA_HRP"


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
