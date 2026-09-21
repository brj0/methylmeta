def dataset_id(row):
    return "GSE108576"


def description(row):
    return (
        "Epigenetic profiling for the molecular classification of "
        "metastatic brain tumors, Orozco 2018"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    value = row["disease state"]
    mapping = {
        "Breast cancer brain metastasis": "BR_CA",
        "Lung cancer brain metastasis": "NSCLC",
        "Melanoma brain metastasis": "MEL",
        "Uncertain primary tumor brain metastasis": "CUPS",
    }
    return mapping[value]


def sample_site(row):
    return "Brain"


def primary_site(row):
    value = row["disease state"]
    mapping = {
        "Breast cancer brain metastasis": "Breast",
        "Lung cancer brain metastasis": "Lung",
        "Melanoma brain metastasis": "Skin",
        "Uncertain primary tumor brain metastasis": None,
    }
    return mapping[value]


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
