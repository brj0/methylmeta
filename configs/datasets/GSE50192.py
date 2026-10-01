def dataset_id(row):
    return "GSE50192"


def description(row):
    return (
        "DNA methylome profiling of 17 human somatic autopsy tissues "
        "(Lokk et al., 2014)"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    return row["tissue"].replace("_", " ")


def sample_site(row):
    return row["tissue"].replace("_", " ")


def methylation_class(row):
    mapping = {
        "Adipose_abdominal": "CTRL_ADIPOSE",
        "Adipose_subcutaenous": "CTRL_ADIPOSE",
        "Aorta_abdominal": "CTRL_NOS",
        "Aorta_thoracic": "CTRL_NOS",
        "Bladder": "CTRL_BLA",
        "Bone": "CTRL_BONE",
        "Bone marrow_red": "CTRL_MARROW",
        "Bone marrow_yellow": "CTRL_MARROW",
        "Coronary_artery": "CTRL_NOS",
        "Gallbladder": "CTRL_GB",
        "Gastric_mucosa": "CTRL_GAST",
        "Ischiatic_nerve": "CTRL_NERVE",
        "Joint_cartilage": "CTRL_CART",
        "Lymph_node": "CTRL_LYMPH",
        "Medulla_oblongata": "CTRL_BRAIN",
        "Splenic_artery": "CTRL_VESSEL",
        "Tonsils": "CTRL_LYMPH",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    return "control"


def material_type(row):
    return "tissue"


def sex(row):
    return row["gender"]
