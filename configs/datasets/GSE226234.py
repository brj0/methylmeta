def dataset_id(row):
    return "GSE226234"


def description(row):
    return (
        "Genetic and epigenetic features of bilateral Wilms tumor "
        "predisposition, DNA methylation (St. Jude Children's Research "
        "Hospital)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["Source"] == "Blood":
        return "normal blood"
    return row["diagnosis"]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Blood": "CTRL_BLOOD",
        "Tumor": "WILMS",
    }
    return mapping[value]


def sample_type(row):
    value = row["Source"]
    mapping = {
        "Blood": "control",
        "Tumor": "primary",
    }
    return mapping[value]


def material_type(row):
    value = row["Source"]
    mapping = {
        "Blood": "blood",
        "Tumor": "tissue",
    }
    return mapping[value]


def sample_site(row):
    value = row["Source"]
    mapping = {
        "Blood": "Blood",
        "Tumor": "Kidney",
    }
    return mapping[value]


def primary_site(row):
    if row["Source"] == "Tumor":
        return "Kidney"
    return None
