def dataset_id(row):
    return "E-MTAB-13583"


def description(row):
    return (
        "Illumina EPIC methylation profiling of peripheral blood from "
        "children with developmental language disorder and healthy controls"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "developmental language disorder": (
            "blood, developmental language disorder"
        ),
        "normal": "normal blood",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "developmental language disorder": "CTRL_BLOOD",
        "normal": "CTRL_BLOOD",
    }
    return mapping[value]


def sample_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "control"


def material_type(row):
    return "blood"
