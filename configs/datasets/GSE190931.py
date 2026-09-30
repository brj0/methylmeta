def dataset_id(row):
    return "GSE190931"


def description(row):
    return (
        "Pediatric acute myeloid leukemia (AAML1031), diagnostic and relapsed "
        "specimens, Smith 2022"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "pediatric acute myeloid leukemia"


def methylation_class(row):
    return "AML"


def sample_type(row):
    mapping = {"Diagnosis": "primary", "Relapse": "recurrence"}
    return mapping[row["timepoint"]]


def material_type(row):
    return "blood"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age (years)"])
