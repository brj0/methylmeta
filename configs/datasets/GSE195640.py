def dataset_id(row):
    return "GSE195640"


def description(row):
    return (
        "DNA methylation-based age acceleration in IDH wild-type "
        "glioblastoma (EORTC 26981/NCIC CE.3 and Lausanne pilot trials)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease state"]
    mapping = {"GBM": "Glioblastoma"}
    return mapping[value]


def methylation_class(row):
    value = row["disease state"]
    mapping = {"GBM": "GBM_NOS"}
    return mapping[value]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["tissue_type"]
    mapping = {"FFPE": "FFPE"}
    return mapping[value]


def tumor_grade(row):
    return "G4"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
