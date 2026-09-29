def dataset_id(row):
    return "GSE289527"


def description(row):
    return (
        "Age-linked DNA methylation and gene expression in head and neck "
        "alveolar rhabdomyosarcoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Alveolar rhabdomyosarcoma"


def methylation_class(row):
    return "RMS_ALV"


def sample_site(row):
    return "Head and neck"


def primary_site(row):
    return "Head and neck"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"].split()[0])
