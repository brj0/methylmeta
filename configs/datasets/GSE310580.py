def dataset_id(row):
    return "GSE310580"


def description(row):
    return (
        "Mucinous ovarian carcinoma, mucinous borderline ovarian tumours and "
        "extraovarian mucinous metastases"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    tumor_type = row["tumor type"]
    if tumor_type != "extra ovarian metastasis":
        return tumor_type
    mapping = {
        "CRC": "colorectal carcinoma",
        "STAD": "gastric adenocarcinoma",
        "PAAD": "pancreatic ductal adenocarcinoma",
        "CHOL": "cholangiocarcinoma",
        "LUAD": "lung adenocarcinoma",
        "ESCA": "esophageal adenocarcinoma",
        "Ileum": "jejunoileal adenocarcinoma",
        "LAMN": "low-grade appendiceal mucinous neoplasm",
        "ApAD": "appendiceal adenocarcinoma",
        "Appendiceal Mucinous AC": "appendiceal mucinous adenocarcinoma",
        "Appendiceal Goblet Cell AC": "appendiceal goblet cell adenocarcinoma",
    }
    return "Metastatic " + mapping[row["primary location"]]


def methylation_class(row):
    tumor_type = row["tumor type"]
    if tumor_type == "primary mucinous ovarian cancer":
        return "OVA_MUC_CA"
    if tumor_type == "mucinous borderline ovarian tumor":
        return "OVA_MUC_BOT"
    mapping = {
        "CRC": "CR_CA",
        "STAD": "GAST_ADCA",
        "PAAD": "PDAC",
        "CHOL": "CCA",
        "LUAD": "LU_ADCA",
        "ESCA": "ESO_ADCA",
        "Ileum": "JEJIL_ADCA",
        "LAMN": "APP_MUC_NEO",
        "ApAD": "APP_ADCA",
        "Appendiceal Mucinous AC": "APP_ADCA",
        "Appendiceal Goblet Cell AC": "APP_GC_ADCA",
    }
    return mapping[row["primary location"]]


def primary_site(row):
    mapping = {
        "ovary": "Ovary",
        "CRC": "Colon / rectum",
        "STAD": "Stomach",
        "PAAD": "Pancreas",
        "CHOL": "Bile duct",
        "LUAD": "Lung",
        "ESCA": "Esophagus",
        "Ileum": "Jejunum / ileum",
        "LAMN": "Appendix",
        "ApAD": "Appendix",
        "Appendiceal Mucinous AC": "Appendix",
        "Appendiceal Goblet Cell AC": "Appendix",
    }
    return mapping[row["primary location"]]


def sample_type(row):
    mapping = {
        "primary mucinous ovarian cancer": "primary",
        "mucinous borderline ovarian tumor": "primary",
        "extra ovarian metastasis": "metastasis",
    }
    return mapping[row["tumor type"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FF": "FROZEN", "FFPE": "FFPE"}
    return mapping[row["tissue type"]]
