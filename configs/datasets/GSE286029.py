def dataset_id(row):
    return "GSE286029"


def description(row):
    return (
        "Immunodeficiency-associated Burkitt lymphoma and malaria-related "
        "splenomegaly profiled by DNA methylation"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"].split(",")[0]


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "Splenomegaly, FFPE": "CTRL_NOS",
        "immunodeficiency-associated Burkitt lymphoma, "
        "FFPE, EBV-negative": "BURK_EBVN",
        "immunodeficiency-associated Burkitt lymphoma, "
        "FFPE, EBV-positive": "BURK_EBVP",
    }
    return mapping[value]


def sample_site(row):
    value = row["Source"]
    mapping = {
        "appendix": "Appendix",
        "ileon": "Ileum",
        "lymph node": "Lymph node",
        "spleen": "Spleen",
        "unkown": None,
    }
    return mapping[value]


def sample_type(row):
    value = row["Description"]
    mapping = {
        "Splenomegaly, FFPE": "control",
        "immunodeficiency-associated Burkitt lymphoma, "
        "FFPE, EBV-negative": "primary",
        "immunodeficiency-associated Burkitt lymphoma, "
        "FFPE, EBV-positive": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
