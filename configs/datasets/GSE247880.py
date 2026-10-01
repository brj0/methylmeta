def dataset_id(row):
    return "GSE247880"


def description(row):
    return (
        "DNA methylation alterations across time and space in paediatric "
        "brain tumours: paired primary, recurrent and metastatic brain "
        "tumour samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Paediatric brain tumour"


def methylation_class(row):
    return None


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "Primary": "primary",
        "Recurrent": "recurrence",
        "Metastatic": "metastasis",
    }
    return mapping[row["tissue type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
