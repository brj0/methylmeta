def dataset_id(row):
    return "GSE159907"


def description(row):
    return "DNA methylation analysis of acute myeloid leukemia (AML)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Acute myeloid leukemia"


def methylation_class(row):
    return "AML"


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    mapping = {
        "Diagnosis": "primary",
        "Relapse": "recurrence",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "blood"
