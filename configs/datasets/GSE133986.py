def dataset_id(row):
    return "GSE133986"


def description(row):
    return "Genome wide DNA methylation of pediatric acute myeloid leukemia"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "AML"


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age"])
