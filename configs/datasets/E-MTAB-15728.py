def dataset_id(row):
    return "E-MTAB-15728"


def description(row):
    return (
        "Pediatric acute promyelocytic leukemia methylation profiling cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "AML_PML_RARA"


def sample_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {"unknown": None}
    return mapping.get(value, value)


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    mapping = {"Male": "male", "Female": "female"}
    return mapping[row["Characteristics[sex]"]]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    return float(value)
