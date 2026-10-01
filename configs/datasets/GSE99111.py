def dataset_id(row):
    return "GSE99111"


def description(row):
    return "DNA methylation epigenotypes of clinical gastric cancer cases"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "GAST_ADCA"


def sample_site(row):
    return "Stomach"


def primary_site(row):
    return "Stomach"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Male": "male", "Female": "female"}
    return mapping[row["gender"]]
