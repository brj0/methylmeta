def dataset_id(row):
    return "GSE193000"


def description(row):
    return (
        "Primary osteosarcomas and normal bone tissue profiled with the "
        "Illumina HM450K methylation array"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["subtypes"]
    mapping = {
        "bone": "normal bone",
        "osteoblastic": "osteoblastic osteosarcoma",
        "osteblastic, condroblastic": (
            "osteosarcoma, mixed osteoblastic and chondroblastic"
        ),
        "condroblastic": "chondroblastic osteosarcoma",
        "fibroblastic": "fibroblastic osteosarcoma",
        "parosteal": "parosteal osteosarcoma",
        "telangectasic": "telangiectatic osteosarcoma",
        "sarcoma pleomorphic with osteoid": "pleomorphic sarcoma with osteoid",
    }
    return mapping.get(value, "osteosarcoma")


def methylation_class(row):
    mapping = {
        "bone": "CTRL_BONE",
        "osteoblastic": "OS_CONV",
        "osteblastic, condroblastic": "OS_CONV",
        "condroblastic": "OS_CONV",
        "fibroblastic": "OS_CONV",
        "parosteal": "OS_PAROST",
        "telangectasic": "OS_TELEANG",
        "sarcoma pleomorphic with osteoid": "OS",
        None: None,
    }
    return mapping[row["subtypes"]]


def sample_site(row):
    return "Bone"


def primary_site(row):
    return "Bone"


def sample_type(row):
    mapping = {
        "bone": "control",
        "osteosarcoma": "primary",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def sex(row):
    return row["Sex"]


def age(row):
    value = row["age (years)"]
    if value is None:
        return None
    return float(value)
