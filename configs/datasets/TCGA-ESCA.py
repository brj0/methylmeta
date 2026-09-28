def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    if not barcode:
        return None
    return barcode.split("-")[-1][:2]


def dataset_id(row):
    return "TCGA-ESCA"


def description(row):
    return (
        "TCGA Esophageal Carcinoma (ESCA), Cancer Genome Atlas Research "
        "Network 2017"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    parts = [
        row["diagnoses.primary_diagnosis"],
        row["diagnoses.morphology"],
        row["diagnoses.classification_of_tumor"],
    ]
    return " | ".join(parts)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Adenocarcinoma, NOS": "ESO_ADCA",
        "Basal cell carcinoma, NOS": "BCC",
        "Basaloid squamous cell carcinoma": "ESO_SCC",
        "Malignant lymphoma, non-Hodgkin, NOS": "DLBCL",
        "Mucinous adenocarcinoma": "ESO_ADCA",
        "Multiple myeloma": "MYELOMA",
        "Not Reported": None,
        "Squamous cell carcinoma, NOS": "ESO_SCC",
        "Squamous cell carcinoma, keratinizing, NOS": "ESO_SCC",
        "Tubular adenocarcinoma": "ESO_ADCA",
    }
    if _sample_type_code(row) == "11":
        return "CTRL_ESO"
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None, "Esophagus, NOS": "Esophagus"}
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
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "GX": None,
        None: None,
    }
    return mapping[value]


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
