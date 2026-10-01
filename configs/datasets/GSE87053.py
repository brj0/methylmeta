def dataset_id(row):
    return "GSE87053"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of oral squamous cell "
        "carcinoma lesions and adjacent normal oral mucosa"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["tissue type"] == "Adjacent Normal":
        return "adjacent normal oral mucosa"
    return "oral squamous cell carcinoma"


def methylation_class(row):
    if row["tissue type"] == "Adjacent Normal":
        return "CTRL_HN"
    mapping = {
        "HPV_Positive": "HNSCC_HPVA",
        "HPV_Negative": "HNSCC_HPVI",
    }
    return mapping[row["hpv status"]]


def sample_type(row):
    mapping = {
        "Adjacent Normal": "control",
        "OSCC lesion": "primary",
    }
    return mapping[row["tissue type"]]


def sample_site(row):
    return "Oral cavity"


def primary_site(row):
    return "Oral cavity"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["gender"]]
