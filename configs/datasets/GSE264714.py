def dataset_id(row):
    return "GSE264714"


def description(row):
    return "A novel type of spinal ependymoma with anaplastic features"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "EPN_SPINE"


def sample_site(row):
    return "Spinal cord"


def primary_site(row):
    return "Spinal cord"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
