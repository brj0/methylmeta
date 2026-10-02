def dataset_id(row):
    return "E-MTAB-10578"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Source Name"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "HN_SCC"


def sample_site(row):
    return "Head and Neck"


def primary_site(row):
    return "Head and Neck"


def sample_type(row):
    return "primary"


def sex(row):
    return row["Characteristics[sex]"]
