def dataset_id(row):
    return "GSE51820"


def description(row):
    return "DNA methylation profiles of primary ovarian cancers"


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    mapping = {
        "clear cell": "Ovarian clear cell carcinoma",
        "endometrioid": "Ovarian endometrioid carcinoma",
        "mucinous": "Ovarian mucinous carcinoma",
        "serous": "Ovarian serous carcinoma",
        "fallopian tube epithelium": "Normal fallopian tube epithelium",
        "ovarian surface epithelium": "Normal ovarian surface epithelium",
        "normal lymphocyte DNA": "Normal peripheral blood lymphocytes",
        "universally methylated DNA": "Universally methylated DNA control",
        "universally methylated DNA mixed 1:1 with normal lymphocyte DNA": (
            "Universally methylated DNA mixed 1:1 with normal lymphocyte DNA"
        ),
    }
    return mapping[row["histologic type"]]


def methylation_class(row):
    mapping = {
        "clear cell": "OVA_CCC",
        "endometrioid": "OVA_ENDOID_CA",
        "mucinous": "OVA_MUC_CA",
        "serous": "OVA_HGSC",
        "fallopian tube epithelium": "CTRL_TUB",
        "ovarian surface epithelium": "CTRL_OVA",
        "normal lymphocyte DNA": "CTRL_BLOOD",
        "universally methylated DNA": None,
        "universally methylated DNA mixed 1:1 with normal lymphocyte DNA": None,
    }
    return mapping[row["histologic type"]]


def sample_site(row):
    mapping = {
        "ovarian cancer": "Ovary",
        "ovarian surface epithelium": "Ovary",
        "fallopian tube epithelium": "Fallopian tube",
        "normal lymphocyte DNA": "Blood",
        "universally methylated DNA": None,
        "universally methylated DNA mixed 1:1 with normal lymphocyte DNA": None,
    }
    return mapping[row["Source"]]


def primary_site(row):
    mapping = {
        "ovarian cancer": "Ovary",
        "ovarian surface epithelium": "Ovary",
        "fallopian tube epithelium": "Fallopian tube",
        "normal lymphocyte DNA": "Blood",
        "universally methylated DNA": None,
        "universally methylated DNA mixed 1:1 with normal lymphocyte DNA": None,
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {
        "ovarian cancer": "primary",
        "ovarian surface epithelium": "control",
        "fallopian tube epithelium": "control",
        "normal lymphocyte DNA": "control",
        "universally methylated DNA": "control",
        "universally methylated DNA mixed 1:1 with normal lymphocyte DNA": (
            "control"
        ),
    }
    return mapping[row["Source"]]


def material_type(row):
    mapping = {
        "ovarian cancer": "tissue",
        "ovarian surface epithelium": "tissue",
        "fallopian tube epithelium": "tissue",
        "normal lymphocyte DNA": "blood",
        "universally methylated DNA": None,
        "universally methylated DNA mixed 1:1 with normal lymphocyte DNA": None,
    }
    return mapping[row["Source"]]


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {"female": "female", "unknown": None}
    return mapping[row["gender"]]
