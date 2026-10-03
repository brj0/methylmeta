def dataset_id(row):
    return "GSE243303"


def description(row):
    return (
        "Precursor lesions of endometrial endometrioid carcinoma: atypical "
        "and non-atypical endometrial hyperplasia"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "AEH": "Atypical endometrial hyperplasia",
        "NAEH": "Endometrial hyperplasia without atypia",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "AEH": "EIN",
        "NAEH": "ENDOM_HYP_NOATY",
    }
    return mapping[row["Source"]]


def sample_site(row):
    return row["anatomical site"]


def primary_site(row):
    return row["anatomical site"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
