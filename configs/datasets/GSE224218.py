def dataset_id(row):
    return "GSE224218"


def description(row):
    return "Adult intracranial ependymoma, DNA methylation profiling"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["incoming diagnosis"]


def _site(row):
    mapping = {
        "infratentorial": "Posterior fossa",
        "infratentoriell": "Posterior fossa",
        "supratentorial": "Supratentorial",
    }
    return mapping[row["tumor location"]]


def methylation_class(row):
    mapping = {
        ("Posterior fossa", "Anaplastic ependymoma (WHO grade III)"): "EPN_PF",
        ("Posterior fossa", "Ependymoma (WHO grade II)"): "EPN_PF",
        (
            "Supratentorial",
            "Anaplastic ependymoma (WHO grade III)",
        ): "EPN_ST",
        ("Supratentorial", "Ependymoma (WHO grade II)"): "EPN_ST",
    }
    return mapping[(_site(row), row["incoming diagnosis"])]


def sample_site(row):
    return _site(row)


def primary_site(row):
    return _site(row)


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "KRYO": "FROZEN",
    }
    return mapping[row["material type"]]


def tumor_grade(row):
    mapping = {
        "Anaplastic ependymoma (WHO grade III)": "high-grade",
        "Ependymoma (WHO grade II)": "low-grade",
    }
    return mapping[row["incoming diagnosis"]]


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping[row["Sex"]]


def age(row):
    return float(row["age"])
