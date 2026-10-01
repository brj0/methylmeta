def dataset_id(row):
    return "GSE195684"


def description(row):
    return (
        "IDH wild-type glioblastoma (GBMnordic), FFPE surgical resections "
        "from Nordic clinical trials"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["tissue type"]
    if "FFPE" in value:
        return "FFPE"
    return None


def tumor_grade(row):
    value = row["grade"]
    mapping = {
        "grade I": "G1",
        "grade II": "G2",
        "grade III": "G3",
        "grade IV": "G4",
    }
    return mapping[value]


def sex(row):
    value = row["gender"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
