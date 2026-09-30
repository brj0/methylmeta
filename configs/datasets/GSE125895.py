def dataset_id(row):
    return "GSE125895"


def description(row):
    return (
        "Postmortem brain DNA methylation across four brain regions in an "
        "Alzheimer's disease case-control series, 2019"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Alzheimer": "Alzheimer's disease",
        "Control": "neurotypical control",
    }
    return mapping[row["disease state (dx)"]]


def methylation_class(row):
    return "CTRL_BRAIN"


def sample_site(row):
    mapping = {
        "CRB": "cerebellum",
        "DLPFC": "dorsolateral prefrontal cortex",
        "ERC": "entorhinal cortex",
        "HIPPO": "hippocampus",
    }
    return mapping[row["tissue region"]]


def primary_site(row):
    return "brain"


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
