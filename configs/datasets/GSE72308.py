def dataset_id(row):
    return "GSE72308"


def description(row):
    return "Breast tumors from three clinical cohorts (methylation profiling)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Breast tumor"


def methylation_class(row):
    subtype_ihc = {
        "Basal": "BR_CA_TN",
        "HER2": "BR_CA_HER2",
        "LumA": "BR_CA_HRP",
        "LumB": "BR_CA_HRP",
    }
    subtype_pam50 = {
        "Basal": "BR_CA_TN",
        "Her2": "BR_CA_HER2",
        "LumA": "BR_CA_HRP",
        "LumB": "BR_CA_HRP",
    }
    value = row["subtype_ihc"]
    if value in subtype_ihc:
        return subtype_ihc[value]
    return subtype_pam50.get(row["subtype_pam50"], "BR_CA")


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    mapping = {"1": "G1", "2": "G2", "3": "G3"}
    return mapping.get(row["grade"])


def age(row):
    value = row["age_diagnosis"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
