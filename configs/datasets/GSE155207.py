def dataset_id(row):
    return "GSE155207"


def description(row):
    return "Epigenome analysis of normal and FH-deficient renal cell cancer samples"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "Tumor": "FH-deficient renal cell carcinoma",
        "Normal": "Normal kidney tissue",
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "Tumor": "RCC_FH",
        "Normal": "CTRL_REN",
    }
    return mapping[value]


def sample_site(row):
    return "Kidney"


def primary_site(row):
    return "Kidney"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "Tumor": "primary",
        "Normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"
