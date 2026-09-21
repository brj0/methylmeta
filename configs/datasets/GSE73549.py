def dataset_id(row):
    return "GSE73549"


def description(row):
    return "Prostate cancer & Normal lymph nodes"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["sample info"]


def methylation_class(row):
    tissue = row["tissue type"]
    disease = row["disease state"]

    if tissue == "Lymph node" and disease == "Metastasis":
        return "PRAD"
    if tissue == "Lymph node" and disease == "Normal":
        return "CTRL_LYMPH"
    if tissue == "Prostate" and disease == "Normal":
        return "CTRL_PROST"
    if tissue == "Prostate" and disease == "Tumor":
        return "PRAD"
    if tissue == "Prostate" and disease == "PIN":
        return "PROST_PIN"
    return None


def sample_site(row):
    return row["tissue type"]


def primary_site(row):
    tissue = row["tissue type"]
    disease = row["disease state"]

    if tissue == "Lymph node" and disease == "Metastasis":
        return "Prostate"
    if tissue == "Lymph node" and disease == "Normal":
        return None
    if tissue == "Prostate" and disease == "Normal":
        return None
    if tissue == "Prostate" and disease == "Tumor":
        return "Prostate"
    return None


def sample_type(row):
    disease = row["disease state"]

    if disease == "Normal":
        return "control"
    if disease == "Metastasis":
        return "metastasis"
    if disease == "Tumor":
        return "primary"
    return None


def preservation(row):
    return row["sample type"]


def sex(row):
    return row["gender"]
