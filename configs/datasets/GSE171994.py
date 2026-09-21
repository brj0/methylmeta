def dataset_id(row):
    return "GSE171994"


def description(row):
    return "HNSCC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    value = row["p16_status"]
    mapping = {
        "neg": "HNSCC_HPVI",
        "pos": "HNSCC_HPVA",
        "NA": "HNSCC",
        None: "HNSCC",
    }
    return mapping[value]


def sample_site(row):
    return "Cervical Lymph Node"


def primary_site(row):
    return row["region of origin"]


def sample_type(row):
    return "metastasis"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["Sex"]
    mapping = {
        "sex": None,
        "m": "male",
        "f": "female",
    }
    return mapping[value]
