def dataset_id(row):
    return "GSE298506"


def description(row):
    return (
        "Primary and recurrent myxopapillary ependymoma subtype A "
        "methylation profiles (Hack et al. 2025)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Myxopapillary ependymoma"


def methylation_class(row):
    return "EPN_MPE"


def sample_site(row):
    value = row["localization"]
    mapping = {"not annotated": None}
    return mapping.get(value, value)


def primary_site(row):
    return "Spinal cord"


def sample_type(row):
    mapping = {
        "primary myxopapillary ependymoma subtype A": "primary",
        "recurred myxopapillary ependymoma subtype A": "recurrence",
    }
    return mapping[row["Description"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[row["tissue"]]


def age(row):
    return float(row["age at diagnosis"])
