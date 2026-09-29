def dataset_id(row):
    return "E-MTAB-7490"


def description(row):
    return "Methylation profiling of adult astroblastoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "ASTRO_BL_MN1"


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    return float(row["Characteristics[age]"])
