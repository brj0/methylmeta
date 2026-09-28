def dataset_id(row):
    return "GSE200707"


def description(row):
    return (
        "Multi-omic features of oesophageal adenocarcinoma in patients "
        "treated with preoperative neoadjuvant therapy"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "adenocarcinoma of the esophagus and esophagogastric junction"


def methylation_class(row):
    return "ESO_ADCA"


def sample_site(row):
    return "Esophagus"


def primary_site(row):
    return "Esophagus"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"
