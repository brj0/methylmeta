def dataset_id(row):
    return "GSE299377"


def description(row):
    return (
        "Postmortem non-neoplastic cerebellar cortex samples profiled on EPIC "
        "v1/v2"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "CTRL_CEBM"


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def age(row):
    value = row["age"]
    if value is None:
        return None
    parts = value.split()
    try:
        number = float(parts[0])
    except (IndexError, ValueError):
        return None
    if len(parts) > 1 and parts[1].lower().startswith("month"):
        return number / 12
    return number
