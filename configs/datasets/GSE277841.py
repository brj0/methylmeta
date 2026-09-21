def dataset_id(row):
    return "GSE277841"


def description(row):
    return "Peripheral blood mononuclear cells from patients with primary myelofibrosis and healthy donors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Title"]


def methylation_class(row):
    value = row["Title"]

    if "Healthy control" in value:
        return "CTRL_BLOOD"
    if "ET" in value:
        return "ET"
    if "PMF" in value:
        return "PMF"
    return None


def sample_site(row):
    return row["tissue"]


def sample_type(row):
    value = row["Title"]

    if "Healthy control" in value:
        return "control"
    if "ET" in value:
        return "primary"
    if "PMF" in value:
        return "primary"
    return None


def sex(row):
    return row["Sex"]


def age(row):
    return row["age"]
