def dataset_id(row):
    return "GSE229203"


def description(row):
    return (
        "Origins, diversity and clinical relevance of small intestinal "
        "neuroendocrine tumors"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    site = row["primary tumor site"]
    source = row["Source"]
    if source == "Normal":
        return "normal small intestine"
    if source == "Adenoma":
        return {
            "DUODENUM": "duodenal adenoma",
            "ILEUM": "jejunoileal adenoma",
            "JEJUNUM": "jejunoileal adenoma",
        }[site]
    tumour = {
        "DUODENUM": "duodenal neuroendocrine tumour",
        "ILEUM": "ileal neuroendocrine tumour",
        "JEJUNUM": "jejunal neuroendocrine tumour",
    }[site]
    return {
        "Tumor": tumour,
        "Liver metastasis": tumour + ", liver metastasis",
        "Lymph Node": tumour + ", lymph node metastasis",
        "Mesenteric Lymph Node": (
            tumour + ", mesenteric lymph node metastasis"
        ),
    }[source]


def methylation_class(row):
    organ = {
        "DUODENUM": "Duodenum",
        "ILEUM": "Ileum",
        "JEJUNUM": "Jejunum",
    }[row["primary tumor site"]]
    histology = {
        "Tumor": "neuroendocrine tumour",
        "Liver metastasis": "neuroendocrine tumour",
        "Lymph Node": "neuroendocrine tumour",
        "Mesenteric Lymph Node": "neuroendocrine tumour",
        "Adenoma": "adenoma",
        "Normal": "normal",
    }[row["Source"]]
    return {
        ("Duodenum", "neuroendocrine tumour"): "DUO_NET",
        ("Ileum", "neuroendocrine tumour"): "SI_NET",
        ("Jejunum", "neuroendocrine tumour"): "SI_NET",
        ("Duodenum", "adenoma"): "DUO_AD",
        ("Ileum", "adenoma"): "JEJIL_AD",
        ("Jejunum", "adenoma"): "JEJIL_AD",
        ("Duodenum", "normal"): "CTRL_SI",
        ("Ileum", "normal"): "CTRL_SI",
        ("Jejunum", "normal"): "CTRL_SI",
    }[(organ, histology)]


def sample_site(row):
    return {
        "Liver metastasis": "Liver",
        "Lymph Node": "Lymph node",
        "Mesenteric Lymph Node": "Mesenteric lymph node",
    }.get(row["Source"], row["primary tumor site"].title())


def primary_site(row):
    return row["primary tumor site"].title()


def sample_type(row):
    return {
        "Tumor": "primary",
        "Adenoma": "primary",
        "Normal": "control",
        "Liver metastasis": "metastasis",
        "Lymph Node": "metastasis",
        "Mesenteric Lymph Node": "metastasis",
    }[row["Source"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
