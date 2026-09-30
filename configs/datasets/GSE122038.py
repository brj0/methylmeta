def dataset_id(row):
    return "GSE122038"


def description(row):
    return "ETMR at diagnosis and relapse, Lambo et al. 2019"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Embryonal tumor with multilayered rosettes (ETMR)"


def methylation_class(row):
    return "ETMR"


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    # relapse samples are labelled with an _R suffix, e.g. "ET1_R1"
    if chr(95) in row["Title"]:
        return "recurrence"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["sample type"] or row["material"]
    if value is None:
        return None
    return {"FFPE": "FFPE", "Frozen": "FROZEN"}[value]
