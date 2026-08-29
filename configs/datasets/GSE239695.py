def dataset_id(row):
    return "GSE239695"


def description(row):
    return "Adamantinomatous craniopharyngioma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "CPH_ADM"


def sample_site(row):
    return "Jaw"


def primary_site(row):
    return "Jaw"


def sample_type(row):
    return "primary"


def preservation(row):
    return "FROZEN"


def sex(row):
    return row["sexo"]


def age(row):
    return row["age at diagnosis(years)"]
