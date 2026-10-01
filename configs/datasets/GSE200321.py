def dataset_id(row):
    return "GSE200321"


def description(row):
    return (
        "Epigenome analysis of formalin-fixed paraffin-embedded (FFPE) "
        "meningioma samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["histology"]


def methylation_class(row):
    mapping = {
        "ANAPLASTIC MENINGIOMA": "MNG_MAL",
        "ATYPICAL AND INVASIVE MENINGIOMA": "MNG",
        "ATYPICAL MENINGIOMA": "MNG",
        "CHORDOID AND ATYPICAL": "MNG",
        "CHORDOID MENINGIOMA": "MNG",
        "INVASIVE MENINGIOMA": "MNG",
        "MENINGOTHELIAL MENINGIOMA": "MNG",
        "TRANSITIONAL MENINGIOMA": "MNG",
    }
    return mapping[row["histology"]]


def sample_site(row):
    return "Meninges"


def primary_site(row):
    return "Meninges"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {"1": "G1", "2": "G2", "3": "G3"}
    return mapping[str(row["grade"])]


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]
