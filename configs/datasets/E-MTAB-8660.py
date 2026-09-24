def dataset_id(row):
    return "E-MTAB-8660"


def description(row):
    return "Methylation profiling of lung adenocarcinoma brain metastases"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "lung adenocarcinoma": "LU_ADCA",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "lung"


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"].strip().lower()
    mapping = {
        "female": "female",
        "male": "male",
    }
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    return float(value)
