def dataset_id(row):
    return "GSE61160"


def description(row):
    return (
        "IDH-mutated oligodendroglial tumors with and without 1p/19q "
        "codeletion and non-tumoral brain tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnosis"]
    if value is None:
        return row["Description"]
    mapping = {
        "OD": "oligodendroglioma",
        "AOD": "anaplastic oligodendroglioma",
        "OA": "oligoastrocytoma",
        "AOA": "anaplastic oligoastrocytoma",
    }
    return mapping[value]


def methylation_class(row):
    # diagnosis is empty for the non-tumoral brain samples
    if row["diagnosis"] is None:
        return "CTRL_BRAIN"
    mapping = {
        "OD": "OLIGO_IDH",
        "AOD": "OLIGO_IDH_ANA",
        "OA": "OLIGO_IDH",
        "AOA": "OLIGO_IDH_ANA",
    }
    return mapping[row["diagnosis"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    if row["diagnosis"] is None:
        return "control"
    return "primary"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    mapping = {
        "OD": "G2",
        "AOD": "G3",
        "OA": "G2",
        "AOA": "G3",
        None: None,
    }
    return mapping[row["diagnosis"]]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
