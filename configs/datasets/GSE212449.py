def dataset_id(row):
    return "GSE212449"


def description(row):
    return (
        "Genetic and epigenetic profiling identifies two distinct classes of "
        "spinal meningiomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    histology = row["histology"]
    if histology:
        return f"spinal meningioma, {histology}"
    return "spinal meningioma"


def methylation_class(row):
    mapping = {
        "ben-1": "MNG_BEN_1",
        "ben-2": "MNG_BEN_2",
        "ben-3": "MNG_BEN_3",
        "int-A": "MNG_INTA",
        "int-B": "MNG_INTB",
        "mal": "MNG_MAL",
    }
    return mapping[row["meth.subclass(heidelbergclassifier)"]]


def sample_site(row):
    return "Spinal meninges"


def primary_site(row):
    return "Spinal meninges"


def sample_type(row):
    if "recurrence" in row["Description"]:
        return "recurrence"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = row["who_grade"]
    if value is None:
        return None
    mapping = {1: "G1", 2: "G2", 3: "G3"}
    return mapping[int(value)]


def sex(row):
    mapping = {"f": "female", "m": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
