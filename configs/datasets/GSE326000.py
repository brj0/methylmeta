def dataset_id(row):
    return "GSE326000"


def description(row):
    return (
        "Differential methylation of promoters for histotype stratification "
        "in early-stage epithelial ovarian cancer"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "CCC": "Clear cell carcinoma of the ovary",
        "EC": "Endometrioid carcinoma of the ovary",
        "HGSC": "High-grade serous ovarian carcinoma",
        "MC": "Mucinous carcinoma of the ovary",
    }
    return mapping[row["histological subtype"]]


def methylation_class(row):
    mapping = {
        "CCC": "OVA_CCC",
        "EC": "OVA_ENDOID_CA",
        "HGSC": "OVA_HGSC",
        "MC": "OVA_MUC_CA",
    }
    return mapping[row["histological subtype"]]


def sample_site(row):
    return "Ovary"


def primary_site(row):
    return "Ovary"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return "female"
