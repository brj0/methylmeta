def dataset_id(row):
    return "GSE231574"


def description(row):
    return (
        "DNA methylation profiling of phyllodes tumours, fibroadenomas and "
        "metaplastic breast cancers"
    )


def sample_id(row):
    return row["Sample_ID"]


def methylation_class(row):
    sample_type = row["sample type"]
    if sample_type == "Fibroadenoma":
        return "BR_FAD"
    if sample_type == "Metaplastic Breast Cancer":
        return "BR_CA_META"
    if sample_type == "Phyllodes":
        grade = row["grade"]
        if grade is None:
            return "PHYT_NOS"
        mapping = {
            "Benign": "PHYT_BEN",
            "Borderline": "PHYT_BOR",
            "Malignant": "PHYT_MAL",
        }
        return mapping[grade]
    return None


def diagnosis(row):
    sample_type = row["sample type"]
    if sample_type == "Phyllodes":
        grade = row["grade"]
        if grade:
            return grade + " phyllodes tumour"
        return "Phyllodes tumour"
    mapping = {
        "Fibroadenoma": "Fibroadenoma of the breast",
        "Metaplastic Breast Cancer": "Metaplastic carcinoma of the breast",
    }
    return mapping[sample_type]


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return "female"


def age(row):
    value = row["age at diagnosis"]
    if value is None:
        return None
    return float(value)
