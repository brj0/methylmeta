def dataset_id(row):
    return "GSE221219"


def description(row):
    return (
        "Self-identified race, genetic ancestry and the immunogenomic "
        "landscape of primary prostate cancer (2022)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "Benign adjacent prostate": "CTRL_PROS",
        "Primary prostate tumor": "PROS_ADCA",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Prostate"


def primary_site(row):
    return "Prostate"


def sample_type(row):
    mapping = {
        "Benign adjacent prostate": "control",
        "Primary prostate tumor": "primary",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
