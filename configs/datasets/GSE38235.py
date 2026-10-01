def dataset_id(row):
    return "GSE38235"


def description(row):
    return (
        "Paired tumor and remission samples of childhood B-cell precursor "
        "acute lymphoblastic leukemia profiled on the 450k array"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    if row["disease state"] == "remission":
        return "normal bone marrow"
    return "B-cell precursor acute lymphoblastic leukemia"


def methylation_class(row):
    control_class = {"remission": "CTRL_MARROW"}
    if row["disease state"] in control_class:
        return control_class[row["disease state"]]
    subtype_class = {
        "hyperdiploid": "B_ALL_HYPERDIP",
        "hypodiploidy": "B_ALL_HYPODIP",
        "no abnormal finding": "B_ALL",
        "t(1;19)(q23;p13)": "B_ALL_TCF3_PBX1",
        "t(4;11)(q21;q23)": "B_ALL_KMT2A",
        "t(9;12)(p11?;p13); monosomy 7": "B_ALL",
        "t(9;22)(q34;q11.2)": "B_ALL_BCR_ABL1",
        "t(12;21)(p13;q22)": "B_ALL_ETV6_RUNX1",
        "t(12;21)(p13;q22); trisomy 21": "B_ALL_ETV6_RUNX1",
        "trisomy 5": "B_ALL",
    }
    return subtype_class.get(row["tumor subtype"], "B_ALL")


def sample_type(row):
    state_type = {"remission": "control"}
    return state_type.get(row["disease state"], "primary")


def material_type(row):
    return "blood"


def preservation(row):
    return "FROZEN"


def primary_site(row):
    return "Bone marrow"


def sex(row):
    return row["gender"]
