def dataset_id(row):
    return "GSE136704"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    mapping = {
        "Normal": "Normal oropharyngeal tissue",
        "Cancer": "oropharyngeal Cancer",
    }
    return mapping[value]


def methylation_class(row):
    value = row["disease state"]
    mapping = {
        "Normal": "CTRL_HN",
        "Cancer": "HN_SCC",
    }
    return mapping[value]


def sample_site(row):
    return "Oropharynx"


def primary_site(row):
    return "Oropharynx"


def sample_type(row):
    value = row["disease state"]
    mapping = {
        "Normal": "control",
        "Cancer": "primary",
    }
    return mapping[value]


def sex(row):
    return row["gender"]
