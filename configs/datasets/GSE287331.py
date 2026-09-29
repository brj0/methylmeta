def dataset_id(row):
    return "GSE287331"


def description(row):
    return (
        "DNA methylation profiles along the tumor proximity axis in "
        "breast cancer: tumor, tumor-adjacent normal, ipsilateral "
        "opposite quadrant, contralateral unaffected breast and healthy "
        "donor breast tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    tissue = row["tissue"]
    if tissue == "TU":
        source = row["Source"]
        if "ILC" in source:
            return "Invasive lobular carcinoma of the breast"
        if "DCIS" in source:
            return "Ductal carcinoma in situ of the breast"
        if "IDC" in source:
            return "Invasive ductal carcinoma of the breast"
        return "Breast carcinoma"
    mapping = {
        "AN": "Tumor-adjacent normal breast tissue",
        "OQ": "Normal breast tissue of the ipsilateral opposite quadrant",
        "CUB": "Normal breast tissue of the contralateral breast",
        "HDB": "Normal breast tissue from a healthy donor",
    }
    return mapping[tissue]


def methylation_class(row):
    tissue = row["tissue"]
    if tissue != "TU":
        return "CTRL_BR"
    source = row["Source"]
    if "ILC" in source:
        return "BR_CA_LOB"
    if "DCIS" in source:
        return "DCIS"
    if "HER2+" in source:
        return "BR_CA_HER2"
    if "ER-" in source and "PgR-" in source and "HER2-" in source:
        return "BR_CA_TN"
    if "ER+" in source or "PgR+" in source:
        return "BR_CA_HRP"
    return "BR_CA"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    mapping = {
        "TU": "primary",
        "AN": "control",
        "OQ": "control",
        "CUB": "control",
        "HDB": "control",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    tokens = row["Source"].split()
    for token in tokens:
        grade = {"I": "G1", "II": "G2", "III": "G3"}.get(token)
        if grade:
            return grade
    return None
