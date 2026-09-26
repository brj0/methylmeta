def dataset_id(row):
    return "GSE175769"


def description(row):
    return (
        "Multi-site tumor sampling of malignant pleural mesothelioma "
        "(MesoHET cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["histology (type)"]
    mapping = {
        "Biphasic": "Biphasic malignant pleural mesothelioma",
        "Epitheloid": "Epithelioid malignant pleural mesothelioma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["histology (type)"]
    mapping = {
        "Biphasic": "MESOT_BIPHASIC",
        "Epitheloid": "MESOT_EPITH",
    }
    return mapping[value]


def sample_site(row):
    value = row["tumor sample localisation"]
    mapping = {
        "Apex": "Apex",
        "Apx (Highest metabolic site detected by PET scan)": "Apex",
        "Costo-diaphragmatic": "Costo-diaphragmatic",
    }
    return mapping[value]


def primary_site(row):
    return "Pleura"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def tumor_grade(row):
    who = row["grade (who 2021)"]
    if who is not None:
        mapping = {"high": "high-grade", "low": "low-grade"}
        return mapping[who.lower()]
    value = row["grade (nuclear atypia)"]
    return {"2": "G2", "3": "G3"}.get(value)


def sex(row):
    value = row["gender"]
    mapping = {"Female": "female", "Male": "male"}
    return mapping[value]


def age(row):
    return float(row["age at diagnostic"])
