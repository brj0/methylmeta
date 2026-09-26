def dataset_id(row):
    return "E-MTAB-6884"


def description(row):
    return "DNA methylation profiling of malignant pleural mesothelioma"


def sample_id(row):
    return row["Sample_ID"].strip()


def diagnosis(row):
    return row["Characteristics[histology]"]


def methylation_class(row):
    value = row["Characteristics[histology]"]
    mapping = {
        "epithelioid mesothelioma": "MESOT_EPITH",
        "biphasic mesothelioma": "MESOT_BIPHASIC",
        "sarcomatoid mesothelioma": "MESOT_SARC",
        "desmoplastic mesothelioma": "MESOT_SARC",
        "lymphohistiocytoide mesothelioma": "MESOT",
        "normal": "CTRL_PLEURA",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    mapping = {
        "neoplasm": "primary",
        "normal pleura": "control",
    }
    return mapping[row["Characteristics[sampling site]"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "female": "female",
        "male": "male",
        "not available": None,
    }
    return mapping[row["Characteristics[sex]"]]


def age(row):
    value = row["Characteristics[age]"].strip()
    if not value or value.lower() == "not available":
        return None
    return float(value)
