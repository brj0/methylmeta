def dataset_id(row):
    return "E-MTAB-7924"


def description(row):
    return (
        "Genome-wide methylation profiling of sporadic pancreatic "
        "neuroendocrine tumors (PanNETs)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pancreatic neuroendocrine tumor": "PAN_NET",
        "normal": "CTRL_PAN",
    }
    return mapping[value]


def sample_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {
        "endocrine pancreas": "Pancreas",
        "pancreas": "Pancreas",
    }
    return mapping.get(value, value)


def primary_site(row):
    return "Pancreas"


def sample_type(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pancreatic neuroendocrine tumor": "primary",
        "normal": "control",
    }
    return mapping.get(value, "primary")


def material_type(row):
    # Material Type is 'organism part' for every sample.
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"]
    if value is None:
        return None
    mapping = {"male": "male", "female": "female"}
    return mapping.get(value.strip().lower())


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = str(value).strip()
    if value in {"", "not available", "not applicable", "unknown", "na"}:
        return None
    return float(value)
