def dataset_id(row):
    return "GSE49656"


def description(row):
    return (
        "Cholangiocarcinoma (Opisthorchis viverrini-related and unrelated) "
        "with normal bile duct, Chan-On 2013"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    mapping = {
        "CCA_Tumor_Sample": "Cholangiocarcinoma",
        "Normal Bile Duct": "Normal bile duct tissue",
        "Technical_Control": None,
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "CCA_Tumor_Sample": "CCA",
        "Normal Bile Duct": "CTRL_BD",
        "Technical_Control": "CTRL_NOS",
    }
    return mapping[row["Source"]]


def sample_type(row):
    mapping = {
        "CCA_Tumor_Sample": "primary",
        "Normal Bile Duct": "control",
        "Technical_Control": None,
    }
    return mapping[row["Source"]]


def material_type(row):
    mapping = {
        "CCA_Tumor_Sample": "tissue",
        "Normal Bile Duct": "tissue",
        "Technical_Control": None,
    }
    return mapping[row["Source"]]


def sample_site(row):
    mapping = {
        "CCA_Tumor_Sample": "Bile duct",
        "Normal Bile Duct": "Bile duct",
        "Technical_Control": None,
    }
    return mapping[row["Source"]]


def primary_site(row):
    mapping = {
        "CCA_Tumor_Sample": "Bile duct",
        "Normal Bile Duct": "Bile duct",
        "Technical_Control": None,
    }
    return mapping[row["Source"]]
