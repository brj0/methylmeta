def dataset_id(row):
    return "GSE156546"


def description(row):
    return "Blood samples with essential thrombocythemia and blood controls"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    value = row["disease state"]
    mapping = {
        "essential thrombocythemia": "ET",
        "healthy control": "CONTR_BLOOD",
    }
    return mapping[value]


def sample_site(row):
    return "Blood"


def primary_site(row):
    return "Blood"
