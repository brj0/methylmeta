def dataset_id(row):
    return "GSE164269"


def description(row):
    return "DNA methylation profiling of malignant pleural mesothelioma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["mesothelioma histotype"]


def methylation_class(row):
    mapping = {
        "Biphasic MPM": "MESOT_BIPHASIC",
        "Epithelioid MPM": "MESOT_EPITH",
        "Sarcomatoid MPM": "MESOT_SARC",
    }
    return mapping[row["mesothelioma histotype"]]


def sample_site(row):
    return "pleura"


def primary_site(row):
    return "pleura"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
