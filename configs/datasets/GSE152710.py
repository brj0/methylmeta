def dataset_id(row):
    return "GSE152710"


def description(row):
    return (
        "High-risk myelodysplastic syndromes and secondary AML "
        "(CETLAM MDS-09 azacitidine response cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["time afer diagnosis"] == "CTR":
        return "normal bone marrow"
    return row["diagnosis"]


def methylation_class(row):
    if row["time afer diagnosis"] == "CTR":
        return "CTRL_MARROW"
    return "MDS_HIGH"


def sample_site(row):
    return "bone marrow"


def primary_site(row):
    return "bone marrow"


def sample_type(row):
    mapping = {
        "CTR": "control",
        "DX": "primary",
        "3-5M": "recurrence",
        "6-11M": "recurrence",
        "<3M": "recurrence",
        "> or equal to 12M": "recurrence",
        "POST TPH": "recurrence",
    }
    return mapping[row["time afer diagnosis"]]


def material_type(row):
    return "tissue"
