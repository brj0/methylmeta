def dataset_id(row):
    return "GSE318768"


def description(row):
    return (
        "HPV-related DNA methylation alterations shape the head and neck "
        "tumor microenvironment in space and time"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    title = row["Title"]
    if "_HPV_Positive" in title:
        return "Head and neck squamous cell carcinoma, HPV-positive"
    if "_HPV_Negative" in title:
        return "Head and neck squamous cell carcinoma, HPV-negative"
    return title


def methylation_class(row):
    title = row["Title"]
    if "_HPV_Positive" in title:
        return "HNSCC_HPVA"
    if "_HPV_Negative" in title:
        return "HNSCC_HPVI"
    return None


def sample_site(row):
    return "Head and neck"


def primary_site(row):
    return "Head and neck"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
