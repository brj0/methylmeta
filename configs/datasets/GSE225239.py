def dataset_id(row):
    return "GSE225239"


def description(row):
    return "DNA methylation of relapsed/refractory pediatric acute myeloid leukemia"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {"AML": "Acute myeloid leukemia"}
    return mapping.get(row["disease"], row["disease"])


def methylation_class(row):
    return "AML"


def sample_site(row):
    mapping = {"blood": "blood", "bone marrow": "bone marrow"}
    return mapping[row["tissue"]]


def primary_site(row):
    return "bone marrow"


def sample_type(row):
    return "recurrence"


def material_type(row):
    return "blood"
