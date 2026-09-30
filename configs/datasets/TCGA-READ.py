def dataset_id(row):
    return "TCGA-READ"


def description(row):
    return (
        "TCGA Rectum Adenocarcinoma (READ), Cancer Genome Atlas Network 2012"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal colorectal mucosa"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None, "Unknown": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_COL"
    # site of origin -> organ; unclear sites fall back to the cohort organ
    organ_map = {
        "Colon, NOS": "colon",
        "Rectosigmoid junction": "rectum",
        "Rectum, NOS": "rectum",
        "Connective, subcutaneous and other soft tissues of abdomen": "colorectal",
        "Prostate gland": "prostate",
        "Not Reported": "colorectal",
        "Unknown primary site": "colorectal",
    }
    # ICD-O-3 morphology code -> readable name
    morph_label = {
        "8140/3": "Adenocarcinoma, NOS",
        "8211/3": "Tubular adenocarcinoma",
        "8255/3": "Adenocarcinoma with mixed subtypes",
        "8263/3": "Adenocarcinoma in tubulovillous adenoma",
        "8480/3": "Mucinous adenocarcinoma",
        "Not Reported": "Not Reported",
        "Unknown": "Unknown",
    }
    class_map = {
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("colon", "Tubular adenocarcinoma"): "CR_CA",
        ("colon", "Adenocarcinoma with mixed subtypes"): "CR_CA",
        ("colon", "Adenocarcinoma in tubulovillous adenoma"): "CR_CA",
        ("colon", "Mucinous adenocarcinoma"): "CR_CA",
        ("rectum", "Adenocarcinoma, NOS"): "CR_CA",
        ("rectum", "Tubular adenocarcinoma"): "CR_CA",
        ("rectum", "Adenocarcinoma with mixed subtypes"): "CR_CA",
        ("rectum", "Adenocarcinoma in tubulovillous adenoma"): "CR_CA",
        ("rectum", "Mucinous adenocarcinoma"): "CR_CA",
        ("colorectal", "Adenocarcinoma, NOS"): "CR_CA",
        ("colorectal", "Tubular adenocarcinoma"): "CR_CA",
        ("colorectal", "Adenocarcinoma with mixed subtypes"): "CR_CA",
        ("colorectal", "Adenocarcinoma in tubulovillous adenoma"): "CR_CA",
        ("colorectal", "Mucinous adenocarcinoma"): "CR_CA",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
        # histology not reported: no tumor type can be determined
        ("colon", "Not Reported"): None,
        ("colon", "Unknown"): None,
        ("rectum", "Not Reported"): None,
        ("rectum", "Unknown"): None,
        ("colorectal", "Not Reported"): None,
        ("colorectal", "Unknown"): None,
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    histology = morph_label[row["diagnoses.morphology"]]
    return class_map.get((organ, histology))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown primary site": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "Primary Tumor": "primary",
        "Recurrent Tumor": "recurrence",
        "Solid Tissue Normal": "control",
    }
    return mapping[row["sample_type"]]


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
