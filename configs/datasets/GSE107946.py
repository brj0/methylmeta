def dataset_id(row):
    return "GSE107946"


def description(row):
    return (
        "Malignant rhabdoid tumors originating within and outside the "
        "central nervous system"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "CNS Tumor": "ATRT",
        "Extra-CNS Tumor": "MRT",
    }
    return mapping[row["location"]]


def sample_site(row):
    mapping = {
        "CNS Tumor": "Central nervous system",
        "Extra-CNS Tumor": None,
    }
    return mapping[row["location"]]


def primary_site(row):
    mapping = {
        "CNS Tumor": "Central nervous system",
        "Extra-CNS Tumor": None,
    }
    return mapping[row["location"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
