def _organ(row):
    mapping = {
        "Lung, NOS": "lung",
        "Kidney, NOS": "kidney",
        "Uterus, NOS": "uterus",
        "Skin, NOS": "skin",
        "Pancreas, NOS": "pancreas",
        "Stomach, NOS": "stomach",
        "Colon, NOS": "colon",
        "Breast, NOS": "breast",
        "Urethra": "urethra",
        "Hematopoietic system, NOS": "bone marrow",
        "Brain, NOS": "brain",
        "Cerebrum": "brain",
        "Frontal lobe": "brain",
        "Occipital lobe": "brain",
        "Parietal lobe": "brain",
        "Temporal lobe": "brain",
        "Larynx, NOS": "head and neck",
        "Tongue, NOS": "head and neck",
        "Floor of mouth, NOS": "head and neck",
        "Oropharynx, NOS": "head and neck",
        "Gum, NOS": "head and neck",
        "Lip, NOS": "head and neck",
        "Cheek mucosa": "head and neck",
        "Base of tongue, NOS": "head and neck",
        "Tonsil, NOS": "head and neck",
        "Head, face or neck, NOS": "head and neck",
        "Overlapping lesion of lip, oral cavity and pharynx": "head and neck",
        "Unknown": None,
    }
    return mapping[row["diagnoses.tissue_or_organ_of_origin"]]


def dataset_id(row):
    return "CPTAC-3"


def description(row):
    return "Prospective pan-cancer proteogenomics cohort (CPTAC)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    normal_diagnosis = {
        "lung": "Normal lung tissue",
        "kidney": "Normal kidney tissue",
        "pancreas": "Normal pancreas tissue",
        "uterus": "Normal endometrium",
        "skin": "Normal skin",
        "brain": "Normal brain tissue",
        "stomach": "Normal stomach tissue",
        "head and neck": "Normal head and neck mucosa",
        "colon": "Normal colon",
        "breast": "Normal breast tissue",
    }
    if row["sample_type"] == "Solid Tissue Normal":
        return normal_diagnosis.get(_organ(row))
    value = row["diagnoses.primary_diagnosis"]
    if value == "Unknown":
        return None
    return value


def methylation_class(row):
    organ = _organ(row)
    if row["sample_type"] == "Solid Tissue Normal":
        control_mapping = {
            "lung": "CTRL_LU",
            "kidney": "CTRL_REN",
            "pancreas": "CTRL_PAN",
            "uterus": "CTRL_ENDOM",
            "skin": "CTRL_SKIN",
            "brain": "CTRL_BRAIN_GBM",
            "stomach": "CTRL_GAST",
            "head and neck": "CTRL_HN",
            "colon": "CTRL_COL",
            "breast": "CTRL_BR",
        }
        return control_mapping.get(organ)
    class_mapping = {
        ("bone marrow", "Acute myeloid leukemia, NOS"): "AML",
        ("brain", "Astrocytoma, NOS"): "ASTRO_IDH",
        ("brain", "Glioblastoma"): "GBM_NOS",
        ("brain", "Gliosarcoma"): "GBM_NOS",
        # cohort gliomas NOS are grade G4
        ("brain", "Glioma, NOS"): "HGG",
        ("brain", "Oligodendroglioma, NOS"): "OLIGO_IDH",
        ("brain", "Oligodendroglioma, anaplastic"): "OLIGO_IDH_ANA",
        ("brain", "Unknown"): None,
        ("breast", "Intraductal carcinoma, NOS"): "DCIS",
        ("colon", "Carcinoma, NOS"): "CR_CA",
        ("head and neck", "Squamous cell carcinoma, NOS"): "HNSCC",
        ("kidney", "Angiomyolipoma"): "REN_PEC",
        ("kidney", "Benign cystic nephroma"): "PED_CYSTNEPH",
        (
            "kidney",
            "Hereditary leiomyomatosis & RCC-associated renal cell carcinoma",
        ): "RCC_FH",
        ("kidney", "Oncocytoma"): "REN_ONC",
        ("kidney", "Papillary renal cell carcinoma"): "RCC_PAP",
        ("kidney", "Renal cell carcinoma, NOS"): "RCC",
        ("kidney", "Renal cell carcinoma, chromophobe type"): "RCC_CP",
        ("kidney", "Unknown"): None,
        ("kidney", "Urothelial carcinoma, NOS"): "URO_CA",
        ("lung", "Adenocarcinoma, NOS"): "LU_ADCA",
        ("lung", "Squamous cell carcinoma, NOS"): "LU_SCC",
        ("pancreas", "Infiltrating duct carcinoma, NOS"): "PAN_CA",
        ("skin", "Malignant melanoma, NOS"): "SKIN_MEL",
        ("stomach", "Adenocarcinoma, NOS"): "GAST_ADCA",
        ("urethra", "Malignant melanoma, NOS"): "MUC_MEL",
        ("uterus", "Adenocarcinoma, NOS"): "ENDOM_EC",
        ("uterus", "Endometrioid adenocarcinoma, NOS"): "ENDOM_EC",
        # adenosquamous carcinoma of unknown organ of origin
        (None, "Adenosquamous carcinoma"): None,
    }
    return class_mapping.get((organ, row["diagnoses.primary_diagnosis"]))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    if value in {None, "Unknown"}:
        return None
    return value.replace(", NOS", "")


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    if value in {None, "Unknown"}:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {
        "Primary Tumor": "primary",
        "Metastatic": "metastasis",
        "Recurrent Tumor": "recurrence",
        "Solid Tissue Normal": "control",
        "Primary Blood Derived Cancer - Bone Marrow": "primary",
        "Primary Blood Derived Cancer - Peripheral Blood": "primary",
        None: None,
    }
    return mapping[row["sample_type"]]


def material_type(row):
    mapping = {
        "Primary Tumor": "tissue",
        "Metastatic": "tissue",
        "Recurrent Tumor": "tissue",
        "Solid Tissue Normal": "tissue",
        "Primary Blood Derived Cancer - Bone Marrow": "blood",
        "Primary Blood Derived Cancer - Peripheral Blood": "blood",
        None: "tissue",
    }
    return mapping[row["sample_type"]]


def preservation(row):
    mapping = {
        "Frozen": "FROZEN",
        "Snap Frozen": "FROZEN",
    }
    return mapping[row["preservation_method"]]


def tumor_grade(row):
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "G4": "G4",
        "High Grade": "high-grade",
        "GX": None,
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping[row["diagnoses.tumor_grade"]]


def age(row):
    years = row["demographic.age_at_index"]
    days = row["diagnoses.age_at_diagnosis"]
    if years is not None:
        return float(years)
    if days is None:
        return None
    return round(float(days) / 365.25, 1)
