def dataset_id(row):
    return "GSE42372"


def description(row):
    return "Methylation profiling classifies HIV-associated lymphoma"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    mapping = {
        "HIV-associated lymphoma": "HIV_LPD",
        "non-HIV lymphoma": None,
    }
    return mapping[row["disease state"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age"])
