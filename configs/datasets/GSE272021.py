def dataset_id(row):
    return "GSE272021"


def description(row):
    return (
        "Pediatric T-cell acute lymphoblastic leukemia CIMP methylation "
        "profiling at diagnosis, with sorted blood cell and lymph node "
        "controls"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    if row["tissue type"] == "Control":
        mapping = {
            "Lymph node sample": "normal lymph node",
            "Peripheral blood sample": "normal peripheral blood",
            "T-ALL bone marrow/peripheral blood sample": "normal blood",
        }
        return mapping[row["tissue"]]
    return row["disease"]


def methylation_class(row):
    if row["tissue type"] == "Control":
        mapping = {
            "Lymph node sample": "CTRL_LYMPH",
            "Peripheral blood sample": "CTRL_BLOOD",
            "T-ALL bone marrow/peripheral blood sample": "CTRL_BLOOD",
        }
        return mapping[row["tissue"]]
    return "T_ALL"


def sample_site(row):
    value = row["tissue"]
    if value.startswith("T-ALL "):
        value = value[len("T-ALL ") :]
    if value.endswith(" sample"):
        value = value[: -len(" sample")]
    return value


def primary_site(row):
    if row["tissue type"] == "Control":
        return sample_site(row)
    return "bone marrow"


def sample_type(row):
    mapping = {"Control": "control", "Tumor": "primary"}
    return mapping[row["tissue type"]]


def material_type(row):
    mapping = {
        "Lymph node sample": "tissue",
        "Peripheral blood sample": "blood",
        "T-ALL bone marrow/peripheral blood sample": "blood",
    }
    return mapping[row["tissue"]]


def preservation(row):
    return "FROZEN"
