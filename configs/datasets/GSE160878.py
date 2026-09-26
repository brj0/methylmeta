def dataset_id(row):
    return "GSE160878"


def description(row):
    return (
        "Merkel cell carcinoma primary, metastatic and adjacent normal skin "
        "samples with MCC cell lines"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    source = row["Source"]
    if source == "Normal":
        return "adjacent normal skin"
    if source == "cell_line":
        return "Merkel cell carcinoma cell line"
    return "Merkel cell carcinoma"


def methylation_class(row):
    mapping = {
        "Primary": "MCC",
        "Metastatic_LN": "MCC",
        "Metastatic_Sk": "MCC",
        "Normal": "CTRL_SKIN",
        "cell_line": "MCC",
    }
    return mapping[row["Source"]]


def sample_site(row):
    mapping = {
        "Primary": "skin",
        "Metastatic_LN": "lymph node",
        "Metastatic_Sk": "skin",
        "Normal": "skin",
        "cell_line": None,
    }
    return mapping[row["Source"]]


def primary_site(row):
    return "skin"


def sample_type(row):
    mapping = {
        "Primary": "primary",
        "Metastatic_LN": "metastasis",
        "Metastatic_Sk": "metastasis",
        "Normal": "control",
        "cell_line": None,
    }
    return mapping[row["Source"]]


def material_type(row):
    if row["Source"] == "cell_line":
        return "cell_line"
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
