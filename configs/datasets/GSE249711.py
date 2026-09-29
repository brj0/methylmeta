def dataset_id(row):
    return "GSE249711"


def description(row):
    return (
        "Methylation profiling of medullary thyroid carcinoma for the "
        "identification of sites of origin in carcinoma of unknown primary"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor type"]


def methylation_class(row):
    mapping = {
        "Medullary Thyroid": "MTC",
    }
    return mapping[row["tumor type"]]


def sample_site(row):
    return "Thyroid"


def primary_site(row):
    return "Thyroid"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
