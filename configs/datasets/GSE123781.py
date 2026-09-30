def dataset_id(row):
    return "GSE123781"


def description(row):
    return (
        "DNA methylation profiling of oral squamous cell carcinoma, oral "
        "lichen planus and normal oral mucosa (Illumina 450k)"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    mapping = {
        "OSCC": "oral squamous cell carcinoma",
        "OLP": "oral lichen planus",
        "control": "normal oral mucosa",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    # HPV status is not recorded, so OSCC is classified as the broader
    # head and neck squamous cell carcinoma class. Oral lichen planus is
    # a premalignant condition with its own class; controls are normal
    # head and neck mucosa.
    mapping = {
        "OSCC": "HNSCC",
        "OLP": "OLP",
        "control": "CTRL_HN",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Oral cavity"


def primary_site(row):
    if row["Source"] == "OSCC":
        return "Oral cavity"
    return None


def sample_type(row):
    # OLP is an inflammatory premalignant lesion, not a tumor sample.
    mapping = {
        "OSCC": "primary",
        "OLP": None,
        "control": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age [years]"]
    if value is None:
        return None
    return float(value)
