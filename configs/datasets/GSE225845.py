def dataset_id(row):
    return "GSE225845"


def description(row):
    return (
        "NCI-Maryland Breast Cancer Cohort: neighborhood deprivation and "
        "DNA methylation in breast tissue (2023)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "tumor": "Breast carcinoma",
        "normal": "Normal breast tissue",
        "adj_norm": "Normal breast tissue",
    }
    return mapping[row["sample type"]]


def methylation_class(row):
    sample = row["sample type"]
    if sample in {"normal", "adj_norm"}:
        return "CTRL_BR"
    mapping = {
        "HER2+": "BR_CA_HER2",
        "HR+": "BR_CA_HRP",
        "TNBC": "BR_CA_TN",
    }
    return mapping.get(row["molecular subtype"], "BR_CA")


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    mapping = {
        "tumor": "primary",
        "normal": "control",
        "adj_norm": "control",
    }
    return mapping[row["sample type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    mapping = {
        "1": "G1",
        "2": "G2",
        "3": "G3",
        "Low grade": "low-grade",
    }
    return mapping.get(row["grade"])


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping.get(row["Sex"])


def age(row):
    value = row["age_at_surgery"]
    if value is None:
        return None
    return float(value)
