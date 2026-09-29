def dataset_id(row):
    return "GSE216313"


def description(row):
    return (
        "Towards optimization of precision oncology in metastatic uterine "
        "tumors: invasive tumor front of lung metastases from uterine "
        "adenocarcinoma and uterine leiomyosarcoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"]


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "Invasive tumor front (ITF) of lung metastatic uterine "
        "adenocarcinoma": "ENDOM_CA",
        "Invasive tumor front (ITF) of lung metastatic uterine "
        "leiomyosarcoma": "UT_LMS",
    }
    return mapping[value]


def sample_site(row):
    return "Lung"


def primary_site(row):
    return "Uterus"


def sample_type(row):
    return "metastasis"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
