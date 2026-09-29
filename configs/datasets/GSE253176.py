def dataset_id(row):
    return "GSE253176"


def description(row):
    return (
        "DNA methylation patterns facilitate tracing the origin of "
        "neuroendocrine neoplasms"
    )


def _organ(row):
    mapping = {
        "NEN appendix": "Appendix",
        "NEN ileum": "Ileum",
        "NEN duodenum": "Duodenum",
        "NEN colon ascending": "Ascending colon",
        "NEN colon sigmoid": "Sigmoid colon",
        "NEN colon transverse": "Transverse colon",
        "NEN rectum": "Rectum",
        "NEN stomach": "Stomach",
        "NEN pancreas": "Pancreas",
        "NEN liver metastasis": "Liver",
        "hepatic NEN": "Liver",
        "EXCLUDE______hepatic NEN": "Liver",
        "Merkel cell carcinoma": "Skin",
        "Pulmonary carcinoid": "Lung",
        "Pulmonal NEC": "Lung",
    }
    return mapping[row["Source"]]


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "NEN appendix": "Neuroendocrine neoplasm of the appendix",
        "NEN ileum": "Neuroendocrine neoplasm of the ileum",
        "NEN duodenum": "Neuroendocrine neoplasm of the duodenum",
        "NEN colon ascending": "Neuroendocrine neoplasm of the ascending colon",
        "NEN colon sigmoid": "Neuroendocrine neoplasm of the sigmoid colon",
        "NEN colon transverse": "Neuroendocrine neoplasm of the transverse colon",
        "NEN rectum": "Neuroendocrine neoplasm of the rectum",
        "NEN stomach": "Neuroendocrine neoplasm of the stomach",
        "NEN pancreas": "Neuroendocrine neoplasm of the pancreas",
        "NEN liver metastasis": "Neuroendocrine neoplasm metastatic to the liver",
        "hepatic NEN": "Hepatic neuroendocrine neoplasm",
        "EXCLUDE______hepatic NEN": "Hepatic neuroendocrine neoplasm",
        "Merkel cell carcinoma": "Merkel cell carcinoma",
        "Pulmonary carcinoid": "Carcinoid tumour of the lung",
        "Pulmonal NEC": "Neuroendocrine carcinoma of the lung",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    # A liver metastasis keeps the class of its (unrecorded) primary, so no
    # methylation class can be assigned to it.
    mapping = {
        "NEN appendix": "APP_NET",
        "NEN ileum": "SI_NET",
        "NEN duodenum": "DUO_NET",
        "NEN colon ascending": "CR_NET",
        "NEN colon sigmoid": "CR_NET",
        "NEN colon transverse": "CR_NET",
        "NEN rectum": "CR_NET",
        "NEN stomach": "GAST_NET",
        "NEN pancreas": "PAN_NET",
        "NEN liver metastasis": None,
        "hepatic NEN": "LIV_NET",
        "EXCLUDE______hepatic NEN": "LIV_NET",
        "Merkel cell carcinoma": "MCC",
        "Pulmonary carcinoid": "LU_NET",
        "Pulmonal NEC": "LU_NEC",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return _organ(row)


def primary_site(row):
    if row["Source"] == "NEN liver metastasis":
        return None
    return _organ(row)


def sample_type(row):
    mapping = {"NEN liver metastasis": "metastasis"}
    return mapping.get(row["Source"], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age_years"])
