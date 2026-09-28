def dataset_id(row):
    return "GSE97529"


def description(row):
    return (
        "DNA methylation profiling of bone sarcomas: Ewing's sarcoma, "
        "synovial sarcoma and osteosarcoma (Wu et al., 2017)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    value = row["diagnosis"].lower()
    if "ewing" in value:
        return "EWS"
    if "synovial" in value:
        return "SYNSARC"
    if "osteosarcoma" in value:
        return "OS"
    return None


def sample_site(row):
    return "Bone"


def primary_site(row):
    return "Bone"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {
        "female": "female",
        "male": "male",
    }
    return mapping[row["Sex"]]
