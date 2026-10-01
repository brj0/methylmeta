def dataset_id(row):
    return "GSE221256"


def description(row):
    return (
        "DNA methylation profiling of hepatocellular carcinoma and adjacent "
        "normal liver tissue for early-stage HCC detection (2022)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "Hepatocellular carcinoma": "HCC",
        "normal liver tissue adjacent to the tumor (NAT)": "CTRL_LIV",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return "Liver"


def primary_site(row):
    return "Liver"


def sample_type(row):
    mapping = {
        "Hepatocellular carcinoma": "primary",
        "normal liver tissue adjacent to the tumor (NAT)": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Male": "male",
        "Female": "female",
        "not collected": None,
    }
    return mapping[row["gender"]]
