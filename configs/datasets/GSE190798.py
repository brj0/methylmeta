def dataset_id(row):
    return "GSE190798"


def description(row):
    return (
        "Retrospective pediatric ependymoma DNA methylation profiles, "
        "Nottingham, UK"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    mapping = {
        "PF_EPN_A": "EPN_PF_A",
        "ST_EPN_RELA": "EPN_ST_ZFTA",  # RELA is the former name of ZFTA
    }
    return mapping[row["methylation class"]]


def sample_site(row):
    mapping = {"PF": "Posterior fossa", "ST": "Supratentorial"}
    return mapping[row["tumor location"]]


def primary_site(row):
    mapping = {"PF": "Posterior fossa", "ST": "Supratentorial"}
    return mapping[row["tumor location"]]


def sample_type(row):
    case = row["Title"][:-1]
    while case[-1].isdigit():
        case = case[:-1]
    return {"P": "primary", "R": "recurrence"}[case[-1]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping.get(row["gender"])


def tumor_grade(row):
    grade = row["who grade"]
    if grade is None:
        return None
    mapping = {2: "G2", 3: "G3"}
    return mapping[int(grade)]
