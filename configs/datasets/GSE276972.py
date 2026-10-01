def dataset_id(row):
    return "GSE276972"


def description(row):
    return (
        "Pediatric spinal ependymoma cohort from the HIT-MED database, "
        "classified by DNA methylation profiling"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "MPE": "Myxopapillary ependymoma",
        "SP-EPN": "Spinal ependymoma",
        "SP-EPN-MYCN": "Spinal ependymoma, MYCN-amplified",
        "no match": "Spinal ependymoma, NOS",
    }
    return mapping[row["classification result v12.5"]]


def methylation_class(row):
    mapping = {
        "MPE": "EPN_MPE",
        "SP-EPN": "EPN_SPINE",
        "SP-EPN-MYCN": "EPN_SPINE_MYCN",
        "no match": None,
    }
    return mapping[row["classification result v12.5"]]


def sample_site(row):
    level = row["localization"]
    if level is None:
        return "Spinal cord"
    return f"Spinal cord, {level}"


def primary_site(row):
    return "Spinal cord"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["material"]
    if value is None:
        return "FFPE"
    return value


def tumor_grade(row):
    mapping = {
        "WHO grade 3": "G3",
        "non-myxopapillary WHO grade 2": "G2",
        "myxopapillary WHO grade non-myxopapillary WHO grade 2": "G2",
        "not specified": None,
    }
    return mapping[row["who tumor grade"]]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
