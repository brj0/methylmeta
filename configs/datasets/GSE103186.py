def dataset_id(row):
    return "GSE103186"


def description(row):
    return (
        "Genomic and epigenomic profiling of high-risk gastric intestinal "
        "metaplasia, Huang 2018"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # Full diagnosis of the sampled gastric mucosa (normal or metaplastic).
    return row["tissue"]


def methylation_class(row):
    mapping = {
        "intestinal metaplasia biopsy from gastric antrum": "GAST_IM",
        "intestinal metaplasia biopsy from gastric body": "GAST_IM",
        "intestinal metaplasia biopsy from gastric cardia": "GAST_IM",
        "mild intestinal metaplasia biopsy from gastric antrum": "GAST_IM",
        "normal biopsy from gastric antrum": "CTRL_GAST",
        "normal biopsy from gastric body": "CTRL_GAST",
        "normal biopsy from gastric cardia": "CTRL_GAST",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    value = row["tissue"]
    if "antrum" in value:
        return "Gastric antrum"
    if "body" in value:
        return "Gastric body"
    if "cardia" in value:
        return "Gastric cardia"
    return None


def primary_site(row):
    return "Stomach"


def sample_type(row):
    mapping = {
        "normal biopsy from gastric antrum": "control",
        "normal biopsy from gastric body": "control",
        "normal biopsy from gastric cardia": "control",
        "intestinal metaplasia biopsy from gastric antrum": None,
        "intestinal metaplasia biopsy from gastric body": None,
        "intestinal metaplasia biopsy from gastric cardia": None,
        "mild intestinal metaplasia biopsy from gastric antrum": None,
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"
