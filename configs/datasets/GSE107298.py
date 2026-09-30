def dataset_id(row):
    return "GSE107298"


def description(row):
    return (
        "Methylome-genome interactions in localized prostate cancer "
        "(CPCG cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Prostate adenocarcinoma"


def methylation_class(row):
    return "PROS_ADCA"


def sample_site(row):
    return "Prostate"


def primary_site(row):
    return "Prostate"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"Fresh frozen": "FROZEN"}
    return mapping[row["tissue"]]
