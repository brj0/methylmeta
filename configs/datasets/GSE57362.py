def dataset_id(row):
    return "GSE57362"


def description(row):
    return "A DNA methylation atlas of the human eye and its diseases"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    disease = row["disease state"]
    if disease == "normal":
        return "Normal " + row["tissue"].lower()
    mapping = {
        "Retinoblastoma": "Retinoblastoma",
        "Retinoblastoma blood": "Normal blood",
        "Uveal melanoma": "Uveal melanoma",
        "diabetic retinopathy": "Diabetic retinopathy fibrovascular membrane",
        "non-proliferative diabetic retinopathy": (
            "Non-proliferative diabetic retinopathy neuroretina"
        ),
        "proliferative vitreoretinopathy": (
            "Proliferative vitreoretinopathy membrane"
        ),
    }
    return mapping[disease]


def methylation_class(row):
    mapping = {
        "normal": "CTRL_EYE",
        "Retinoblastoma": "RB",
        "Retinoblastoma blood": "CTRL_BLOOD",
        "Uveal melanoma": "UVE_MEL",
        "diabetic retinopathy": "CTRL_EYE",
        "non-proliferative diabetic retinopathy": "CTRL_EYE",
        "proliferative vitreoretinopathy": "CTRL_EYE",
    }
    return mapping[row["disease state"]]


def sample_type(row):
    mapping = {
        "normal": "control",
        "Retinoblastoma": "primary",
        "Retinoblastoma blood": "control",
        "Uveal melanoma": "primary",
        "diabetic retinopathy": None,
        "non-proliferative diabetic retinopathy": None,
        "proliferative vitreoretinopathy": None,
    }
    return mapping[row["disease state"]]


def sample_site(row):
    mapping = {
        "Blood": "Blood",
        "Choroid and ciliary muscle": "Choroid and ciliary body",
        "Eye": "Eye",
        "Retina": "Retina",
        "Sclera": "Sclera",
        "Uveal melanoma": "Uvea",
        "eye fibrovascular membranes": "Retina",
        "eye membrane": "Retina",
        "neuroretina": "Retina",
        "retina": "Retina",
        "sclera": "Sclera",
        "uvea": "Uvea",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return row["Source"]


def material_type(row):
    mapping = {"Blood": "blood", "Eye": "tissue"}
    return mapping[row["Source"]]
