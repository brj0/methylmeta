def dataset_id(row):
    return "GSE292896"


def description(row):
    return (
        "Somatic development of Wilms tumour via normal kidneys in "
        "predisposed children"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    mapping = {
        "Blood": "normal blood",
        "Kidney": "Nephroblastoma (Wilms tumour)",
        "Unknown": None,
    }
    return mapping[value]


def methylation_class(row):
    value = row["tissue"]
    mapping = {
        "Blood": "CTRL_BLOOD",
        "Kidney": "WILMS",
        "Unknown": None,
    }
    return mapping[value]


def sample_site(row):
    value = row["tissue"]
    mapping = {"Unknown": None}
    return mapping.get(value, value)


def primary_site(row):
    return "Kidney"


def sample_type(row):
    value = row["tissue"]
    mapping = {
        "Blood": "control",
        "Kidney": "primary",
        "Unknown": None,
    }
    return mapping[value]


def material_type(row):
    value = row["tissue"]
    mapping = {
        "Blood": "blood",
        "Kidney": "tissue",
        "Unknown": None,
    }
    return mapping[value]
