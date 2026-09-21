def dataset_id(row):
    return "GSE217337"


def description(row):
    return "Nasal epithelium EPIC"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Control Nasal Epithelial Cells"


def methylation_class(row):
    return "CTRL_SINO"


def sample_site(row):
    return "Sinonasal"


def sex(row):
    return row["Sex"]
