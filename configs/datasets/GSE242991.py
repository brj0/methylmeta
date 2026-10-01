def dataset_id(row):
    return "GSE242991"


def description(row):
    return (
        "Spinal ependymoma (SP-EPN) methylation profiling identifies "
        "NF2-related molecular subtypes"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Spinal ependymoma"


def methylation_class(row):
    return "EPN_SPINE"


def sample_site(row):
    return "Spinal cord"


def primary_site(row):
    return "Spinal cord"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"Cryo": "FROZEN", "FFPE": "FFPE"}
    return mapping[row["material type"]]
