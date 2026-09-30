def dataset_id(row):
    return "E-MTAB-8542"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of cutaneous squamous cell "
        "carcinoma and its precursor actinic keratosis"
    )


def sample_id(row):
    # Sentrix-style IDAT basename, e.g. '201503470052_R02C01'.
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "actinic keratosis": "SKIN_AK",
        "cutaneous squamous cell carcinoma": "SKIN_SCC",
    }
    return mapping[row["Characteristics[disease]"]]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "female": "female",
        "male": "male",
    }
    return mapping[row["Characteristics[sex]"].strip().lower()]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    return float(value)
