def dataset_id(row):
    return "GSE203152"


def description(row):
    return (
        "DNA methylation profiling of intra- and extracranial melanoma "
        "metastases"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "MEL"


def sample_site(row):
    mapping = {
        "Melanoma brain metastasis": "Brain",
        "Melanoma liver metastasis": "Liver",
        "Melanoma lung metastasis": "Lung",
        "Melanoma lymph node metastasis": "Lymph node",
        "Melanoma skin metastasis": "Skin",
        "Melanoma soft tissue metastasis": "Soft tissue",
    }
    return mapping[row["Source"]]


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
