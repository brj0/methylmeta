def dataset_id(row):
    return "GSE123601"


def description(row):
    return (
        "Primary extracranial malignant rhabdoid tumors (eMRT) and "
        "atypical teratoid/rhabdoid tumors (ATRT) of the DKFZ and TARGET "
        "cohorts, profiled by methylation arrays"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "ATRT": "atypical teratoid/rhabdoid tumor",
        "eMRT": "extracranial malignant rhabdoid tumor",
    }
    return mapping[row["tumor type"]]


def methylation_class(row):
    mapping = {
        "ATRT": "ATRT",
        "eMRT": "MRT",
    }
    return mapping[row["tumor type"]]


def sample_site(row):
    value = row["tissue"]
    if value is None:
        return None
    return value.replace("_", " ")


def primary_site(row):
    value = row["tissue"]
    if value is None:
        return None
    return value.replace("_", " ")


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
