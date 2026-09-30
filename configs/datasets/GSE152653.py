def dataset_id(row):
    return "GSE152653"


def description(row):
    return (
        "Epigenome analysis of low-grade neuroepithelial tumors "
        "with FGFR1 alterations"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Title"].split("#")[0].strip()
    mapping = {
        "RGNT": "Rosette-forming glioneuronal tumor",
        "PA": "Pilocytic astrocytoma",
        "DNT": "Dysembryoplastic neuroepithelial tumor",
        "EVN": "Extraventricular neurocytoma",
        "uLGNET": "Unclassified low-grade neuroepithelial tumor",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Title"].split("#")[0].strip()
    mapping = {
        "RGNT": "LGG_RGNT",
        "PA": "LGG",
        "DNT": "LGG_DNT",
        "EVN": "EVN",
        "uLGNET": None,
    }
    return mapping[value]


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]
