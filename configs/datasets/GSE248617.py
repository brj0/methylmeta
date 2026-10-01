def dataset_id(row):
    return "GSE248617"


def description(row):
    return (
        "Paired primary and relapsed posterior fossa type A (PF-EPN-A) "
        "ependymoma, DNA methylation profiling"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Posterior fossa ependymoma type A (PF-EPN-A)"


def methylation_class(row):
    return "EPN_PF_A"


def sample_site(row):
    return "Posterior fossa"


def primary_site(row):
    return "Posterior fossa"


def sample_type(row):
    if "primary" in row["Title"]:
        return "primary"
    return "recurrence"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN", "Fresh": "FRESH"}
    return mapping.get(row["material"])


def tumor_grade(row):
    value = row["who-grade"]
    if value is None:
        return None
    mapping = {1.0: "G1", 2.0: "G2", 3.0: "G3", 4.0: "G4"}
    return mapping.get(float(value))


def sex(row):
    value = row["Sex"]
    if value is None:
        return None
    mapping = {"f": "female", "m": "male"}
    return mapping[value]


def age(row):
    value = row["age (years)"]
    if value is None:
        return None
    return float(value)
