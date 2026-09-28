def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    if not barcode:
        return None
    return barcode.split("-")[-1][:2]


def _is_normal(row):
    return _sample_type_code(row) == "11"


def dataset_id(row):
    return "TCGA-COAD"


def description(row):
    return "TCGA Colon Adenocarcinoma (COAD), Cancer Genome Atlas Network 2012"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_normal(row):
        return "Normal colon tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if _is_normal(row):
        return "CTRL_COL"
    organ_map = {
        "Ascending colon": "colon",
        "Cecum": "colon",
        "Colon, NOS": "colon",
        "Descending colon": "colon",
        "Hepatic flexure of colon": "colon",
        "Rectosigmoid junction": "colon",
        "Rectum, NOS": "colon",
        "Sigmoid colon": "colon",
        "Splenic flexure of colon": "colon",
        "Transverse colon": "colon",
        # missing site: fall back to the cohort organ
        "Not Reported": "colon",
        "Kidney, NOS": "kidney",
        "Liver": "liver",
        "Prostate gland": "prostate",
        "Uterus, NOS": "uterus",
        "Blood": "blood",
        "Skin, NOS": "skin",
        "Skin of scalp and neck": "skin",
        "Eyelid": "skin",
        "Head, face or neck, NOS": "head_neck",
        "Gum, NOS": "head_neck",
        "Larynx, NOS": "head_neck",
        "Breast, NOS": "breast",
        "Lung, NOS": "lung",
        "Stomach, NOS": "stomach",
        "Thyroid gland": "thyroid",
        "Other ill-defined sites": "other",
    }
    # ICD-O-3 morphology code -> readable name
    morph_label = {
        "8140/3": "Adenocarcinoma, NOS",
        "8480/3": "Mucinous adenocarcinoma",
        "8260/3": "Papillary adenocarcinoma, NOS",
        "8574/3": "Adenocarcinoma with mixed subtypes",
        "8255/3": "Adenocarcinoma with neuroendocrine differentiation",
        "8010/3": "Carcinoma, NOS",
        "8010/2": "Carcinoma in situ, NOS",
        "8560/3": "Adenosquamous carcinoma",
        "8070/3": "Squamous cell carcinoma, NOS",
        "8083/3": "Basaloid squamous cell carcinoma",
        "8310/3": "Clear cell carcinoma",
        "8090/3": "Basal cell carcinoma, NOS",
        "8720/3": "Melanoma, NOS",
        "9732/3": "Plasma cell myeloma",
        "9650/3": "Hodgkin lymphoma, NOS",
        "Not Reported": "Not Reported",
    }
    class_map = {
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("colon", "Mucinous adenocarcinoma"): "CR_CA",
        ("colon", "Papillary adenocarcinoma, NOS"): "CR_CA",
        ("colon", "Adenocarcinoma with mixed subtypes"): "CR_CA",
        (
            "colon",
            "Adenocarcinoma with neuroendocrine differentiation",
        ): "CR_CA",
        ("colon", "Carcinoma, NOS"): "CR_CA",
        ("colon", "Carcinoma in situ, NOS"): "CR_CA",
        ("colon", "Adenosquamous carcinoma"): "CR_CA",
        ("colon", "Not Reported"): None,
        ("kidney", "Clear cell carcinoma"): "RCC_CC",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
        ("uterus", "Adenocarcinoma, NOS"): "ENDOM_CA",
        # liver adenocarcinoma, NOS is not distinguishable further
        ("liver", "Adenocarcinoma, NOS"): None,
        ("skin", "Melanoma, NOS"): "MEL",
        ("skin", "Basaloid squamous cell carcinoma"): "SKIN_SCC",
        ("head_neck", "Basal cell carcinoma, NOS"): "BCC",
        ("blood", "Plasma cell myeloma"): "MYELOMA",
        ("blood", "Hodgkin lymphoma, NOS"): "HODG",
        ("other", "Squamous cell carcinoma, NOS"): "SCC",
    }
    organ = organ_map.get(row["diagnoses.tissue_or_organ_of_origin"])
    histology = morph_label.get(row["diagnoses.morphology"])
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
    mapping = {"Not Reported": None, "Unknown": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "01": "primary",
        "02": "recurrence",
        "06": "metastasis",
        "11": "control",
    }
    return mapping.get(_sample_type_code(row))


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    mapping = {"Not Reported": None, "Unknown": None}
    return mapping.get(value)


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
