def dataset_id(row):
    return "E-MTAB-12202"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of oral cancer and oral "
        "leukoplakia patients"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    disease = row["Characteristics[disease]"]
    if disease == "normal":
        return "normal oral mucosa"
    if disease == "oral mucosa leukoplakia":
        clinical = row["Characteristics[clinical information]"]
        if clinical:
            return clinical
    return disease


def methylation_class(row):
    disease = row["Characteristics[disease]"]
    if disease == "normal":
        return "CTRL_HN"
    if disease == "oral mucosa leukoplakia":
        clinical = row["Characteristics[clinical information]"] or ""
        if "proliferative verrucous leukoplakia" in clinical.lower():
            return "PVL"
        return "OML"
    if disease == "oral squamous cell carcinoma":
        return "HNSCC"
    return None


def sample_site(row):
    return "oral cavity"


def primary_site(row):
    return "oral cavity"


def sample_type(row):
    mapping = {
        "normal": "control",
        "oral mucosa leukoplakia": "primary",
        "oral squamous cell carcinoma": "primary",
    }
    return mapping[row["Characteristics[disease]"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    return float(row["Characteristics[age]"])
