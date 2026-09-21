def dataset_id(row):
    return "GSE308517"


def description(row):
    return "Peripheral Blood from ALL survivors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Title"]


def methylation_class(row):
    return "CTRL_BLOOD"


def sample_site(row):
    return "Blood"


def sex(row):
    return row["Sex"]


def age(row):
    return row["age at sample collection"]
