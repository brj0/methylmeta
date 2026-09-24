def dataset_id(row):
    return "GSE118132"


def description(row):
    return "Methylation heterogeneity within human lung carcinoid tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    value = row["diagnosis"]
    mapping = {
        "Atypical Carcinoids (ACs)": "LU_NET_ATYP",
        "Typical Carcinoids (TCs)": "LU_NET_TYP",
        None: "LU_NET",
    }
    return mapping[value]


def sample_site(row):
    return row["tumor in specimen"]


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["gender"]
    mapping = {"F": "female", "M": "male"}
    return mapping.get(value)


def age(row):
    return float(row["age (years)"])
