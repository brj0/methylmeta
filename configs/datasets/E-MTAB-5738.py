def dataset_id(row):
    return "E-MTAB-5738"


def description(row):
    return (
        "Methylation profiling of epidermal preparations from healthy "
        "skin, actinic keratosis and cutaneous squamous cell carcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "actinic keratosis": "SKIN_AK",
        "normal": "CTRL_SKIN",
        "squamous cell carcinoma": "SKIN_SCC",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "skin"


def sample_type(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "normal": "control",
        "actinic keratosis": "primary",
        "squamous cell carcinoma": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"
