def dataset_id(row):
    return "GSE306095"


def description(row):
    return (
        "Pediatric Mexican B-cell acute lymphoblastic leukemia "
        "case-control methylation cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["disease state"] == "acute lymphoblastic leukemia patient":
        return "B-cell acute lymphoblastic leukemia"
    mapping = {
        "Bone marrow": "normal bone marrow",
        "Peripheral blood": "normal peripheral blood",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    if row["disease state"] == "acute lymphoblastic leukemia patient":
        return "B_ALL"
    mapping = {
        "Bone marrow": "CTRL_MARROW",
        "Peripheral blood": "CTRL_BLOOD",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    mapping = {
        "acute lymphoblastic leukemia patient": "primary",
        "non leukemic patient": "control",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "blood"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]
