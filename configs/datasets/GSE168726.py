def dataset_id(row):
    return "GSE168726"


def description(row):
    return "Meningioma methylation analysis"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "meningioma"


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


def preservation(row):
    return "FROZEN"
