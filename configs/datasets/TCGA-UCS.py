def dataset_id(row):
    return "TCGA-UCS"


def description(row):
    return "TCGA Uterine Carcinosarcoma (UCS), Cherniack et al. 2017"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {
        "Basal cell carcinoma, NOS": "BCC",
        "Carcinosarcoma, NOS": "UCS",
        "Infiltrating duct carcinoma, NOS": "BR_CA_NST",
        "Intraductal carcinoma, noninfiltrating, NOS": "DCIS",
        "Melanoma, NOS": "MEL",
        "Mesodermal mixed tumor": "UCS",
        "Mullerian mixed tumor": "UCS",
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
    value = mapping.get(value, value)
    if value is None:
        return None
    return value.replace(", NOS", "")


def sample_type(row):
    mapping = {"Primary Tumor": "primary"}
    return mapping[row["sample_type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"OCT": "FROZEN", "Unknown": None}
    return mapping[row["preservation_method"]]


def sex(row):
    return "female"


def age(row):
    value = row["demographic.age_at_index"]
    if value is None:
        return None
    return float(value)
