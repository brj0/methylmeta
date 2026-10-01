def dataset_id(row):
    return "GSE61441"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of clear cell renal cell "
        "carcinoma (ccRCC) tissue versus matched normal kidney tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Normal": "Normal kidney tissue",
        "Tumor": "Clear cell renal cell carcinoma",
    }
    return mapping[row["sample type"]]


def methylation_class(row):
    mapping = {"Normal": "CTRL_REN", "Tumor": "RCC_CC"}
    return mapping[row["sample type"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    mapping = {"Normal": "control", "Tumor": "primary"}
    return mapping[row["sample type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return row["gender"]
