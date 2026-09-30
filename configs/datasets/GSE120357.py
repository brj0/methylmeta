def dataset_id(row):
    return "GSE120357"


def description(row):
    return (
        "Array-based DNA methylation profiling of primary central nervous "
        "system lymphomas (PCNSL), 2019"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "primary central nervous system lymphoma"


def methylation_class(row):
    return "CNSL"


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Source"]
    mapping = {
        "FFPE tumor": "FFPE",
        "cryo-preserved tumor": "FROZEN",
    }
    return mapping[value]


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
        "n/a": None,
    }
    return mapping[value]
