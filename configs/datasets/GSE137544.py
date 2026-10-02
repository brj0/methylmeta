def dataset_id(row):
    return "GSE137544"


def description(row):
    return (
        "Paediatric kidney tumour and matching tumour-derived organoid "
        "biobank (Wilms tumour, malignant rhabdoid tumour, renal cell "
        "carcinoma); Custers et al."
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Wilms tumor": "Wilms tumour",
        "Wilms organoid": "Wilms tumour",
        "MRT tumor": "Malignant rhabdoid tumour",
        "MRT organoid": "Malignant rhabdoid tumour",
        "RCC tumor": "Renal cell carcinoma",
        "RCC organoid": "Renal cell carcinoma",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "Wilms tumor": "WILMS",
        "Wilms organoid": "WILMS",
        "MRT tumor": "REN_MRT",
        "MRT organoid": "REN_MRT",
        "RCC tumor": "RCC",
        "RCC organoid": "RCC",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "Kidney"


def primary_site(row):
    return "Kidney"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "Wilms tumor": "tissue",
        "Wilms organoid": "cell_line",
        "MRT tumor": "tissue",
        "MRT organoid": "cell_line",
        "RCC tumor": "tissue",
        "RCC organoid": "cell_line",
    }
    return mapping[row["Source"]]


def preservation(row):
    return "FROZEN"
