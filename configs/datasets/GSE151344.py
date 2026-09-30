def dataset_id(row):
    return "GSE151344"


def description(row):
    return (
        "Medulloblastoma patient-derived orthotopic xenografts and matching "
        "human tumors (Rokita et al. 2020)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["Source"] == "PDOX":
        return "medulloblastoma (patient-derived orthotopic xenograft)"
    return "medulloblastoma"


def methylation_class(row):
    mapping = {
        "MB_GRP3": "MB_G3",
        "MB_GRP4": "MB_G4",
        "MB_SHH": "MB_SHH",
    }
    return mapping[row["tumor subgroup"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
