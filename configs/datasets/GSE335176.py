def dataset_id(row):
    return "GSE335176"


def description(row):
    return (
        "DNA methylation profiling of 10 DMPA-associated WHO grade 1 "
        "meningiomas"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "meningioma, " + row["histologic subtype"]


def methylation_class(row):
    mapping = {
        "Ben-2": "MNG_BEN_2",
        "Ben-3": "MNG_BEN_3",
        "unclassified": "MNG",
    }
    return mapping[row["heidelberg methylation class"]]


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
    mapping = {1: "G1"}
    return mapping[row["who grade"]]


def sex(row):
    return "female"
