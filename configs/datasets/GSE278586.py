def dataset_id(row):
    return "GSE278586"


def description(row):
    return (
        "DNA methylation profiling of ER-positive HER2-negative primary "
        "breast tumors"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return "ER-positive HER2-negative breast cancer"


def methylation_class(row):
    return "BR_CA_HRP"


def sample_site(row):
    return "Breast"


def primary_site(row):
    return "Breast"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FRESH"


def sex(row):
    value = row["Sex"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
