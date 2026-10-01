def dataset_id(row):
    return "GSE74104"


def description(row):
    return (
        "Pure testicular germ cell tumor subtypes and matched benign "
        "adjacent testis (NCI, 2016)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # pre-QC subtype of the punched core: BAT = benign adjacent testis,
    # OVTOMA = parthenogenote reference sample (post-QC "REFERENCE")
    mapping = {
        "BAT": "normal testicular tissue",
        "SE": "testicular seminoma",
        "EC": "testicular embryonal carcinoma",
        "TE": "testicular teratoma",
        "YS": "testicular yolk sac tumor",
        "OVTOMA": "parthenogenote reference sample",
    }
    return mapping[row["tgct subtype vs bat (pre-qc)"]]


def methylation_class(row):
    mapping = {
        "BAT": "CTRL_TES",
        "SE": "SEMIN",
        "EC": "TES_EMB_CA",
        # adult (postpubertal-type) pure testicular teratoma
        "TE": "TER_POST",
        "YS": "YST",
        # parthenogenote reference material, no tumor entity
        "OVTOMA": None,
    }
    return mapping[row["tgct subtype vs bat (pre-qc)"]]


def sample_site(row):
    return "Testis"


def primary_site(row):
    return "Testis"


def sample_type(row):
    mapping = {
        "BAT": "control",
        "TGCT": "primary",
        "PARTHENOGENOTE": None,
    }
    return mapping[row["decriptor6"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
