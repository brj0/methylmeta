def dataset_id(row):
    return "GSE306846"


def description(row):
    return "EBV negative lymphoma and controls"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return str(row["Description"]).split("\n", 1)[0].strip()


def methylation_class(row):
    diagnosis = str(row["Description"]).split("\n", 1)[0].strip()
    if "Control" in diagnosis:
        return "CTRL_LYMPH"
    if "EBV+ DLBCL" in diagnosis:
        return "DLBCL_EBV_POS"
    if "DLBCL" in diagnosis:
        return "DLBCL"
    if diagnosis == "High-grade B-cell lymphoma":
        return "HGBCL"
    return None


def sample_site(row):
    return row["Source"]


def sample_type(row):
    value = row["Description"]

    if "Control" in value:
        return "control"
    if "DLBCL" in value:
        return "primary"
    if value == "High-grade B-cell lymphoma":
        return "primary"
    return None


def preservation(row):
    return "FFPE"


def sex(row):
    return row["Sex"]


def age(row):
    return row["age"]
