def dataset_id(row):
    return "GSE292314"


def description(row):
    return "A cellular epigenetic classification system for glioblastoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Glioblastoma"


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    if "FFPE" in row["Title"]:
        return "FFPE"
    return "FROZEN"


def tumor_grade(row):
    return "G4"
