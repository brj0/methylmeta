def dataset_id(row):
    return "GSE317378"


def description(row):
    return (
        "Infant medulloblastoma (<5 years): integrated biomarker and "
        "treatment correlates of prognosis, multi-national cohorts"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # Abbreviations of the medulloblastoma histology of the sampled tumour.
    hist_label = {
        "CLA": "medulloblastoma, classic",
        "DN": "medulloblastoma, desmoplastic/nodular",
        "LCA": "medulloblastoma, large cell/anaplastic",
        "MBEN": "medulloblastoma with extensive nodularity",
    }
    return hist_label.get(row["histopathology"], "medulloblastoma")


def methylation_class(row):
    # The cohort is infant medulloblastoma (<5 years at diagnosis), so its
    # SHH cases are infant SHH tumours, i.e. methylation class MB_SHH_INF.
    mol_grp_class = {
        "Grp3": "MB_G3",
        "Grp4": "MB_G4",
        "SHH": "MB_SHH_INF",
    }
    return mol_grp_class[row["principal_mol_grp"]]


def sample_site(row):
    return "Cerebellum"


def primary_site(row):
    return "Cerebellum"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"0": "female", "1": "male"}
    return mapping[str(row["male_sex"])]


def age(row):
    return float(row["age_diagnosis(yrs)"])
