def dataset_id(row):
    return "GSE38266"


def description(row):
    return (
        "450k methylation analysis of FFPE HPV-positive and HPV-negative "
        "head and neck squamous cell carcinomas"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "HPV+ HNSCC tumor": (
            "Head and neck squamous cell carcinoma, HPV-positive"
        ),
        "HPV- HNSCC tumor": (
            "Head and neck squamous cell carcinoma, HPV-negative"
        ),
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "HPV+ HNSCC tumor": "HNSCC_HPVA",
        "HPV- HNSCC tumor": "HNSCC_HPVI",
    }
    return mapping[value]


def sample_site(row):
    return row["tumour site"]


def primary_site(row):
    return row["tumour site"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
