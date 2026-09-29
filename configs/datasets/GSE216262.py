def dataset_id(row):
    return "GSE216262"


def description(row):
    return (
        "Atypical neurofibromas reveal distinct epigenetic features with "
        "proximity to benign peripheral nerve sheath tumor entities"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["revised histological diagnosis (who 2021)"]
    mapping = {
        "ANNUBP": (
            "Atypical neurofibromatous neoplasm of uncertain biologic"
            " potential (ANNUBP)"
        ),
        "PN": "Plexiform neurofibroma",
        "lg MPNST": "Low-grade malignant peripheral nerve sheath tumor",
    }
    if value in mapping:
        return mapping[value]
    return row["initial histological diagnosis"]


def methylation_class(row):
    value = row["revised histological diagnosis (who 2021)"]
    mapping = {
        "ANNUBP": "NFIB_ATY",
        "PN": "NFIB_PLEX",
        "lg MPNST": "MPNST_LG",
        "n.a.": None,
    }
    return mapping[value]


def sample_site(row):
    return row["Source"].replace("biopsy", "").strip(" ,") or None


def primary_site(row):
    return "Peripheral nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["Sex"]


def age(row):
    return float(row["age"])
