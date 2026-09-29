def dataset_id(row):
    return "E-MTAB-5797"


def description(row):
    return (
        "Methylome profiling of human glioblastoma for the GlioTeX panel, "
        "Illumina 450K (E-MTAB-5797)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {"brain": "Brain"}
    return mapping[value]


def primary_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {"brain": "Brain"}
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Characteristics[specimen with known storage state]"]
    mapping = {"frozen sample": "FROZEN"}
    return mapping[value]


def sex(row):
    value = row["Characteristics[sex]"].strip().lower()
    mapping = {"male": "male", "female": "female", "": None}
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    return float(value)
