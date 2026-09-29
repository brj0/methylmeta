def _tumor(row):
    return row["Title"].split("_")[0]


def _origin(row):
    return row["Title"].split("_")[1]


def dataset_id(row):
    return "GSE217384"


def description(row):
    return (
        "DNA methylation-based classifier separating intrahepatic "
        "cholangiocarcinoma from hepatic metastases of pancreatic ductal "
        "adenocarcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "PAAD": "Pancreatic ductal adenocarcinoma",
        "iCCA": "Intrahepatic cholangiocarcinoma",
    }
    return mapping[_tumor(row)]


def methylation_class(row):
    mapping = {
        "PAAD": "PAN_CA",
        "iCCA": "CCA_INT",
    }
    return mapping[_tumor(row)]


def sample_type(row):
    mapping = {
        "prim": "primary",
        "meta": "metastasis",
    }
    return mapping[_origin(row)]


def sample_site(row):
    mapping = {
        ("PAAD", "prim"): "Pancreas",
        ("PAAD", "meta"): "Liver",
        ("iCCA", "prim"): "Liver",
        ("iCCA", "meta"): "Liver",
    }
    return mapping[(_tumor(row), _origin(row))]


def primary_site(row):
    mapping = {
        "PAAD": "Pancreas",
        "iCCA": "Liver",
    }
    return mapping[_tumor(row)]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
