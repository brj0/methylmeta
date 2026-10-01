def dataset_id(row):
    return "GSE269319"


def description(row):
    return "Methylation profiling for pediatric pineal parenchymal tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "PINE_PPT"


def sample_site(row):
    return "Pineal gland"


def primary_site(row):
    return "Pineal gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["Sex"]]
