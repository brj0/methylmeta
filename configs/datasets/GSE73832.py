def dataset_id(row):
    return "GSE73832"


def description(row):
    return (
        "Small intestinal neuroendocrine tumours and normal tissue controls "
        "(Karpathakis et al. 2016)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["lesion"] == "normal":
        mapping = {
            "small intestine": "small intestine",
            "liver": "liver",
            "colon": "colon",
            "appendix": "appendix",
            "mes_omentum": "omentum",
        }
        site = mapping.get(row["sample site"])
        return "Normal " + site if site else None
    mapping = {
        "small intestine": "Small intestinal neuroendocrine tumour",
        "colon": "Colorectal neuroendocrine neoplasm",
        "appendix": "Neuroendocrine tumour of the appendix",
        "gastric": "Gastric neuroendocrine neoplasm",
        "cell line": "Small intestinal neuroendocrine tumour cell line",
    }
    return mapping.get(row["primary site"], "Neuroendocrine tumour")


def methylation_class(row):
    if row["lesion"] == "normal":
        mapping = {
            "small intestine": "CTRL_SI",
            "liver": "CTRL_LIV",
            "colon": "CTRL_COL",
            "appendix": "CTRL_APP",
            "mes_omentum": "CTRL_OMENT",
        }
        return mapping.get(row["sample site"])
    mapping = {
        "small intestine": "SI_NET",
        "colon": "CR_NET",
        "appendix": "APP_NET",
        "gastric": "GAST_NET",
        "cell line": "SI_NET",
        None: "SI_NET",
    }
    return mapping.get(row["primary site"])


def sample_site(row):
    mapping = {"cell line": None, "normal": None}
    return mapping.get(row["sample site"], row["sample site"])


def primary_site(row):
    mapping = {"cell line": None}
    return mapping.get(row["primary site"], row["primary site"])


def sample_type(row):
    lesion = row["lesion"]
    mapping = {"normal": "control", "cell line": None}
    return mapping.get(lesion, lesion)


def material_type(row):
    mapping = {"FF": "tissue", "FFPE": "tissue", "cell line": "cell_line"}
    return mapping[row["source tissue type"]]


def preservation(row):
    mapping = {"FF": "FROZEN", "FFPE": "FFPE", "cell line": None}
    return mapping[row["source tissue type"]]


def tumor_grade(row):
    mapping = {
        "1": "G1",
        "2": "G2",
        "3": "G3",
        "cell line": None,
        "normal": None,
        "unk": None,
        None: None,
    }
    return mapping[row["grade"]]


def sex(row):
    mapping = {"F": "female", "M": "male", "cell line": None, None: None}
    return mapping[row["gender"]]


def age(row):
    value = row["age"]
    return float(value) if value is not None else None
