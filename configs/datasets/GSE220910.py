def dataset_id(row):
    return "GSE220910"


def description(row):
    return (
        "DNA methylome analysis of primary prostate cancer and pathologic "
        "lymph node metastases in patients with low and high Gleason score"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "PROS_ADCA"


def sample_site(row):
    return {
        "primary_tumor": "prostate",
        "lymph_node_met": "lymph node",
    }[row["tumor type"]]


def primary_site(row):
    return "prostate"


def sample_type(row):
    return {
        "primary_tumor": "primary",
        "lymph_node_met": "metastasis",
    }[row["tumor type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return {
        "GS-6/7a": "ISUP 1",  # NOTE: 7a dropped
        "GS-9/10": "ISUP 5",
    }[row["gleason group"]]
