def dataset_id(row):
    return "GSE151067"


def description(row):
    return "Multisite methylation profiling of primary human meningioma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return row["site"]


def primary_site(row):
    return "Meninges"


def sample_type(row):
    mapping = {"Intracranial": "primary", "Liver": "metastasis"}
    return mapping[row["site"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
