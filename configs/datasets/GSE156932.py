def dataset_id(row):
    return "GSE156932"


def description(row):
    return (
        "DNA methylation profiling of renal oncocytoma, chromophobe and "
        "clear cell renal cell carcinoma, hybrid oncocytic tumours and "
        "tumor-adjacent normal kidney parenchyma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "clear cell renal cell carcinoma": ("Clear cell renal cell carcinoma"),
        "hybrid oncocytic renal neoplasm": "Hybrid oncocytic renal neoplasm",
        "hybrid oncocytic/chromophobe type": (
            "Hybrid oncocytic/chromophobe renal tumour"
        ),
        "normal kidney parenchyma": "Normal kidney parenchyma",
        "oncocytoma": "Oncocytoma of the kidney",
        "renal cell carcinoma-chromophobe": (
            "Chromophobe renal cell carcinoma"
        ),
    }
    return mapping[row["sample type"]]


def methylation_class(row):
    mapping = {
        "clear cell renal cell carcinoma": "RCC_CC",
        "hybrid oncocytic renal neoplasm": "HOCT",
        "hybrid oncocytic/chromophobe type": "HOCT",
        "normal kidney parenchyma": "CTRL_REN",
        "oncocytoma": "REN_ONC",
        "renal cell carcinoma-chromophobe": "RCC_CP",
    }
    return mapping[row["sample type"]]


def sample_site(row):
    return "Kidney"


def primary_site(row):
    return "Kidney"


def sample_type(row):
    mapping = {
        "clear cell renal cell carcinoma": "primary",
        "hybrid oncocytic renal neoplasm": "primary",
        "hybrid oncocytic/chromophobe type": "primary",
        "normal kidney parenchyma": "control",
        "oncocytoma": "primary",
        "renal cell carcinoma-chromophobe": "primary",
    }
    return mapping[row["sample type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
