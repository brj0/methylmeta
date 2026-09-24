def dataset_id(row):
    return "E-MTAB-8864"


def description(row):
    return (
        "Methylation profiling of malignant peripheral nerve sheath "
        "tumours and related soft tissue sarcomas"
    )


def sample_id(row):
    # Sentrix-style IDAT basename, e.g. '200550900071_R04C01'.
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "malignant peripheral nerve sheath tumor": "MPNST",
        "malignant peripheral nerve sheath tumor (RT-induced)": "MPNST",
        "malignant peripheral nerve sheath tumor (epithelioid)": "MPNST",
        "melanoma": "MEL",
        "sarcoma, NOS": None,
        "spindle cell rhabdomyosarcoma (MYOD1 mutant)": "RMS_MYOD1",
        "undifferentiated pleomorphic sarcoma": "UPS",
    }
    # 'sarcoma, NOS' has no valid WHO methylation class, and any
    # unexpected diagnosis is mapped to None (unclassified), never
    # passed through unchanged.
    return mapping.get(value)


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
    mapping = {"male": "male", "female": "female"}
    return mapping.get(value)


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = str(value).strip()
    if not value:
        return None
    return float(value)
