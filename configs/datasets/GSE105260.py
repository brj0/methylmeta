def dataset_id(row):
    return "GSE105260"


def description(row):
    return (
        "DNA methylation profiling of normal kidney, primary and metastatic "
        "clear cell renal cell carcinoma (ccRCC) tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Primary RCC tumor": "Clear cell renal cell carcinoma",
        "Metastasis RCC tumor": "Metastatic clear cell renal cell carcinoma",
        "Normal renal tissue": "Normal kidney tissue",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Primary RCC tumor": "RCC_CC",
        "Metastasis RCC tumor": "RCC_CC",
        "Normal renal tissue": "CTRL_REN",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    mapping = {
        "Primary RCC tumor": "Kidney",
        "Metastasis RCC tumor": None,
        "Normal renal tissue": "Kidney",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "Kidney"


def sample_type(row):
    mapping = {
        "Primary RCC tumor": "primary",
        "Metastasis RCC tumor": "metastasis",
        "Normal renal tissue": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
