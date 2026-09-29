def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    if not barcode:
        return None
    return barcode.split("-")[-1][:2]


def _is_control(row):
    return _sample_type_code(row) in {"10", "11", "12", "13", "14"}


def dataset_id(row):
    return "TCGA-KIRP"


def description(row):
    return (
        "TCGA Kidney Renal Papillary Cell Carcinoma (KIRP), TCGA Research "
        "Network"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_control(row):
        return "Normal kidney tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if _is_control(row):
        return "CTRL_REN"
    organ = {
        "Kidney, NOS": "kidney",
        "Bladder, NOS": "bladder",
        "Breast, NOS": "breast",
        "Colon, NOS": "colon",
        "Rectosigmoid junction": "colon",
        "Prostate gland": "prostate",
        "Lymph node, NOS": "lymph node",
        "Skin, NOS": "skin",
        "Head, face or neck, NOS": "head and neck",
        "Lower limb, NOS": "lower limb",
        "Thyroid gland": "thyroid",
        "Other ill-defined sites": None,
        "Not Reported": None,
    }[row["diagnoses.tissue_or_organ_of_origin"]]
    histology = row["diagnoses.primary_diagnosis"]
    mapping = {
        ("kidney", "Papillary renal cell carcinoma"): "RCC_PAP",
        ("kidney", "Papillary adenocarcinoma, NOS"): "RCC_PAP",
        (None, "Papillary adenocarcinoma, NOS"): "RCC_PAP",
        ("kidney", "Clear cell adenocarcinoma, NOS"): "RCC_CC",
        ("kidney", "Not Reported"): None,
        ("bladder", "Transitional cell carcinoma"): "URO_CA",
        ("breast", "Infiltrating duct carcinoma, NOS"): "BR_CA_NST",
        ("breast", "Not Reported"): None,
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
        ("prostate", "Not Reported"): None,
        ("thyroid", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("lymph node", "Follicular lymphoma, NOS"): "FL",
        ("skin", "Melanoma, NOS"): "SKIN_MEL",
        ("head and neck", "Basal cell carcinoma, NOS"): "BCC",
        (None, "Basal cell carcinoma, NOS"): "BCC",
        ("lower limb", "Malignant fibrous histiocytoma"): "UPS",
        (None, "Not Reported"): None,
    }
    return mapping.get((organ, histology))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    if value in {None, "Not Reported"}:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    if value in {None, "Not Reported"}:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "01": "primary",
        "02": "recurrence",
        "03": "primary",
        "05": "primary",
        "06": "metastasis",
        "07": "metastasis",
        "10": "control",
        "11": "control",
        "12": "control",
        "13": "control",
        "14": "control",
    }
    return mapping.get(_sample_type_code(row))


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["preservation_method"]
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[value]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
