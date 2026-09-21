def dataset_id(row):
    return "GSE315367"


def description(row):
    return "Longitudinal AML samples"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease status"]
    mapping = {
        "Diagnosis": "Diagnosis",
        "Relapse": "Relapse",
        "Remission1": "Remission1",
        "Remission2": "Remission2",
    }
    return mapping[value]


def methylation_class(row):
    tissue = str(row["tissue"]).lower()
    disease_status = str(row["disease status"]).lower()
    if "remission" in disease_status or "relapse" in disease_status:
        if "blood" in tissue:
            return "CONTR_BLOOD"
        if "bone marrow" in tissue:
            return "CONTR_MARROW"
    if "diagnosis" in disease_status:
        return "AML"
    return None


def sample_site(row):
    return row["tissue"]


def sex(row):
    return row["Sex"]


def age(row):
    return row["age at diagnosis"]
