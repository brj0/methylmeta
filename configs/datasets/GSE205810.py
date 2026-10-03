def dataset_id(row):
    return "GSE205810"


def description(row):
    return "Methylome analysis of high-grade glioma (HGG_F) samples"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "High-grade glioma"


def methylation_class(row):
    return "HGG_F"


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "Brain"


def sample_type(row):
    value = row["primary_recurrence"]
    mapping = {"p": "primary", "r": "recurrence"}
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    return row["Sex"]
