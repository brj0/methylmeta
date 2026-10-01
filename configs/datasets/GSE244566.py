def dataset_id(row):
    return "GSE244566"


def description(row):
    return (
        "Molecular refinement of pilocytic astrocytoma in adult patients: "
        "methylation profiling of 71 histologically diagnosed pilocytic "
        "astrocytomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["initial histological diagnosis"]


def methylation_class(row):
    mapping = {
        "EPN_SPINE": "EPN_SPINE",
        "EPN_SPINE_SE_A": "EPN_SPINE",
        "HGAP": "HGAP",
        "PA_CORT": "LGG_PA_GG_ST",
        "PA_INF": "LGG_PA_PF",
        "PA_MID": "LGG_PA_MID",
        "PXA": "PXA",
        "RGNT": "LGG_RGNT",
        "no match": None,
    }
    return mapping[row["brain tumor classifier result (v12.5)"]]


def sample_site(row):
    mapping = {"not available": None}
    return mapping.get(row["Source"], row["Source"])


def primary_site(row):
    mapping = {"not available": None}
    return mapping.get(row["Source"], row["Source"])


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["material"]


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age"]
    return float(value) if value is not None else None
