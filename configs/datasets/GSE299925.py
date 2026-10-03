def dataset_id(row):
    return "GSE299925"


def description(row):
    return (
        "Epigenome analysis of precursor lesions of endometrial "
        "endometrioid carcinoma (Cancer Institute Hospital, JFCR)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "AEH": "Atypical endometrial hyperplasia",
        "NAEH": "Endometrial hyperplasia without atypia",
        "APA": "Atypical polypoid adenomyoma",
        "G1": "Endometrioid carcinoma, FIGO grade 1",
        "G2": "Endometrioid carcinoma, FIGO grade 2",
        "Mixed": "Mixed carcinoma of the endometrium",
    }
    return mapping[row["Source"]]


def methylation_class(row):
    mapping = {
        "AEH": "EIN",
        "NAEH": "ENDOM_HYP_NOATY",
        "APA": "APA",
        "G1": "ENDOM_EC",
        "G2": "ENDOM_EC",
        "Mixed": "ENDOM_MIXC",
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


def tumor_grade(row):
    mapping = {"G1": "G1", "G2": "G2"}
    return mapping.get(row["Source"])


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
