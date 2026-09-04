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

    # DLBCL subtype (ABC/GCB) gets its own check up front: the "ABC"/"GCB"
    # marker shows up with or without a comma/space around it, and both
    # "DLBCL" and the spelled-out name appear in this dataset.
    if "dlbcl" in value or "diffuse large b-cell lymphoma" in value:
        if "leg type" in value:
            return "DLBCL_PC_LEG"
        if "non-gcb" in value or "abc" in value:
            return "DLBCL_ABC"
        if "gcb" in value or "germinal center" in value:
            return "DLBCL_GCB"
        return "DLBCL"
    if "anaplastic large" in value:
        if "positive" in value:
            return "ALCL_ALK_POS"
        if "negative" in value:
            return "ALCL_ALK_NEG"

    mapping = {
        # Specific entities first - riskiest overlaps up top.
        "marginal zone b-cell lymphoma, splenic type": "LYM_B_MZL_SP",
        "castleman disease, hyaline vascular variant": "CAST",
        "primary cutaneous anaplastic large cell lymphoma": "C_ALCL",
        "cutaneous alcl": "C_ALCL",
        "infant b-cell precursor acute lymphoblastic": "B_ALL",
        "b-lymphoblastic": "B_ALL",
        "b-all": "B_ALL",
        "primary cutaneous follicle cent": "PCFCL",  # center/centre
        "primary central nervous system lymphoma": "CNSL",
        "cutaneous gamma delta": "PCGD",
        "cutenaous gamma delta": "PCGD",  # dataset typo
        "pcgd": "PCGD",
        "acute myelogenous leukemia": "AML",
        "monomorphic epitheliotropic": "MEITL",
        "meitl": "MEITL",
        "juvenile myelomonocytic": "JMML",
        "jmml": "JMML",
        "langerhans": "LCH",
        "fdc sarcoma": "FDCS",
        "fdcs": "FDCS",
        "chronic lymphocytic": "CLL",
        "mantle cell lymphoma": "MCL",
        "mcl": "MCL",
        "lymphoblastic leukemia": "T_ALL",  # after b-lymphoblastic/b-all above
        "t-lymphoblastic": "T_ALL",
        "angioimmunoblastic": "AITL",  # before follicular helper (WHO: angio-type TFH)
        "follicular helper": "FTHCL",
        "tfh": "FTHCL",
        "follicular t-cell lymphoma": "FTHCL",
        "anaplastic large": "ALCL",  # after cutaneous ALCL variants above
        "peripheral t-cell": "PTCL",
        "lymphoplasm": "LPL",  # lymphoplasmacytic / lymphoplasmocytic (typo)
        "lpl": "LPL",
        "enteropathy-associated": "EATL",
        "eatl": "EATL",
        "histiocytic sarcoma": "HISTSARC",
        "cll": "CLL",
        "marginal zone": "MZL",  # after the splenic-specific key above
        "nmzl": "MZL",
        "mzl": "MZL",
        "follicular lymphoma": "FL",
        "extranodal nk/t": "ENKTL",
        "hepatosplenic": "HSTCL",
        "hairy cell": "HCL",
        "bl, ebv": "BURK",
        "burkitt": "BURK",
        "sezary": "SZ",  # fixed: WHO acronym is SZ, not SEZARY
        "plasma cell neoplasm": "PLASMA_CELL",
        "plasmazytoma": "PLASMA",
        "plasmacytoma": "PLASMA",
        "dendritic": "FDCS",  # after lymphoblastic keys (avoids FDCS clash)
        "unicentric castleman": "CAST",
        # Reactive / non-neoplastic lymph node changes -> control tissue.
        "reactive lymphoid hyperplasia": "CONTR_LYMPH",
        "reactive follicular": "CONTR_LYMPH",
        "follicular hyperplasia": "CONTR_LYMPH",
        "paracortical hyperplasia": "CONTR_LYMPH",
        "fh": "CONTR_LYMPH",
    }
    for text, acronym in mapping.items():
        if text in value:
            return acronym
    return None


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
