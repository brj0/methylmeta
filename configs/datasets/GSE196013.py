def dataset_id(row):
    return "GSE196013"


def description(row):
    return "ACVR1-mutant posterior fossa ependymoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Ependymoma, posterior fossa"


def methylation_class(row):
    return "EPN_PF"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["material"]]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["sex_predicted"]]


def age(row):
    return float(row["age"])
