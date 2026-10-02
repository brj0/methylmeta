def dataset_id(row):
    return "E-MTAB-10577"


def description(row):
    return "HPV negative Head & Neck squamous cell carcinoma"


def sample_id(row):
    return row["Source Name"]


def diagnosis(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "head and neck malignant neoplasia": "HPV-Negative Head and Neck Squamous Cell Carcinoma",
    }
    return mapping[value]


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    return row["Characteristics[age]"]


def sample_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {"head": "Head and Neck"}
    return mapping[value]


def primary_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {"head": "Head and Neck"}
    return mapping[value]


def methylation_class(row):
    return "HN_SCC_HPVI"
