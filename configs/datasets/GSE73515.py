def dataset_id(row):
    return "GSE73515"


def description(row):
    return "DNA methylation profiling of 105 primary neuroblastomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    return "NBL"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
