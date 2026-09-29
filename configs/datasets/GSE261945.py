def dataset_id(row):
    return "GSE261945"


def description(row):
    return (
        "Spindle cell lesions with oncogenic EGFR kinase domain aberrations "
        "(protein kinase-related mesenchymal tumours)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    # Sarcoma classifier output, e.g. "DFSP (score 0.91)", with the first
    # (highest scoring) call used when two classes are reported.
    top_call = row["methylation class"].split(",")[0]
    label = top_call.split(" (score")[0].strip()
    mapping = {
        "Chondrosarcoma family": "CSA",
        "DFSP": "DFSP",
        "Lipoma": "LIPO",
        "MPNST-like sarcoma": "MPNST",
        "Sarcoma MPNST-like": "MPNST",
        "Well- / dedifferentiated liposarcoma": "LPS_WD_DD",
    }
    return mapping[label]


def sample_site(row):
    return "Soft tissue"


def primary_site(row):
    return "Soft tissue"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
