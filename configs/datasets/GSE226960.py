def dataset_id(row):
    return "GSE226960"


def description(row):
    return (
        "DNA methylation profiling of childhood posterior fossa group A "
        "(PFA) ependymoma patient samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "EPN_PF_A"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    mapping = {
        "presentation": "primary",
        "recurrence": "recurrence",
    }
    return mapping[row["tumor stage"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["gender"]
