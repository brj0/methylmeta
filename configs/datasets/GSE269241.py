def dataset_id(row):
    return "GSE269241"


def description(row):
    return (
        "DNA methylation biomarkers predicting Wilms tumor disease progression"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["cell type"]
    mapping = {
        "tumour": "Wilms tumor (nephroblastoma)",
        "normal": "adjacent normal kidney tissue",
    }
    return mapping[value]


def methylation_class(row):
    value = row["cell type"]
    mapping = {
        "tumour": "WILMS",
        "normal": "CTRL_REN",
    }
    return mapping[value]


def sample_site(row):
    return "Kidney"


def primary_site(row):
    return "Kidney"


def sample_type(row):
    value = row["cell type"]
    mapping = {
        "tumour": "primary",
        "normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
