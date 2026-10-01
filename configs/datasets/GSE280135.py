def dataset_id(row):
    return "GSE280135"


def description(row):
    return (
        "Primary central conventional chondrosarcoma methylation profiling "
        "(CHROME risk model study)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    value = row["idh status"]
    mapping = {
        "IDH1 MUT": "CSA_IDH_MUT",
        "IDH2 MUT": "CSA_IDH_MUT",
        "WT": "CSA_IDH_WT",
    }
    return mapping[value]


def sample_site(row):
    return "Bone"


def primary_site(row):
    return "Bone"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    value = row["grade"]
    mapping = {
        "ACT": "G1",
        "2": "G2",
        "3": "G3",
    }
    return mapping[value]


def sex(row):
    value = row["Sex"]
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[value]


def age(row):
    return float(row["age"])
