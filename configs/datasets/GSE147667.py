def dataset_id(row):
    return "GSE147667"


def description(row):
    return (
        "DNA methylation profiles of primary adult T-ALL and sorted normal "
        "thymic T-cell subpopulations (GRAALL 2003-2005 trial)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnosis"]
    mapping = {"normal": "normal thymus"}
    return mapping.get(value, value)


def methylation_class(row):
    mapping = {
        "T-ALL": "T_ALL",
        "normal": "CTRL_THYM",
    }
    return mapping[row["diagnosis"]]


def sample_type(row):
    mapping = {
        "T-ALL": "primary",
        "normal": "control",
    }
    return mapping[row["diagnosis"]]


def sample_site(row):
    mapping = {
        "T-ALL Bone Marrow": "Bone marrow",
        "Normal Thymic cell type": "Thymus",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    mapping = {
        "T-ALL Bone Marrow": "Bone marrow",
        "Normal Thymic cell type": "Thymus",
    }
    return mapping[row["tissue"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping.get(row["gender"])


def age(row):
    return row["age"]
