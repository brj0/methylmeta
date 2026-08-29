def dataset_id(row):
    return "GSE211634"


def description(row):
    return "Single olfactory neuroblastoma sample"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Olfactory neuroblastoma"


def methylation_class(row):
    return "ONB"


def sample_site(row):
    return "Sella Turcica"


def primary_site(row):
    return "Sella Turcica"


def sample_type(row):
    return "primary"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    return 58
