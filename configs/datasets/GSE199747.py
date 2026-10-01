def dataset_id(row):
    return "GSE199747"


def description(row):
    return (
        "Pediatric hepatocellular malignant neoplasm, NOS (HCN-NOS) tumors "
        "and adjacent non-tumor liver controls"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "HCN-NOS tumor": "Hepatocellular malignant neoplasm, NOS",
        "non-tumor control": "Normal liver tissue",
    }
    return mapping[row["group"]]


def methylation_class(row):
    mapping = {
        "HCN-NOS tumor": None,
        "non-tumor control": "CTRL_LIV",
    }
    return mapping[row["group"]]


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    mapping = {
        "HCN-NOS tumor": "primary",
        "non-tumor control": "control",
    }
    return mapping[row["group"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"M": "male", "F": "female"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
