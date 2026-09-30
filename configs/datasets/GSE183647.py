def dataset_id(row):
    return "GSE183647"


def description(row):
    return (
        "DNA methylation profiling of 565 meningiomas from two institutions "
        "(Nassiri et al. 2021)"
    )


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
    return "FROZEN"


def tumor_grade(row):
    mapping = {1: "G1", 2: "G2", 3: "G3"}
    return mapping[row["grade"]]


def sex(row):
    mapping = {1: "male", 2: "female"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
