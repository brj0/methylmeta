def _organ(row):
    source = row["Source"].lower()
    if "anal" in source:
        return "anal"
    if "cervical" in source:
        return "cervical"
    return None


def dataset_id(row):
    return "GSE186859"


def description(row):
    return (
        "Genome-wide host methylation profiling of anal and cervical carcinoma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    sample_type = row["sample type"]
    organ = _organ(row)
    if organ is None:
        return None
    if sample_type == "Normal":
        return "Normal " + organ + " tissue"
    if sample_type == "AIN3":
        return "Anal squamous intraepithelial neoplasia grade 3"
    if sample_type == "CIN3":
        return "Cervical intraepithelial neoplasia grade 3"
    if sample_type == "Tumor":
        return organ.capitalize() + " squamous cell carcinoma"
    return None


def methylation_class(row):
    sample_type = row["sample type"]
    organ = _organ(row)
    if sample_type == "Normal":
        if organ == "anal":
            return "CTRL_ANAL"
        if organ == "cervical":
            return "CTRL_CERV"
        return "CTRL_NOS"
    if sample_type == "AIN3":
        return "ANAL_SIN"
    if sample_type == "CIN3":
        return "CIN"
    if sample_type == "Tumor":
        if organ == "anal":
            return "ANAL_SCC"
        if organ == "cervical":
            return "CERV_SCC"
    return None


def sample_site(row):
    organ = _organ(row)
    if organ == "anal":
        return "Anal canal"
    if organ == "cervical":
        return "Cervix"
    return None


def primary_site(row):
    organ = _organ(row)
    if organ == "anal":
        return "Anal canal"
    if organ == "cervical":
        return "Cervix"
    return None


def sample_type(row):
    value = row["sample type"]
    mapping = {
        "Normal": "control",
        "AIN3": "primary",
        "CIN3": "primary",
        "Tumor": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"
