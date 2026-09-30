def dataset_id(row):
    return "GSE169265"


def description(row):
    return (
        "Methylation profiling of subependymoma of the posterior fossa and "
        "ependymoma evolving from subependymoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["subtype"]
    mapping = {
        "pure SE": "subependymoma",
        "mixed, distinct": "mixed subependymoma and ependymoma (distinct)",
        "mixed, diffuse": "mixed subependymoma and ependymoma (diffuse)",
        "E_mcSE,PF-6": "ependymoma, methylation class subependymoma",
    }
    return mapping[value]


def methylation_class(row):
    return "SUBEPN_PF"


def primary_site(row):
    return "Posterior fossa"


def sample_site(row):
    return "Posterior fossa"


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
