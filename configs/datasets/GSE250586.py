def dataset_id(row):
    return "GSE250586"


def description(row):
    return (
        "Methylation profiling of medulloblastoma tumors (WNT, SHH, group 3 "
        "and group 4) used to map naturally presented T-cell antigens"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "medulloblastoma"


def methylation_class(row):
    mapping = {
        "WNT": "MB_WNT",
        "SHH": "MB_SHH",
        "Group 3": "MB_G3",
        "Group 4": "MB_G4",
    }
    return mapping[row["tumor subgroup"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    return "G4"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age at diagnosis"])
