def dataset_id(row):
    return "GSE210353"


def description(row):
    return "Proteogenomic cohort of primary pilocytic astrocytomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease"]


def methylation_class(row):
    return "LGG"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["tissue status"]
    mapping = {"FFPE": "FFPE", "FrFr": "FROZEN"}
    return mapping[value]
