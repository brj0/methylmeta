def dataset_id(row):
    return "GSE117130"


def description(row):
    return (
        "Heterogeneity within the posterior fossa ependymoma group B "
        "(PF-EPN-B) subgroup"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "EPN_PF_B"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE Tumor": "FFPE",
        "Frozen Tumor": "FROZEN",
    }
    return mapping[row["tissue type"]]


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping.get(row["gender"])


def age(row):
    value = row["age"]
    return float(value) if value is not None else None
