def _tumor_group(title):
    if title.startswith("MPNST"):
        return "MPNST"
    if title.startswith("VS"):
        return "VS"
    if title.startswith("N"):
        return "N"
    return None


def dataset_id(row):
    return "GSE212963"


def description(row):
    return "Peripheral nerve tumors in neurofibromatosis"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "MPNST": "Malignant peripheral nerve sheath tumor",
        "VS": "Schwannoma",
        "N": "Normal peripheral nerve",
    }
    return mapping[_tumor_group(row["Title"])]


def methylation_class(row):
    mapping = {
        "MPNST": "MPNST",
        "VS": "SCHW",
        "N": "CTRL_NERVE",
    }
    return mapping[_tumor_group(row["Title"])]


def sample_site(row):
    return "Peripheral nerve"


def primary_site(row):
    return "Peripheral nerve"


def sample_type(row):
    mapping = {
        "MPNST": "primary",
        "VS": "primary",
        "N": "control",
    }
    return mapping[_tumor_group(row["Title"])]


def material_type(row):
    return "tissue"
