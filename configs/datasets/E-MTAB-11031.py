def dataset_id(row):
    return "E-MTAB-11031"


def description(row):
    return "Methylation profiling of chondrosarcoma tumour samples"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "ACT central": "ACT",
        "primary central chondrosarcoma": "CSA",
        "dedifferentiated chondrosarcoma": "CSA_DD",
        "periosteal chondrosarcoma": "CSA_PERIOST",
        "normal": "CTRL_BONE",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "ACT central": "primary",
        "primary central chondrosarcoma": "primary",
        "dedifferentiated chondrosarcoma": "primary",
        "periosteal chondrosarcoma": "primary",
        "normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"]
    mapping = {"male": "male", "female": "female", "unknown": None}
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    return float(value)
