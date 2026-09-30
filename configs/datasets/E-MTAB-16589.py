def dataset_id(row):
    return "E-MTAB-16589"


def description(row):
    return (
        "Global epigenomic profiling of corticotroph pituitary "
        "neuroendocrine tumors"
    )


def sample_id(row):
    # Array Data File holds the full IDAT filename, e.g. 12345_C010_Grn.idat
    value = row["Array Data File"]
    suffix = "_Grn.idat" if value.endswith("_Grn.idat") else "_Red.idat"
    return value[: -len(suffix)]


def diagnosis(row):
    mapping = {
        "Corticotroph PitNET": "Corticotroph PitNET",
        "Non-neoplastic": "Non-neoplastic adenohypophysis",
    }
    return mapping[row["Characteristics[disease]"]]


def methylation_class(row):
    mapping = {
        "Corticotroph PitNET": "PIT_AD_ACTH",
        "Non-neoplastic": "CTRL_ADENOPIT",
    }
    return mapping[row["Characteristics[disease]"]]


def sample_site(row):
    mapping = {
        "Adenohypophysis": "Adenohypophysis",
        "Sellar neoplasm": "Sellar region",
    }
    return mapping[row["Characteristics[organism part]"]]


def primary_site(row):
    return "Pituitary gland"


def sample_type(row):
    mapping = {"Tumor": "primary", "Control": "control"}
    return mapping[row["Characteristics[sampling site]"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    return float(value)
