def dataset_id(row):
    return "GSE270371"


def description(row):
    return "Meningioma methylation data (retrospective cohort)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
