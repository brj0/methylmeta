def dataset_id(row):
    return "GSE168808"


def description(row):
    return "Methylation profiling of endolymphatic sac tumors (ELST)"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "endolymphatic sac tumor"


def methylation_class(row):
    return "ELST"


def primary_site(row):
    return "Temporal bone"


def sample_site(row):
    return "Temporal bone"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"f": "female", "m": "male"}
    return mapping[row["gender"]]


def age(row):
    return float(row["age"])
