def dataset_id(row):
    return "GSE211942"


def description(row):
    return "Renal medullary carcinoma methylation cohort, 2022"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Renal medullary carcinoma"


def methylation_class(row):
    return "RCC_SMARCB1"


def sample_site(row):
    return "Kidney"


def primary_site(row):
    return "Kidney"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["tumor grade"]
    mapping = {"RMC grade 4": "G4"}
    return mapping[value]
