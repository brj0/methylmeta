def dataset_id(row):
    return "GSE119462"


def description(row):
    return "Methylation profiles of benign and malignant primary bone tumours"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["disease"]
    mapping = {
        "Aneurysmal_Bone_Cyst": "Aneurysmal bone cyst",
        "Chondroblastoma": "Chondroblastoma",
        "Chondromyxoid_Fibroma": "Chondromyxoid fibroma",
        "Chondrosarcoma": "Chondrosarcoma",
        "Chordoma": "Chordoma",
        "Nonossifying_Fibroma": "Non-ossifying fibroma",
        "Osteoblastoma": "Osteoblastoma",
    }
    return mapping.get(value, value)


def methylation_class(row):
    value = row["disease"]
    mapping = {
        "Aneurysmal_Bone_Cyst": "ABC",
        "Chondroblastoma": "CHONDBL",
        "Chondromyxoid_Fibroma": "CMF",
        "Chondrosarcoma": "CSA",
        "Chordoma": "CHORD",
        "Nonossifying_Fibroma": "NOF",
        "Osteoblastoma": "OSTEOBL",
        None: None,
    }
    return mapping[value]


def sample_site(row):
    return "Bone"


def primary_site(row):
    return "Bone"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Source"]
    mapping = {"Fresh frozen tumour": "FROZEN"}
    return mapping[value]
