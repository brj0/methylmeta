def dataset_id(row):
    return "TCGA-SARC"


def description(row):
    return (
        "TCGA adult soft tissue sarcoma cohort (SARC), "
        "Cancer Genome Atlas Research Network 2017"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "Normal soft tissue"
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    if row["sample_type"] == "Solid Tissue Normal":
        return "CTRL_SOFT"
    value = row["diagnoses.primary_diagnosis"]
    organ = row["diagnoses.tissue_or_organ_of_origin"]
    organ_class = {
        ("Uterus, NOS", "Leiomyosarcoma, NOS"): "UT_LMS",
        ("Myometrium", "Leiomyosarcoma, NOS"): "UT_LMS",
        ("Isthmus uteri", "Myxoid leiomyosarcoma"): "UT_LMS",
        ("Prostate gland", "Adenocarcinoma, NOS"): "PROS_ADCA",
        ("Uterus, NOS", "Adenocarcinoma, NOS"): "ENDOM_CA",
        ("Cervix uteri", "Squamous cell carcinoma, NOS"): "CERV_SCC",
        ("Kidney, NOS", "Carcinoma, NOS"): "RCC",
    }
    if (organ, value) in organ_class:
        return organ_class[(organ, value)]
    mapping = {
        "Leiomyosarcoma, NOS": "LMS",
        "Myxoid leiomyosarcoma": "LMS",
        "Dedifferentiated liposarcoma": "LPS_DD",
        "Liposarcoma, well differentiated": "LPS_WD",
        "Pleomorphic liposarcoma": "LPS_PLEO",
        "Liposarcoma, NOS": "LPS",
        "Undifferentiated sarcoma": "UPS",
        "Malignant fibrous histiocytoma": "UPS",
        "Giant cell sarcoma": "UPS",
        "Fibromyxosarcoma": "MFS",
        "Malignant peripheral nerve sheath tumor": "MPNST",
        "Synovial sarcoma, NOS": "SYNSARC",
        "Synovial sarcoma, spindle cell": "SYNSARC",
        "Synovial sarcoma, biphasic": "SYNSARC",
        "Sarcoma, NOS": "SARC_NOS",
        "Aggressive fibromatosis": "DESMOID",
        "Abdominal fibromatosis": "DESMOID",
        "Adenocarcinoma, NOS": None,
        "Carcinoma, NOS": None,
        "Squamous cell carcinoma, NOS": "SCC",
        "Basal cell carcinoma, NOS": "BCC",
        "Melanoma, NOS": "MEL",
        "Thecoma, NOS": "THEC",
        "Malignant lymphoma, small B lymphocytic, NOS": None,
        "Intraductal carcinoma, noninfiltrating, NOS": "DCIS",
        "Transitional cell papilloma, inverted, NOS": None,
        "Not Reported": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown": None}
    return mapping.get(value, value)


def sample_type(row):
    value = row["sample_type"]
    mapping = {
        "Primary Tumor": "primary",
        "Metastatic": "metastasis",
        "Recurrent Tumor": "recurrence",
        "Solid Tissue Normal": "control",
    }
    return mapping[value]


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
