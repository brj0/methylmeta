def dataset_id(row):
    return "GSE69229"


def description(row):
    return "Childhood acute lymphoblastic leukemia, 4 cytogenetic subtypes"


def sample_id(row):
    return row["Description"].split("\n")[-1].strip()


def diagnosis(row):
    return "B-lymphoblastic leukemia " + row["all cytogenetic subtype"]


def methylation_class(row):
    value = row["all cytogenetic subtype"]
    mapping = {
        "Dic(9;20)": "B_ALL",
        "ETV6-RUNX1": "B_ALL_ETV6_RUNX1",
        "HeH": "B_ALL",
        "TCF3-PBX1": "B_ALL_TCF3_PBX1",
    }
    return mapping[value]


def sample_site(row):
    return "Bone marrow"


def primary_site(row):
    return "Bone marrow"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]
