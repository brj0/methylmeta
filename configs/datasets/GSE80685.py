def dataset_id(row):
    return "GSE80685"


def description(row):
    return (
        "Localized sporadic and germline BRCA2-mutant prostate cancers, "
        "Taylor et al. 2017"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "BRCA2": "Prostate tumour in a germline BRCA2 mutation carrier",
        "Sporadic": "Sporadic prostate tumour",
    }
    return mapping[row["disease state"]]


def methylation_class(row):
    return "PROS_ADCA"


def sample_site(row):
    return "prostate"


def primary_site(row):
    return "prostate"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
