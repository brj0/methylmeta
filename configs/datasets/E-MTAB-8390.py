def dataset_id(row):
    return "E-MTAB-8390"


def description(row):
    return (
        "Methylation profiling of pediatric histologically defined "
        "anaplastic pilocytic astrocytoma"
    )


def sample_id(row):
    # Sentrix-style IDAT basename, e.g. '203219730026_R01C01'.
    return row["Sample_ID"]


def diagnosis(row):
    # All samples are pediatric tumors with the histological diagnosis of
    # anaplastic pilocytic astrocytoma (raw disease column: astrocytoma).
    return "anaplastic pilocytic astrocytoma"


def methylation_class(row):
    return "ANA_PA"


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"].strip().lower()
    mapping = {
        "female": "female",
        "male": "male",
    }
    return mapping[value]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    return float(value)
