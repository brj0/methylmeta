def dataset_id(row):
    return "GSE284758"


def description(row):
    return (
        "Molecular signatures define BAP1-altered meningioma as a distinct "
        "CNS tumor (Krumbein et al., 2025)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "meningioma, BAP1-altered"


def methylation_class(row):
    return "MNG"


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[row["material"]]


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
