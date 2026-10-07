def dataset_id(row):
    return "GSE282216"


def description(row):
    return (
        "DNA methylation profiling of MPNST, adjacent neurofibroma, "
        "normal nerve tissue and nerve sheath cell lines from NF1 patients"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "MPNST_T": "malignant peripheral nerve sheath tumor",
        "MPNST Cell Line": "malignant peripheral nerve sheath tumor",
        "NF": "neurofibroma",
        "Nerve": "normal peripheral nerve",
        "Normal Schwann Cell Line": "normal Schwann cell",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "MPNST_T": "MPNST",
        "MPNST Cell Line": "MPNST",
        "NF": "NFIB",
        "Nerve": "CTRL_NERVE",
        "Normal Schwann Cell Line": "CTRL_NERVE",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return "peripheral nerve"


def primary_site(row):
    return "peripheral nerve"


def sample_type(row):
    mapping = {
        "MPNST_T": "primary",
        "MPNST Cell Line": "primary",
        "NF": "primary",
        "Nerve": "control",
        "Normal Schwann Cell Line": "control",
    }
    return mapping[row["Source"]]


def material_type(row):
    mapping = {
        "MPNST_T": "tissue",
        "MPNST Cell Line": "cell_line",
        "NF": "tissue",
        "Nerve": "tissue",
        "Normal Schwann Cell Line": "cell_line",
    }
    return mapping[row["Source"]]
