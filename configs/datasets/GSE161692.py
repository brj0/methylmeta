def dataset_id(row):
    return "GSE161692"


def description(row):
    return (
        "ATRTs, extracranial malignant rhabdoid tumors and SCCOHT with "
        "SMARCA4 mutations profiled by DNA methylation"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["subject status"]
    mapping = {
        "Atypical teratoid/rhabdoid tumors (ATRTs)": (
            "Atypical teratoid/rhabdoid tumor"
        ),
        "extracranial malignant rhabdoid tumors (eMRTs)": (
            "Extracranial malignant rhabdoid tumor"
        ),
        "small cell carcinoma of the ovary hypercalcemic type (SCCOHT)": (
            "Small cell carcinoma of the ovary, hypercalcemic type"
        ),
    }
    return mapping[value]


def methylation_class(row):
    value = row["subject status"]
    mapping = {
        "Atypical teratoid/rhabdoid tumors (ATRTs)": "ATRT",
        "extracranial malignant rhabdoid tumors (eMRTs)": "ERT",
        "small cell carcinoma of the ovary hypercalcemic type (SCCOHT)": (
            "SCCOHT"
        ),
    }
    return mapping[value]


def sample_site(row):
    value = row["subject status"]
    mapping = {
        "Atypical teratoid/rhabdoid tumors (ATRTs)": "Central nervous system",
        "extracranial malignant rhabdoid tumors (eMRTs)": None,
        "small cell carcinoma of the ovary hypercalcemic type (SCCOHT)": (
            "Ovary"
        ),
    }
    return mapping[value]


def primary_site(row):
    value = row["subject status"]
    mapping = {
        "Atypical teratoid/rhabdoid tumors (ATRTs)": "Central nervous system",
        "extracranial malignant rhabdoid tumors (eMRTs)": None,
        "small cell carcinoma of the ovary hypercalcemic type (SCCOHT)": (
            "Ovary"
        ),
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["Sex"]
    mapping = {
        "female": "female",
        "male": "male",
        "n/a": None,
    }
    return mapping[value]
