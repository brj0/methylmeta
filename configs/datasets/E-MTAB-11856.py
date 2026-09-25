def dataset_id(row):
    return "E-MTAB-11856"


def description(row):
    return (
        "Keratinocyte cancers and their precursors: basal cell carcinoma, "
        "cutaneous squamous cell carcinoma, actinic keratosis, Bowen disease "
        "and seborrheic keratosis"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "basal cell carcinoma": "BCC",
        "Bowen disease of the skin": "BOWEN",
        "actinic keratosis": "SKIN_AK",
        "seborrheic keratosis": "SKIN_SEBK",
        "squamous cell carcinoma": "SKIN_SCC",
        "squamous cell carcinoma metastasizing": "SKIN_SCC",
        "keratinocyte carcinoma": "SKIN_SCC",
    }
    return mapping[value]


def sample_site(row):
    return "skin"


def primary_site(row):
    return "skin"


def sample_type(row):
    if (
        row["Characteristics[organism part]"] == "metastasis"
        or row["Characteristics[sampling site]"] == "metastasis"
    ):
        return "metastasis"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Characteristics[specimen with known storage state]"]
    mapping = {
        "FFPE": "FFPE",
        "fresh frozen": "FROZEN",
    }
    return mapping[value]
