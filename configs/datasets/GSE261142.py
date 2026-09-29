def dataset_id(row):
    return "GSE261142"


def description(row):
    return (
        "Predictors of primary endocrine resistance in hormone receptor "
        "positive breast cancer (WSG-ADAPT trial)"
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
    value = row["age (years)"]
    if value is None:
        return None
    return float(value)
