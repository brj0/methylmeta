def dataset_id(row):
    return "CGCI-HTMCP-CC"


def description(row):
    return (
        "HIV+ Tumor Molecular Characterization Project - Cervical "
        "Cancer (HTMCP-CC), CGCI"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Squamous cell carcinoma, keratinizing, NOS": "CERV_SCC",
        "Squamous cell carcinoma, nonkeratinizing, NOS": "CERV_SCC",
        "Basaloid squamous cell carcinoma": "CERV_SCC",
        "Papillary squamous cell carcinoma": "CERV_SCC",
        "Warty carcinoma": "CERV_SCC",
        "Lymphoepithelial carcinoma": "CERV_SCC",
        "Adenocarcinoma, NOS": "CERV_ADCA",
        "Adenosquamous carcinoma": "CERV_ASC",
        "Tumor, NOS": "CERV_CA",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    return "Cervix uteri"


def sample_type(row):
    value = row["sample_type"]
    mapping = {"Primary Tumor": "primary"}
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["preservation_method"]
    mapping = {
        "Unknown": None,
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
        "Fresh": "FRESH",
    }
    return mapping.get(value)


def tumor_grade(row):
    value = row["diagnoses.tumor_grade"]
    mapping = {"G1": "G1", "G2": "G2", "G3": "G3"}
    return mapping.get(value)


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
