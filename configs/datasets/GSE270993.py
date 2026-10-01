def dataset_id(row):
    return "GSE270993"


def description(row):
    return (
        "Two molecularly and clinically distinct subtypes of H3 K27M-mutant "
        "diffuse midline gliomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Diffuse midline glioma, H3 K27-altered"


def methylation_class(row):
    return "DMG_K27"


def sample_site(row):
    return row["localisation"]


def primary_site(row):
    return row["localisation"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "FROZEN": "FROZEN"}
    return mapping[row["material"]]


def sex(row):
    mapping = {"f": "female", "m": "male"}
    return mapping[row["Sex"]]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
