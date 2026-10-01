def dataset_id(row):
    return "GSE210723"


def description(row):
    return (
        "Paediatric brain tumour cohort (medulloblastoma, ependymoma, ATRT, "
        "ETMR, normal cerebellum) profiled for the EpiGe medulloblastoma "
        "classification study"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "ATRT": "Atypical teratoid/rhabdoid tumor",
        "Cerebellum": "Normal cerebellar tissue",
        "ETMR": "Embryonal tumor with multilayered rosettes",
        "Ependymoma": "Ependymoma",
        "Medulloblastoma": "Medulloblastoma",
    }
    return mapping[row["sample type"]]


def methylation_class(row):
    mapping = {
        ("ATRT", "ATRT"): "ATRT",
        ("ATRT", "SHH"): "ATRT",
        ("ATRT", "non-WNT/non-SHH"): "ATRT",
        ("Cerebellum", "Cerebellum"): "CTRL_CEBM",
        ("ETMR", "ETMR"): "ETMR",
        ("Ependymoma", "EP"): "EPN",
        ("Medulloblastoma", "SHH"): "MB_SHH",
        ("Medulloblastoma", "WNT"): "MB_WNT",
        ("Medulloblastoma", "non-WNT/non-SHH"): "MB",
    }
    return mapping[(row["sample type"], row["sample subtype"])]


def sample_type(row):
    mapping = {"Cerebellum": "control"}
    return mapping.get(row["sample type"], "primary")


def primary_site(row):
    return "Central nervous system"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Fresh-Frozen": "FROZEN"}
    return mapping[row["material"]]
