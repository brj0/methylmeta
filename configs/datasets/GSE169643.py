def dataset_id(row):
    return "GSE169643"


def description(row):
    return (
        "Extranodal NK/T-cell lymphoma (ENKTL) tumors, normal NK-cell "
        "developmental stages and ENKTL PDX models"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["sample type"]
    if value.startswith("NKDI_Stage_"):
        stage = value[len("NKDI_Stage_") :]
        return "normal NK cell developmental intermediate, stage " + stage
    mapping = {
        "ENKTL": "Extranodal NK/T-cell lymphoma",
        "NKLGL": "NK-cell large granular lymphocytic leukemia",
        "HSPC": "normal hematopoietic stem and progenitor cells",
    }
    return mapping[value]


def methylation_class(row):
    value = row["sample type"]
    if value == "ENKTL":
        return "ENKTL"
    if value == "NKLGL":
        return "NK_LGL"
    mapping = {
        "Tonsil": "CTRL_LYMPH",
        "Peripheral blood": "CTRL_BLOOD",
        "Bone marrow": "CTRL_MARROW",
    }
    return mapping[row["Source"]]


def sample_site(row):
    source = row["Source"]
    if source != "Tumor":
        return source
    title = row["Title"]
    if "_SPL" in title:
        return "spleen"
    if "_BM" in title:
        return "bone marrow"
    return None


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Normal": "control",
    }
    return mapping[row["disease state"]]


def material_type(row):
    mapping = {
        "Tumor": "tissue",
        "Tonsil": "tissue",
        "Peripheral blood": "blood",
        "Bone marrow": "blood",
    }
    return mapping[row["Source"]]


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "fresh-frozen": "FROZEN",
    }
    return mapping[row["dna isolation type"]]
