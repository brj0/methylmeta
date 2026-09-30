def dataset_id(row):
    return "GSE136583"


def description(row):
    return (
        "Tumor and non-tumor liver tissue from Peruvian patients with "
        "hepatocellular carcinoma (HCC), DNA hydroxy-methylation profiling"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["tissue"] == "hepatocellular carcinoma":
        return "Hepatocellular carcinoma"
    return "Normal liver tissue"


def methylation_class(row):
    if row["tissue"] == "hepatocellular carcinoma":
        return "HCC"
    return "CTRL_LIV"


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    mapping = {
        "hepatocellular carcinoma": "primary",
        "non-tumor liver": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
