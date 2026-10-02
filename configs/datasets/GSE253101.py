def dataset_id(row):
    return "GSE253101"


def description(row):
    return "DNA methylation-based classification of common renal tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnosis"]
    if value in {"Cortex", "Medulla"}:
        return "Normal kidney " + value.lower()
    return value


def methylation_class(row):
    mapping = {
        "ccRCC": "RCC_CC",
        "RCC_unclassifiable": "RCC",
        "Oncocytoma": "REN_ONC",
        "HLRCC": "RCC_FH",
        "ChRCC": "RCC_CP",
        "Hybrid": "HOCT",
        "AML": "REN_PEC",
        "PRCC": "RCC_PAP",
        "PRCC T1": "RCC_PAP",
        "PRCC T2": "RCC_PAP",
        "Metanephric adenoma": "REN_METAD",
        "HOCT": "HOCT",
        "Reverse polarity": "RCC_RP",
        "ccPRCC": "RCC_CCP",
        "Wilms tumor": "WILMS",
        "Oncocytic neoplasm": None,
        "MRT": "REN_MRT",
        "CCSK": "REN_CCS",
        "Cortex": "CTRL_REN",
        "Medulla": "CTRL_REN",
    }
    return mapping[row["diagnosis"]]


def sample_site(row):
    return "Kidney"


def primary_site(row):
    return "Kidney"


def sample_type(row):
    mapping = {"Normal": "control", "Tumor": "primary"}
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male", None: None}
    return mapping[row["gender"]]
