def dataset_id(row):
    return "TCGA-LUAD"


def description(row):
    return (
        "TCGA Lung Adenocarcinoma (LUAD), Cancer Genome Atlas "
        "Research Network 2014"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal lung tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_LU"
    histology = row["diagnoses.primary_diagnosis"]
    if histology is None or histology == "Not Reported":
        return None
    # recorded site of the diagnosis; a missing site falls back to the
    # cohort organ (lung)
    organ_map = {
        "Bladder, NOS": "bladder",
        "Breast, NOS": "breast",
        "Cervix uteri": "cervix",
        "Colon, NOS": "colon",
        "Endometrium": "uterus",
        "External ear": "skin",
        "Female genital tract, NOS": "female_genital",
        "Head, face or neck, NOS": "head_neck",
        "Kidney, NOS": "kidney",
        "Lower lobe, lung": "lung",
        "Lung, NOS": "lung",
        "Main bronchus": "lung",
        "Middle lobe, lung": "lung",
        "Mouth, NOS": "head_neck",
        "Not Reported": "lung",
        "Overlapping lesion of lung": "lung",
        "Ovary": "ovary",
        "Penis, NOS": "penis",
        "Prostate gland": "prostate",
        "Skin of other and unspecified parts of face": "skin",
        "Spleen": "spleen",
        "Thymus": "thymus",
        "Thyroid gland": "thyroid",
        "Unknown": "lung",
        "Upper limb, NOS": "skin",
        "Upper lobe, lung": "lung",
        "Uterus, NOS": "uterus",
        "Vulva, NOS": "vulva",
        None: "lung",
    }
    class_map = {
        # lung primaries (the cohort organ)
        ("lung", "Adenocarcinoma, NOS"): "LU_ADCA",
        ("lung", "Adenocarcinoma with mixed subtypes"): "LU_ADCA",
        ("lung", "Acinar cell carcinoma"): "LU_NONMUC_ADCA",
        ("lung", "Bronchio-alveolar carcinoma, mucinous"): "LU_MUC_ADCA",
        ("lung", "Bronchiolo-alveolar adenocarcinoma, NOS"): "LU_ADCA",
        (
            "lung",
            "Bronchiolo-alveolar carcinoma, non-mucinous",
        ): "LU_NONMUC_ADCA",
        ("lung", "Carcinoid tumor, NOS"): "LU_NET",
        ("lung", "Mucinous adenocarcinoma"): "LU_MUC_ADCA",
        ("lung", "Papillary adenocarcinoma, NOS"): "LU_NONMUC_ADCA",
        ("lung", "Signet ring cell carcinoma"): "LU_ADCA",
        ("lung", "Solid carcinoma, NOS"): "LU_ADCA",
        ("lung", "Squamous cell carcinoma, NOS"): "LU_SCC",
        # no lineage or no organ-specific entity discernible
        ("lung", "Carcinoma in situ, NOS"): None,
        ("lung", "Clear cell adenocarcinoma, NOS"): None,
        ("lung", "Clear cell carcinoma"): None,
        ("lung", "Medullary carcinoma, NOS"): None,
        # entities that name their organ, also relevant when the recorded
        # site is missing
        ("lung", "Basal cell carcinoma, NOS"): "BCC",
        ("lung", "Endometrioid adenocarcinoma, NOS"): "ENDOM_EC",
        ("lung", "Granulosa cell tumor, malignant"): "GRAN_ADULT",
        ("lung", "Hodgkin lymphoma, NOS"): "HODG",
        ("lung", "Infiltrating duct carcinoma, NOS"): "BR_CA_NST",
        ("lung", "Invasive micropapillary carcinoma"): "LU_NONMUC_ADCA",
        ("lung", "Papillary transitional cell carcinoma"): "URO_CA",
        # non-lung primaries stored in the diagnosis records of these cases
        ("bladder", "Papillary transitional cell carcinoma"): "URO_CA",
        ("breast", "Adenocarcinoma, NOS"): "BR_CA_NST",
        ("breast", "Infiltrating duct carcinoma, NOS"): "BR_CA_NST",
        ("breast", "Invasive micropapillary carcinoma"): "BR_CA_MICROPAP",
        ("breast", "Medullary carcinoma, NOS"): "BR_CA_NST",
        ("breast", "Mucinous adenocarcinoma"): "BR_CA_MUC",
        ("cervix", "Adenocarcinoma, NOS"): "CERV_ADCA",
        ("cervix", "Clear cell adenocarcinoma, NOS"): "CERV_HPVI_CC",
        ("cervix", "Endometrioid adenocarcinoma, NOS"): "CERV_ADCA",
        ("cervix", "Mucinous adenocarcinoma"): "CERV_ADCA",
        ("cervix", "Squamous cell carcinoma, NOS"): "CERV_SCC",
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("colon", "Mucinous adenocarcinoma"): "CR_CA",
        ("colon", "Signet ring cell carcinoma"): "CR_CA",
        # site too vague to pick a female genital entity
        ("female_genital", "Adenocarcinoma, NOS"): None,
        ("female_genital", "Carcinoma in situ, NOS"): None,
        ("female_genital", "Granulosa cell tumor, malignant"): "GRAN_ADULT",
        # basal cell carcinoma is a skin entity of the head/face region
        ("head_neck", "Basal cell carcinoma, NOS"): "BCC",
        ("head_neck", "Squamous cell carcinoma, NOS"): "HN_SCC",
        ("kidney", "Adenocarcinoma, NOS"): "RCC",
        ("kidney", "Clear cell adenocarcinoma, NOS"): "RCC_CC",
        ("kidney", "Clear cell carcinoma"): "RCC_CC",
        ("ovary", "Adenocarcinoma, NOS"): "OVA_CA",
        ("ovary", "Clear cell adenocarcinoma, NOS"): "OVA_CCC",
        ("ovary", "Clear cell carcinoma"): "OVA_CCC",
        ("ovary", "Endometrioid adenocarcinoma, NOS"): "OVA_ENDOID_CA",
        ("ovary", "Granulosa cell tumor, malignant"): "GRAN_ADULT",
        ("penis", "Squamous cell carcinoma, NOS"): "PEN_SCC_NOS",
        ("prostate", "Acinar cell carcinoma"): "PROS_ACIN",
        ("prostate", "Adenocarcinoma, NOS"): "PROS_ADCA",
        ("prostate", "Squamous cell carcinoma, NOS"): "PROS_SCC",
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("skin", "Squamous cell carcinoma, NOS"): "SKIN_SCC",
        ("spleen", "Hodgkin lymphoma, NOS"): "HODG",
        ("thymus", "Carcinoid tumor, NOS"): "THYM_NET",
        ("thymus", "Squamous cell carcinoma, NOS"): "THYM_CA",
        ("thyroid", "Medullary carcinoma, NOS"): "MTC",
        ("thyroid", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("uterus", "Adenocarcinoma, NOS"): "ENDOM_CA",
        ("uterus", "Clear cell adenocarcinoma, NOS"): "ENDOM_CCC",
        ("uterus", "Clear cell carcinoma"): "ENDOM_CCC",
        ("uterus", "Endometrioid adenocarcinoma, NOS"): "ENDOM_EC",
        ("vulva", "Squamous cell carcinoma, NOS"): "VULV_SCC",
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    return class_map.get((organ, histology))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown": None}
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


def preservation(row):
    mapping = {"FFPE": "FFPE", "OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
