def dataset_id(row):
    return "GSE287994"


def description(row):
    return (
        "Epigenome-wide methylation study of cervical pre-invasive (CIN3) "
        "and invasive disease in exfoliated cervical cells"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Benign cervical sample": "Benign cervical epithelium",
        "CIN3 or Cancer sample": "CIN3 or cervical cancer",
    }
    return mapping[row["cell type"]]


def methylation_class(row):
    mapping = {
        "Benign cervical sample": "CTRL_CERV",
        "CIN3 or Cancer sample": "CERV_CA",
    }
    return mapping[row["cell type"]]


def sample_site(row):
    return "Cervix"


def primary_site(row):
    return "Cervix"


def sample_type(row):
    mapping = {
        "Benign cervical sample": "control",
        "CIN3 or Cancer sample": "primary",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]
