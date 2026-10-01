def dataset_id(row):
    return "GSE327663"


def description(row):
    return (
        "Epigenetic alterations in cervical intraepithelial neoplasia of "
        "women with African and European ancestry"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Cervical intraepithelial neoplasia"


def methylation_class(row):
    return "CIN"


def sample_site(row):
    return "Uterine cervix"


def primary_site(row):
    return "Uterine cervix"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
