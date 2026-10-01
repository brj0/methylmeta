def dataset_id(row):
    return "GSE311943"


def description(row):
    return (
        "Primary lung adenocarcinoma samples from a Swedish multiomics "
        "epitype cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "LU_ADCA"


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Lung"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["patient age"])
