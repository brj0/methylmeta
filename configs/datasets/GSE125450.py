def dataset_id(row):
    return "GSE125450"


def description(row):
    return "DNA methylation analysis of astroblastomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {"astroblastomas": "Astroblastoma"}
    return mapping[value]


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
