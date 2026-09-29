def dataset_id(row):
    return "GSE212370"


def description(row):
    return "Primary and metastatic breast tumors from the AURORA US Network"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    cell_line = row["cell line"]
    if cell_line:
        mapping = {
            "GM12878 lymphoblastoid": "Lymphoblastoid cell line GM12878",
            "HCT116 colon cancer": "Colorectal carcinoma cell line HCT116",
            "IMR-90 fibroblast": "Normal lung fibroblast cell line IMR-90",
        }
        return mapping[cell_line]
    sample_type = row["sample type"]
    if sample_type == "Normal tissue":
        mapping = {
            "Breast": "Normal breast tissue",
            "Brain": "Normal brain tissue",
            "Liver": "Normal liver tissue",
        }
        return mapping[row["tissue"]]
    if sample_type == "Metastatic tumor":
        return "Metastatic breast carcinoma"
    if sample_type == "Primary tumor":
        return "Breast carcinoma"
    return None


def methylation_class(row):
    cell_line = row["cell line"]
    if cell_line:
        mapping = {
            "GM12878 lymphoblastoid": "CTRL_BLOOD",
            "HCT116 colon cancer": "CR_CA",
            "IMR-90 fibroblast": "CTRL_LU",
        }
        return mapping[cell_line]
    sample_type = row["sample type"]
    if sample_type == "Normal tissue":
        mapping = {
            "Breast": "CTRL_BR",
            "Brain": "CTRL_BRAIN_GBM",
            "Liver": "CTRL_LIV",
        }
        return mapping[row["tissue"]]
    if sample_type in {"Primary tumor", "Metastatic tumor"}:
        return "BR_CA"
    return None


def sample_site(row):
    cell_line = row["cell line"]
    if cell_line:
        mapping = {
            "GM12878 lymphoblastoid": "Blood",
            "HCT116 colon cancer": "Colon",
            "IMR-90 fibroblast": "Lung",
        }
        return mapping[cell_line]
    return row["tissue"]


def primary_site(row):
    cell_line = row["cell line"]
    if cell_line:
        mapping = {
            "GM12878 lymphoblastoid": "Blood",
            "HCT116 colon cancer": "Colon",
            "IMR-90 fibroblast": "Lung",
        }
        return mapping[cell_line]
    return "Breast"


def sample_type(row):
    mapping = {
        "Primary tumor": "primary",
        "Metastatic tumor": "metastasis",
        "Normal tissue": "control",
    }
    return mapping.get(row["sample type"])


def material_type(row):
    if row["cell line"]:
        return "cell_line"
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Fresh frozen": "FROZEN"}
    return mapping.get(row["tissue type"])


def sex(row):
    value = row["Sex"]
    if value is None:
        return None
    return value.lower()
