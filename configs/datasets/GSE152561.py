def dataset_id(row):
    return "GSE152561"


def description(row):
    return (
        "5mC and 5hmC profiles of pediatric brain tumors (glioma, "
        "ependymoma, embryonal) and non-tumor pediatric brain tissue"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Embryonal": "Embryonal tumor, NOS",
        "Ependymoma": "Ependymoma",
        "Glioma": "Glioma",
        "Non-Tumor": "Non-tumor brain tissue",
    }
    return mapping[row["tumor_type"]]


def methylation_class(row):
    tumor_type = row["tumor_type"]
    if tumor_type == "Non-Tumor":
        return "CTRL_BRAIN"
    if tumor_type == "Embryonal":
        return "CNS_EMB_NEC"
    if tumor_type == "Ependymoma":
        mapping = {
            "POSTERIOR FOSSA": "EPN_PF",
            "4TH VENTRICLE": "EPN_PF",
            "SPINAL CORD": "EPN_SPINE",
        }
        return mapping.get(row["sample brain lobe location"])
    if tumor_type == "Glioma" and str(row["who_grade"]) in {"1", "2"}:
        return "LGG"
    return None


def sample_site(row):
    return row["sample brain lobe location"]


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "Embryonal": "primary",
        "Ependymoma": "primary",
        "Glioma": "primary",
        "Non-Tumor": "control",
    }
    return mapping[row["tumor_type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    mapping = {
        "1": "G1",
        "2": "G2",
        "3": "G3",
        "4": "G4",
    }
    value = row["who_grade"]
    if value is None:
        return None
    return mapping[str(value)]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["Sex"]]


def age(row):
    return float(row["age (years)"])
