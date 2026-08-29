def dataset_id(row):
    return "GSE218549"


def description(row):
    return "Thymoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "atypical type A thymoma": None,
        "micronodular thymoma": "THY_MN",
        "normal thymus": "CONTR_THYM",
        "type A thymoma": "THYMO_A",
        "type AB thymoma": "THYMO_AB",
        "type B1 thymoma": "THYMO_B1",
        "type B2 thymoma": "THYMO_B2",
        "type B3 thymoma": "THYMO_B3",
    }
    return mapping[value]


def sample_site(row):
    return "Thymus"


def preservation(row):
    return row["material"]
