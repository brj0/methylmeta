def dataset_id(row):
    return "GSE233603"


def description(row):
    return (
        "High-risk colorectal adenoma (colon polyp) cohort, "
        "Illumina methylation profiling"
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
    if grade == "3" or hgd == "1":
        return "CR_AD_HG"
    if grade in {"1", "2"} or hgd == "0":
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
    mapping = {"1": "G1", "2": "G2", "3": "G3"}
    return mapping.get(str(value))


def sex(row):
    value = row["is_female"]
    if value is None:
        return None
    try:
        return "female" if int(value) == 1 else "male"
    except (TypeError, ValueError):
        return None


def age(row):
    value = row["age"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
