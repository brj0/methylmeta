def dataset_id(row):
    return "GSE188547"


def description(row):
    return (
        "Glioblastoma IDH-wildtype cohort profiled for DNA methylation "
        "subclasses (Drexler et al. 2021)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["gender"]
    mapping = {"female": "female", "male": "male"}
    return mapping[value]


def age(row):
    return float(row["age"])
