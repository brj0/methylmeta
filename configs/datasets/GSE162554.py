def dataset_id(row):
    return "GSE162554"


def description(row):
    return (
        "Paired bone marrow and peripheral blood methylation profiles from "
        "pediatric cancer patients during and after chemotherapy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Bone marrow": "normal bone marrow",
        "peripheral blood": "normal peripheral blood",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "Bone marrow": "CTRL_MARROW",
        "peripheral blood": "CTRL_BLOOD",
    }
    return mapping[row["tissue"]]


def sample_site(row):
    return row["tissue"]


def sample_type(row):
    return "control"


def material_type(row):
    return "blood"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
