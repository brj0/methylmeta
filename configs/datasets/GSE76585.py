def dataset_id(row):
    return "GSE76585"


def description(row):
    return (
        "DNA methylation profiling of pediatric B lymphoblastic leukemia "
        "with KMT2A rearrangement"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "B_ALL_KMT2A"


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    mapping = {"f": "female", "m": "male"}
    return mapping[row["gender"]]
