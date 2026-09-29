def dataset_id(row):
    return "GSE252130"


def description(row):
    return (
        "DNA methylation classifier to diagnose pancreatic ductal "
        "adenocarcinoma metastases from different anatomical sites"
    )


def _tumor_code(title):
    parts = title.split("_")
    if parts[0] == "Organoid":
        return parts[1]
    return parts[0]


def _is_organoid(row):
    return row["tissue type"] == "organoid"


def _is_metastatic(title):
    return "meta" in title


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    mapping = {
        "PAAD": "PAN_CA",
        "LUAD": "LU_ADCA",
        "UCEC": "ENDOM_CA",
        "STAD": "GAST_ADCA",
        "BRCA": "BR_CA",
        "PRAD": "PROS_ADCA",
        "PMOC": "OVA_MUC_CA",
        "UNKNOWN": "CUP",
    }
    return mapping[_tumor_code(row["Title"])]


def primary_site(row):
    mapping = {
        "PAAD": "Pancreas",
        "LUAD": "Lung",
        "UCEC": "Uterus",
        "STAD": "Stomach",
        "BRCA": "Breast",
        "PRAD": "Prostate",
        "PMOC": "Ovary",
        "UNKNOWN": None,
    }
    return mapping[_tumor_code(row["Title"])]


def sample_site(row):
    title = row["Title"].lower()
    if "brain" in title:
        return "Brain"
    if "spleen" in title:
        return "Spleen"
    if "peritoneal" in title:
        return "Peritoneum"
    if "lymph_node" in title or "lymphnode" in title:
        return "Lymph node"
    if "lung" in title:
        return "Lung"
    if "liver" in title:
        return "Liver"
    return None


def sample_type(row):
    if _is_organoid(row):
        return "metastasis" if _is_metastatic(row["Title"]) else "primary"
    mapping = {"metastasis": "metastasis", "primary": "primary"}
    return mapping[row["tissue type"]]


def material_type(row):
    if _is_organoid(row):
        return "cell_line"
    return "tissue"


def preservation(row):
    return "FFPE"
