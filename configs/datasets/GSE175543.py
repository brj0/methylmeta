def dataset_id(row):
    return "GSE175543"


def description(row):
    return "Pediatric radiation-induced high-grade gliomas (RIG cohort)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "HGG"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return "high-grade"
