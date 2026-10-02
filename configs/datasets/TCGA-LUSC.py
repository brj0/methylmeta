def dataset_id(row):
    return "TCGA-LUSC"


def description(row):
    return (
        "TCGA Lung Squamous Cell Carcinoma (LUSC), Cancer Genome Atlas "
        "Research Network 2012"
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
    # organ of the recorded diagnosis; a missing organ falls back to the
    # cohort organ (lung)
    organ_map = {
        "Bladder, NOS": "bladder",
        "Blood": "blood",
        "Breast, NOS": "breast",
        "Cervix uteri": "cervix",
        "Head, face or neck, NOS": "head_neck",
        "Kidney, NOS": "kidney",
        "Lower lobe, lung": "lung",
        "Lung, NOS": "lung",
        "Main bronchus": "lung",
        "Middle lobe, lung": "lung",
        "Nasopharynx, NOS": "nasopharynx",
        "Not Reported": "lung",
        "Overlapping lesion of lung": "lung",
        "Prostate gland": "prostate",
        "Skin, NOS": "skin",
        "Thymus": "thymus",
        "Tongue, NOS": "head_neck",
        "Tonsil, NOS": "head_neck",
        "Upper limb, NOS": "skin",
        "Upper lobe, lung": "lung",
    }
    class_map = {
        # lung primaries (the cohort organ)
        ("lung", "Squamous cell carcinoma, NOS"): "LU_SCC",
        ("lung", "Squamous cell carcinoma, keratinizing, NOS"): "LU_SCC",
        ("lung", "Basaloid squamous cell carcinoma"): "LU_SCC",
        ("lung", "Papillary squamous cell carcinoma"): "LU_SCC",
        (
            "lung",
            "Squamous cell carcinoma, large cell, nonkeratinizing, NOS",
        ): "LU_SCC",
        (
            "lung",
            "Squamous cell carcinoma, small cell, nonkeratinizing",
        ): "LU_SCC",
        ("lung", "Adenosquamous carcinoma"): "LU_ASC",
        ("lung", "Adenocarcinoma, NOS"): "LU_ADCA",
        # histology not further specified
        ("lung", "Not Reported"): None,
        # non-lung primaries stored in the diagnosis records of these cases
        ("bladder", "Transitional cell carcinoma"): "URO_CA",
        ("blood", "Hairy cell leukemia"): "HCL",
        ("breast", "Not Reported"): None,
        ("cervix", "Carcinoma, NOS"): None,
        ("head_neck", "Squamous cell carcinoma, NOS"): "HN_SCC",
        ("head_neck", "Squamous cell carcinoma, clear cell type"): "HN_SCC",
        ("head_neck", "Basal cell carcinoma, NOS"): "BCC",
        ("head_neck", "Lentigo maligna"): "MEL_CSD",
        ("kidney", "Renal cell carcinoma, chromophobe type"): "RCC_CP",
        ("nasopharynx", "Squamous cell carcinoma, NOS"): "NP_CA",
        ("prostate", "Not Reported"): None,
        ("skin", "Basaloid squamous cell carcinoma"): "SKIN_SCC",
        ("skin", "Not Reported"): None,
        ("thymus", "Not Reported"): None,
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    return class_map.get((organ, row["diagnoses.primary_diagnosis"]))


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
