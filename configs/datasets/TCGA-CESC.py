def _sample_type_code(row):
    barcode = row["sample_submitter_id"]
    return barcode.split("-")[-1][:2]


def dataset_id(row):
    return "TCGA-CESC"


def description(row):
    return (
        "TCGA Cervical Squamous Cell Carcinoma and Endocervical "
        "Adenocarcinoma (CESC), TCGA 2017"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _sample_type_code(row) == "11":
        return "Normal cervical tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if _sample_type_code(row) == "11":
        return "CTRL_CERV"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Squamous cell carcinoma, NOS": "CERV_SCC",
        "Squamous cell carcinoma, keratinizing, NOS": "CERV_SCC",
        "Squamous cell carcinoma, large cell, nonkeratinizing, NOS": (
            "CERV_SCC"
        ),
        "Basaloid squamous cell carcinoma": "CERV_SCC",
        "Papillary squamous cell carcinoma": "CERV_SCC",
        "Adenocarcinoma, NOS": "CERV_ADCA",
        "Adenocarcinoma, endocervical type": "CERV_ADCA",
        "Mucinous adenocarcinoma": "CERV_ADCA",
        "Mucinous adenocarcinoma, endocervical type": "CERV_ADCA",
        "Endometrioid adenocarcinoma, NOS": "CERV_ADCA",
        "Adenosquamous carcinoma": "CERV_CA",
        "Carcinoma, NOS": "CERV_CA",
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None, None: None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {
        "Endocervix": "Cervix uteri",
        "Exocervix": "Cervix uteri",
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping.get(value, value)


def sample_type(row):
    mapping = {
        "01": "primary",
        "02": "recurrence",
        "06": "metastasis",
        "11": "control",
        "12": "control",
    }
    return mapping.get(_sample_type_code(row))


def material_type(row):
    return "tissue"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
