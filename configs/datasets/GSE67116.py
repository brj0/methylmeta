def dataset_id(row):
    return "GSE67116"


def description(row):
    return (
        "Genome-wide DNA methylation profiling of endometrial hyperplasias, "
        "primary cancers and metastases"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["primary disease dx"]


def methylation_class(row):
    mapping = {
        "Endometrial cancer": "ENDOM_CA",
        "Endometrial carcinoma cell line": "ENDOM_CA",
        "Endometrial hyperplasia": "EMH",
    }
    return mapping[row["primary disease dx"]]


def sample_site(row):
    mapping = {
        "Abdomunal tissue": "Abdominal tissue",
        "Gastrointertinal tissue": "Gastrointestinal tissue",
        "Douglasi": "Pouch of Douglas",
    }
    return mapping.get(row["tissue site"], row["tissue site"])


def primary_site(row):
    return "Endometrium"


def sample_type(row):
    mapping = {
        "Primary": "primary",
        "Metastasis": "metastasis",
        "Hyperplasia": "primary",
        "Cell line ECC-1": "primary",
        "Cell line Hec-1-b": "primary",
    }
    return mapping[row["tumor.type"]]


def material_type(row):
    mapping = {
        "Cell-line": "cell_line",
        "Hyperplasia": "tissue",
        "Tumor": "tissue",
    }
    return mapping[row["sample type"]]


def sex(row):
    return "female"
