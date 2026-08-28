def dataset_id(row):
    return "GSE197675"


def description(row):
    return "Childhood cancer survivors — peripheral blood"


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    return "CONTR_BLOOD"


def sample_site(row):
    return "Blood"


def primary_site(row):
    return "Blood"


def sample_type(row):
    return "control"


def preservation(row):
    return None


def sex(row):
    return row["gender"]


def age(row):
    return row["age"]
