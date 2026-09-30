def dataset_id(row):
    return "GSE104210"


def description(row):
    return (
        "DNA methylation profiling of posterior fossa type A (PFA) ependymoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Ependymoma, posterior fossa group A"


def methylation_class(row):
    return "EPN_PF_A"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]


def age(row):
    try:
        return float(row["age"])
    except ValueError:
        return None
