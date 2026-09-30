def dataset_id(row):
    return "GSE109507"


def description(row):
    return "DNA methylation analysis in familial adenomatous polyposis"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return f"{row['disease state']} tumor"


def methylation_class(row):
    # 23 colorectal tumours from FAP patients, grouped into low or
    # intermediate methylation level; no adenoma histology is given.
    return "CR_CA"


def sample_site(row):
    return "Colon / rectum"


def primary_site(row):
    return "Colon / rectum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Male": "male", "Female": "female"}
    return mapping[row["gender"]]
