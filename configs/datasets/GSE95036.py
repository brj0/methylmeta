def dataset_id(row):
    return "GSE95036"


def description(row):
    return "HNSCC HPV+/-"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["hpv status"]
    mapping = {
        "Positive": "HPV-positive HNSCC",
        "Negative": "HPV-negative HNSCC",
    }
    return mapping[value]


def methylation_class(row):
    value = row["hpv status"]
    mapping = {
        "Positive": "HNSCC_HPVA",
        "Negative": "HNSCC_HPVI",
    }
    return mapping[value]


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    return "primary"


def sex(row):
    return row["gender"]
