def dataset_id(row):
    return "GSE58783"


def description(row):
    return "Retinoblastoma genome methylation data"


def _is_retina_control(row):
    return "foetal retina" in row["Source"]


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if _is_retina_control(row):
        return "Foetal retina"
    return "Retinoblastoma"


def methylation_class(row):
    if _is_retina_control(row):
        return "CTRL_EYE"
    return "RB"


def sample_type(row):
    if _is_retina_control(row):
        return "control"
    return "primary"


def sample_site(row):
    return "Retina"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
