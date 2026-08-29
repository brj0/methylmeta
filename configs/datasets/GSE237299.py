def dataset_id(row):
    return "GSE237299"


def description(row):
    return "Hematolymphoid Tumors"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    value = str(row["tissue"]).lower()

    if "mantle cell lymphoma" in value or "mcl" in value:
        return "MCL"
    if "chronic lymphocytic" in value or "cll" in value:
        return "CLL"
    if "diffuse large bcell lymphoma" in value or "dlbcl" in value:
        return "DLBCL"
    if "infant b-cell precursor acute lymphoblastic" in value:
        return "B_ALL"
    if "angioimmunoblastic" in value or "aitl" in value:
        return "AITL"
    if "follicular lymphoma" in value or "fl" in value:
        return "FL"
    if "juvenile myelomonocytic" in value or "jmml" in value:
        return "JMML"
    if "burkitt" in value or "bl" in value:
        return "BURK"
    if "monomorphic epitheliotropic" in value or "meitl" in value:
        return "MEITL"
    if "t-all" in value or "t-lymphoblastic" in value:
        return "T_ALL"
    if "histiocytic sarcoma" in value or "hs" in value:
        return "HISTSARC"
    if "hepato" in value and "splenic" in value and "t-cell" in value:
        return "HSTCL"
    if "extranodal nk/t" in value and "nasal" in value:
        return "ENKTL"
    if "peripheral t-cell" in value or "ptcl" in value:
        return "PTCL"
    if "lymphoplasmacytic" in value or "lpl" in value:
        return "LPL"
    if "hairy cell" in value:
        return "HCL"
    if "sezary" in value:
        return "SZ"
    if "acute myelogenous" in value or "aml" in value:
        return "AML"
    if "pcgd" in value:
        return "PCGD"
    if "fdcs" in value or "follicular dendritic" in value:
        return "FDCS"
    if "marginal zone lymphoma" in value or "nmzl" in value:
        return "MZL"
    if "primary central nervous system lymphoma" in value or "cnsl" in value:
        return "CNSL"
    if "enteropathy-associated t-cell lymphoma" in value or "eatl" in value:
        return "EATL"
    if "hairy cell" in value or "hcl" in value:
        return "HCL"
    if "primary cutaneous follicle center lymphoma" in value:
        return "PCFCL"
    if (
        "primary cutaneous anaplastic large cell lymphoma" in value
        or "alcl" in value
    ):
        return "C_ALCL"
    if "anaplastic large" in value and "cell lymphoma" in value:
        return "ALCL"
    return "HL_NOS"


def sample_site(row):
    value = row["tissue_1"]
    mapping = {
        "--": None,
    }
    return mapping.get(value, value)


def preservation(row):
    value = row["material"]
    mapping = {
        "Frozen": "FROZEN",
        "PB": None,
        "FFPE": "FFPE",
    }
    return mapping[value]


def sex(row):
    return row["Sex"]


def age(row):
    return row["age"]
