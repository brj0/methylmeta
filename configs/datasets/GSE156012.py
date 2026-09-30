def dataset_id(row):
    return "GSE156012"


def description(row):
    return (
        "Epigenetic methylation chip analysis of childhood medulloblastoma "
        "patient samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Medulloblastoma"


def methylation_class(row):
    return "MB"


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


def sex(row):
    mapping = {"female": "female", "male": "male"}
    return mapping[row["gender"]]
