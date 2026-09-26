def dataset_id(row):
    return "GSE161407"


def description(row):
    return (
        "DNA methylation profiling of osteosarcoma patient samples and "
        "normal bone samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def _is_control(row):
    return row["Title"].startswith("Normal")


def diagnosis(row):
    if _is_control(row):
        return "normal bone tissue"
    return "osteosarcoma"


def methylation_class(row):
    if _is_control(row):
        return "CTRL_BONE"
    return "OS"


def sample_site(row):
    return "Bone"


def primary_site(row):
    return "Bone"


def sample_type(row):
    if _is_control(row):
        return "control"
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male", None: None}
    return mapping[row["Sex"]]
