def dataset_id(row):
    return "TCGA-LGG"


def description(row):
    return "TCGA Brain Lower Grade Glioma (LGG), Brat 2015"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    organ_mapping = {
        "Brain, NOS": "brain",
        "Cerebrum": "brain",
        "Frontal lobe": "brain",
        "Occipital lobe": "brain",
        "Parietal lobe": "brain",
        "Temporal lobe": "brain",
        "Skin of scalp and neck": "skin",
        "Thyroid gland": "thyroid",
        "Not Reported": None,
    }
    class_mapping = {
        ("brain", "Astrocytoma, NOS"): "ASTRO_IDH",
        ("brain", "Astrocytoma, anaplastic"): "ASTRO_IDH_HG",
        ("brain", "Mixed glioma"): "LGG",
        ("brain", "Oligodendroglioma, NOS"): "OLIGO_IDH",
        ("brain", "Oligodendroglioma, anaplastic"): "OLIGO_IDH_ANA",
        ("brain", "Not Reported"): None,
        ("skin", "Basal cell carcinoma, NOS"): "BCC",
        ("thyroid", "Papillary carcinoma, NOS"): "THYR_PTC",
        (None, "Astrocytoma, NOS"): "ASTRO_IDH",
        (None, "Astrocytoma, anaplastic"): "ASTRO_IDH_HG",
        (None, "Mixed glioma"): "LGG",
        (None, "Oligodendroglioma, NOS"): "OLIGO_IDH",
        (None, "Oligodendroglioma, anaplastic"): "OLIGO_IDH_ANA",
        (None, "Not Reported"): None,
    }
    organ = organ_mapping[row["diagnoses.tissue_or_organ_of_origin"]]
    histology = row["diagnoses.primary_diagnosis"]
    return class_mapping.get((organ, histology))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {
        "Nervous system, NOS": "Nervous system",
        "Not Reported": None,
    }
    return mapping[value]


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None}
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    value = row["sample_type"]
    mapping = {
        "Primary Tumor": "primary",
        "Recurrent Tumor": "recurrence",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["preservation_method"]
    mapping = {
        "OCT": "FROZEN",
        "Unknown": None,
    }
    return mapping[value]


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    mapping = {
        "G2": "G2",
        "G3": "G3",
        None: None,
    }
    return mapping[value]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
