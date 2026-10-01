def _is_tumor(row):
    return "tumor" in row["Title"].lower()


def dataset_id(row):
    return "GSE322956"


def description(row):
    return (
        "Paired esophageal squamous cell carcinoma and adjacent "
        "non-tumor esophageal tissue methylation profiling (GSE322956)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_tumor(row):
        return "esophageal squamous cell carcinoma"
    return "adjacent normal esophageal tissue"


def methylation_class(row):
    if _is_tumor(row):
        return "ESO_SCC"
    return "CTRL_ESO"


def sample_site(row):
    return "Esophagus"


def primary_site(row):
    return "Esophagus"


def sample_type(row):
    if _is_tumor(row):
        return "primary"
    return "control"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
