def dataset_id(row):
    return "GSE219033"


def description(row):
    return (
        "DNA methylation (EPIC) of germ cell tumor-related somatic-type "
        "malignancies, teratomas and yolk sac tumors"
    )


def sample_id(row):
    value = row["Sample_ID"]
    if value.endswith(".idat"):
        value = value[:-5]
    if value.endswith("_green"):
        return value[:-6]
    if value.endswith("_red"):
        return value[:-4]
    return value


def diagnosis(row):
    mapping = {
        "STM-adenocarcinoma": "Somatic-type malignancy, adenocarcinoma",
        "STM-rhabdomyosarcoma": "Somatic-type malignancy, rhabdomyosarcoma",
        "Teratoma": "Teratoma",
        "Yolk-sac tumor": "Yolk sac tumor",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "STM-adenocarcinoma": "STMAD",
        "STM-rhabdomyosarcoma": "STMRMS",
        "Teratoma": "TER",
        "Yolk-sac tumor": "YST",
    }
    return mapping[row["tissue"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
