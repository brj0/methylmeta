def dataset_id(row):
    return "GSE307314"


def description(row):
    return (
        "DNA methylation profiling of IDH-mutant medulloblastoma of the "
        "SHH type"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histology"]
    mapping = {
        "classic MB": "medulloblastoma, classic",
        "desmoplastic MB": "medulloblastoma, desmoplastic",
    }
    return mapping[value]


def methylation_class(row):
    # study reports all cases as SHH medulloblastoma; patients are 13-46
    # years old, i.e. the child/adult SHH class, not the infant SHH class
    return "MB_SHH_CHL_AD"


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Source"]
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[value]


def age(row):
    return float(row["age at diagnosis [years]"])
