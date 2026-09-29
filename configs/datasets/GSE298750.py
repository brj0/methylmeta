def dataset_id(row):
    return "GSE298750"


def description(row):
    return "Predicting immune responsiveness in ER-positive breast cancer"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "ER-positive breast cancer"


def methylation_class(row):
    return {"Positive": "BR_CA_HRP"}[row["er_status"]]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return {"Pretreatment": "primary"}[row["treatment"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
