def dataset_id(row):
    return "GSE178216"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "adjacent non-tumor": "Normal adjacent non-tumor oral tissue",
        "tumor": "Oral squamous cell cancer",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "adjacent non-tumor": "CONTR_HN",
        "tumor": "HNSCC",
    }
    return mapping[value]


def sample_site(row):
    return "Oral cavity"


def primary_site(row):
    return "Oral cavity"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "adjacent non-tumor": "control",
        "tumor": "primary",
    }
    return mapping[value]
