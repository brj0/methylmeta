def dataset_id(row):
    return "GSE141338"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of normal breast tissue and "
        "infiltrating ductal breast carcinomas by tumor subtype"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    disease = row["disease"]
    if disease == "normal":
        return "normal breast tissue"
    if disease == "tumor":
        subtype = row["Source"].split(" tumor")[0]
        return "invasive ductal carcinoma (" + subtype + ")"
    return "in vitro methylated DNA control"


def methylation_class(row):
    disease = row["disease"]
    if disease == "normal":
        return "CTRL_BR"
    if disease == "tumor":
        subtype = row["Source"].split(" tumor")[0]
        mapping = {
            "luminal A": "BR_CA_HRP",
            "luminal B": "BR_CA_HRP",
            "luminal-HER2": "BR_CA_HER2",
            "HER2": "BR_CA_HER2",
            "triple-negative": "BR_CA_TN",
        }
        return mapping[subtype]
    return None


def sample_site(row):
    return "breast"


def primary_site(row):
    return "breast"


def sample_type(row):
    mapping = {
        "tumor": "primary",
        "normal": "control",
        "none, in vitro methylated DNA control": "control",
    }
    return mapping[row["disease"]]


def material_type(row):
    mapping = {
        "tumor": "tissue",
        "normal": "tissue",
        "none, in vitro methylated DNA control": None,
    }
    return mapping[row["disease"]]


def preservation(row):
    mapping = {
        "tumor": "FROZEN",
        "normal": "FROZEN",
        "none, in vitro methylated DNA control": None,
    }
    return mapping[row["disease"]]


def sex(row):
    return "female"
