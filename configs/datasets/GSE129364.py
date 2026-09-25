def dataset_id(row):
    return "GSE129364"


def description(row):
    return (
        "Colorectal adenomas with and without recurrence and normal "
        "colon mucosa, 2019"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    diagnosis = row["sample type"]
    histology = row["histology"]
    if histology:
        return f"{diagnosis}, {histology.lower()}"
    return diagnosis


def methylation_class(row):
    mapping = {
        "colorectal adenoma": "CR_AD",
        "normal colon mucosa": "CTRL_COL",
    }
    return mapping[row["sample type"]]


def sample_type(row):
    mapping = {
        "normal colon mucosa": "control",
        "colorectal adenoma without recurrence": "primary",
        "primary colorectal adenoma with recurrence": "primary",
        "recurrent colorectal adenoma": "recurrence",
    }
    return mapping[row["Source"]]


def sample_site(row):
    mapping = {
        "Ascending": "Ascending colon",
        "Cecum": "Cecum",
        "Descending": "Descending colon",
        "Hepatic flexure": "Hepatic flexure of colon",
        "Rectum": "Rectum",
        "Sigmoid": "Sigmoid colon",
        "Transverse": "Transverse colon",
    }
    return mapping[row["localization"]]


def primary_site(row):
    return "Colon"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
