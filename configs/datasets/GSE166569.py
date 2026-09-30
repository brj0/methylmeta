def dataset_id(row):
    return "GSE166569"


def description(row):
    return "DNA methylation profiling of astroblastoma-like tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histological type"]


def methylation_class(row):
    return "ASTRO_BL_MN1"


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


def sex(row):
    return row["gender"]
