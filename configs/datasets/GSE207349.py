def dataset_id(row):
    return "GSE207349"


def description(row):
    return (
        "Transcriptome and DNA methylome analyses reveal underlying "
        "mechanisms for the racial disparity in uterine fibroids"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "Fibroid": "Uterine leiomyoma (fibroid)",
        "Myometrium": "Normal myometrium",
    }
    return mapping[row["tissue type"]]


def methylation_class(row):
    mapping = {
        "Fibroid": "UT_LEIO",
        "Myometrium": "CTRL_MYOMETR",
    }
    return mapping[row["tissue type"]]


def sample_site(row):
    return "Uterus"


def primary_site(row):
    return "Uterus"


def sample_type(row):
    mapping = {
        "Fibroid": "primary",
        "Myometrium": "control",
    }
    return mapping[row["tissue type"]]


def material_type(row):
    return "tissue"
