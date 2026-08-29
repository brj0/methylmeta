def dataset_id(row):
    return "GSE79556"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "HNSCC"


def sample_site(row):
    return "Tongue"


def primary_site(row):
    return "Tongue"


def sample_type(row):
    return "primary"


def preservation(row):
    value = row["Source"]
    mapping = {
        "FFPE Primary OGSCC Tumour": "FFPE",
    }
    return mapping[value]


def sex(row):
    return row["gender"]
