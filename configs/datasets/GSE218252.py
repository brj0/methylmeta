def dataset_id(row):
    return "GSE218252"


def description(row):
    return (
        "DNA methylation profiling of giant cell granulomas of the jaws, "
        "cherubism and their giant cell-rich histological mimics (2023)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    mapping = {
        "Aneurysmal bone cyst": "ABC",
        "Central giant cell granuloma of the jaws": "GCG",
        "Cherubism": "CHERUB",
        "Chondroblastoma": "CHONDBL",
        "Giant cell tumor of the bone": "GCTB",
        "Non-ossifying fibroma": "NOF",
        "Peripheral giant cell granuloma of the jaws": "GCG",
    }
    return mapping[row["Description"]]


def sample_site(row):
    mapping = {
        "Aneurysmal bone cyst": "Bone",
        "Central giant cell granuloma of the jaws": "Jaw",
        "Cherubism": "Jaw",
        "Chondroblastoma": "Bone",
        "Giant cell tumor of the bone": "Bone",
        "Non-ossifying fibroma": "Bone",
        "Peripheral giant cell granuloma of the jaws": "Jaw",
    }
    return mapping[row["Description"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["material"]
