def dataset_id(row):
    return "GSE140124"


def description(row):
    return "Epigenome analysis of pediatric bithalamic diffuse gliomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Bithalamic diffuse glioma"


def methylation_class(row):
    # No clear type in metadata
    return None


def sample_site(row):
    return "Thalamus"


def primary_site(row):
    return "Thalamus"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
