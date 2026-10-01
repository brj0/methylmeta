def dataset_id(row):
    return "GSE233604"


def description(row):
    return (
        "High-risk baseline colorectal adenoma (colon polyp) cohort, "
        "Avaden Biosciences / Janssen"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if str(row["aden_has_hgd"]) == "1" or str(row["aden_grade"]) == "3":
        return "Colorectal adenoma with high-grade dysplasia"
    return "Colorectal adenoma"


def methylation_class(row):
    grade = str(row["aden_grade"])
    hgd = str(row["aden_has_hgd"])
    if hgd == "1" or grade == "3":
        return "CR_AD_HG"
    if hgd == "0" or grade in {"1", "2"}:
        return "CR_AD_LG"
    return "CR_AD"


def sample_site(row):
    return "Colon"


def primary_site(row):
    return "Colon"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["aden_grade"]
    if value is None:
        return None
    return {"1": "G1", "2": "G2", "3": "G3", "4": "G4"}.get(str(value))


def sex(row):
    value = row["is_female"]
    if value is None:
        return None
    try:
        code = int(float(value))
    except (TypeError, ValueError):
        return None
    return {1: "female", 0: "male"}.get(code)


def age(row):
    value = row["age"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
