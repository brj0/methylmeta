def _organ(row):
    return {
        "Breast cancer BM": "Breast",
        "Lung cancer BM": "Lung",
    }[row["Source"]]


def dataset_id(row):
    return "GSE220826"


def description(row):
    return (
        "DNA methylation profiling of HER3-positive and HER3-negative brain "
        "metastases of breast and lung cancer"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    key = (_organ(row), row["tissue type"])
    mapping = {
        ("Breast", "HER2+"): "HER2-positive breast cancer brain metastasis",
        ("Breast", "Luminal"): "Luminal breast cancer brain metastasis",
        ("Breast", "TNBC"): ("Triple-negative breast cancer brain metastasis"),
        ("Lung", "NSCLC"): "Non-small cell lung carcinoma brain metastasis",
    }
    return mapping[key]


def methylation_class(row):
    key = (_organ(row), row["tissue type"])
    mapping = {
        ("Breast", "HER2+"): "BR_CA_HER2",
        ("Breast", "Luminal"): "BR_CA_HRP",
        ("Breast", "TNBC"): "BR_CA_TN",
        ("Lung", "NSCLC"): "NSCLC",
    }
    return mapping.get(key)


def sample_site(row):
    return "Brain"


def primary_site(row):
    return _organ(row)


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
