def dataset_id(row):
    return "GSE262524"


def description(row):
    return (
        "DNA methylation profiling of prostate tumor and adjacent non-tumor "
        "tissue from European American men (EPIC)"
    )


def sample_id(row):
    value = row["Sample_ID"]
    for suffix in ("_Green", "_Red"):
        if value.endswith(suffix):
            return value[: -len(suffix)]
    return value


def diagnosis(row):
    if row["Source"] == "Tumor":
        return "Prostate adenocarcinoma"
    return "Normal prostate tissue"


def methylation_class(row):
    mapping = {
        "Tumor": "PROS_ADCA",
        "Adjacent Tumor": "CTRL_PROST",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "prostate"


def primary_site(row):
    return "prostate"


def sample_type(row):
    mapping = {
        "Tumor": "primary",
        "Adjacent Tumor": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def sex(row):
    return "male"
