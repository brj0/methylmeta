def dataset_id(row):
    return "GSE67097"


def description(row):
    return (
        "Epigenome analysis of cutaneous squamous cell carcinoma and "
        "location-matched normal skin samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def _is_tumor(row):
    return row["tissue"].endswith("squamous cell carcinoma")


def diagnosis(row):
    if _is_tumor(row):
        return "squamous cell carcinoma"
    return "normal skin"


def methylation_class(row):
    if _is_tumor(row):
        return "SKIN_SCC"
    return "CTRL_SKIN"


def sample_site(row):
    return row["body site"]


def primary_site(row):
    return row["body site"]


def sample_type(row):
    if _is_tumor(row):
        return "primary"
    return "control"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    return row["gender"]
