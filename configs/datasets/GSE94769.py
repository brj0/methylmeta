def dataset_id(row):
    return "GSE94769"


def description(row):
    return "Thymoma"


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "A thymoma, DNA methylation": "THYMO_A",
        "B3 thymoma, DNA methylation": "THYMO_B3",
        "NET, DNA methylation": "THYMO_NET",
        "Normal, DNA methylation": "CONTR_THYM",
        "TC, DNA methylation": "THYMO_C",
    }
    return mapping[value]


def sample_site(row):
    return "Thymus"


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]
