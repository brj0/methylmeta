def dataset_id(row):
    return "E-MTAB-8762"


def description(row):
    return (
        "Molecular characterization of T-cell lymphoblastic lymphoma "
        "in children and adolescents"
    )


def sample_id(row):
    # IDAT basename, e.g. 'EPIC_TP14'.
    return row["Sample_ID"]


def diagnosis(row):
    if row["Characteristics[developmental stage]"] == "germline":
        return "normal " + row["Characteristics[organism part]"]
    return row["Characteristics[disease]"]


def methylation_class(row):
    if row["Characteristics[developmental stage]"] == "germline":
        controls = {
            "bone marrow": "CTRL_MARROW",
            "peripheral blood": "CTRL_BLOOD",
        }
        return controls[row["Characteristics[organism part]"]]
    return "T_ALL"


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    if row["Characteristics[developmental stage]"] == "germline":
        return None
    return "bone marrow"


def sample_type(row):
    value = row["Characteristics[developmental stage]"]
    mapping = {
        "germline": "control",
        "primary tumor": "primary",
        "relapse": "recurrence",
    }
    return mapping[value]


def material_type(row):
    value = row["Characteristics[organism part]"]
    if "blood" in value:
        return "blood"
    return "tissue"


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    return float(value)
