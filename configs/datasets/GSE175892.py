def dataset_id(row):
    return "GSE175892"


def description(row):
    return (
        "DNA methylation profiling of SCCOHT and SMARCB1-mutated "
        "rhabdoid tumours"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["sample type"]
    mapping = {
        "ATRT": "Atypical teratoid/rhabdoid tumor",
        "ECRT": "Extracranial rhabdoid tumor, SMARCB1-deficient",
        "SCCOHT": "Small cell carcinoma of the ovary, hypercalcemic type",
    }
    return mapping[value]


def methylation_class(row):
    value = row["sample type"]
    mapping = {
        "ATRT": "ATRT",
        "ECRT": "ERRT",
        "SCCOHT": "SCCOHT",
    }
    return mapping[value]


def sample_site(row):
    value = row["sample type"]
    mapping = {
        "ATRT": "Central nervous system",
        "ECRT": None,
        "SCCOHT": "Ovary",
    }
    return mapping[value]


def primary_site(row):
    value = row["sample type"]
    mapping = {
        "ATRT": "Central nervous system",
        "ECRT": None,
        "SCCOHT": "Ovary",
    }
    return mapping[value]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]
