def dataset_id(row):
    return "GSE293851"


def description(row):
    return "DNA methylation profiling of incidental meningiomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["tumor grade"].strip()
    mapping = {"1": "G1", "2": "G2", "n/a": None}
    return mapping[value]


def sex(row):
    value = row["Sex"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    return float(row["age at surgery"])
