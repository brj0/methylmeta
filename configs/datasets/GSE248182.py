def dataset_id(row):
    return "GSE248182"


def description(row):
    return (
        "Methylation profiling of rhabdomyosarcoma tissue samples and their "
        "matched in vitro models from four patients"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histological_subtype"] + " " + row["cell_type"].lower()


def methylation_class(row):
    mapping = {
        "Embryonal": "RMS_EMB",
    }
    return mapping[row["histological_subtype"]]


def sample_type(row):
    value = row["disease_state"]
    mapping = {
        "Primary": "primary",
        "Relapse": "recurrence",
        "Relapse/metastatic": "metastasis",
    }
    return mapping[value]


def sample_site(row):
    return row["sample_location"]


def primary_site(row):
    return row["primary_tumor_location"]


def material_type(row):
    if "tissue" in row["Source"]:
        return "tissue"
    return "cell_line"


def preservation(row):
    value = row["fresh/cryopreserved"]
    mapping = {"cryopreserved": "FROZEN", "fresh": "FRESH"}
    return mapping.get(value)


def sex(row):
    value = row["Sex"]
    mapping = {"M": "male", "F": "female"}
    return mapping[value]


def age(row):
    value = row["age_in_years"]
    if value == "< 1":
        return None
    return float(value)
