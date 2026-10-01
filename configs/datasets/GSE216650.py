def dataset_id(row):
    return "GSE216650"


def description(row):
    return "Human Tumor Atlas Pilot Project (HTAPP) neuroblastoma cohort"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Neuroblastoma"


def methylation_class(row):
    return "NBL"


def sample_type(row):
    mapping = {
        "1": "primary",
        "2A": "primary",
        "2B": "primary",
        "3": "primary",
        "4": "primary",
        "4S": "primary",
        "Recurrent": "recurrence",
    }
    return mapping[row["inss stage"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"].strip()
    if value.startswith("<"):
        value = value[1:].strip()
    number, unit = value.split()
    number = float(number)
    if unit.startswith("yr"):
        return number
    return round(number / 12, 2)
