def dataset_id(row):
    return "GSE134089"


def description(row):
    return (
        "Epigenome analysis of hereditary and sporadic neuroendocrine tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "DNET": "Duodenal neuroendocrine tumor",
        "GNET": "Gastric neuroendocrine neoplasm",
        "PNET": "Pancreatic neuroendocrine tumor",
        "SINET": "Small intestinal neuroendocrine tumor",
        "Unknown primary": "Neuroendocrine tumor of unknown primary site",
    }
    return mapping[row["tumor type"]]


def methylation_class(row):
    mapping = {
        "DNET": "DUO_NET",
        "GNET": "GAST_NET",
        "PNET": "PAN_NET",
        "SINET": "SI_NET",
        "Unknown primary": None,
    }
    return mapping[row["tumor type"]]


def sample_site(row):
    mapping = {
        "DNET": "Duodenum",
        "GNET": "Stomach",
        "PNET": "Pancreas",
        "SINET": "Small intestine",
        "Unknown primary": None,
    }
    return mapping[row["tumor type"]]


def primary_site(row):
    mapping = {
        "DNET": "Duodenum",
        "GNET": "Stomach",
        "PNET": "Pancreas",
        "SINET": "Small intestine",
        "Unknown primary": None,
    }
    return mapping[row["tumor type"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
