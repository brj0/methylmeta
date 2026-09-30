def dataset_id(row):
    return "E-MTAB-9297"


def description(row):
    return (
        "Patient-derived primary cultures and tumours of paediatric "
        "high-grade glioma and DIPG profiled by methylation array"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    classifier = row["Characteristics[methylation classifier (mnp v11b4)]"]
    if classifier.startswith("CONTR"):
        return "normal brain tissue"
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "A IDH, HG": "ASTRO_IDH_HG",
        "CONTR, HEMI": "CTRL_BRAIN",
        "DMG, K27": "DMG_K27",
        "GBM, G34": "DHG_G34",
        "GBM, MES": "GBM_MES",
        "GBM, MYCN": "GBM_MYCN",
        "GBM, RTK I": "GBM_RTK_1",
        "GBM, RTK II": "GBM_RTK_2",
        "GBM, RTK III": "GBM_RTK_3",
        "IHG": "IHG",
        "LGG, PA PF": "LGG_PA_PF",
        "MNG": "MNG",
        "PLEX, PED B": "PLEX_PED_B",
        "PXA": "PXA",
    }
    classifier = row["Characteristics[methylation classifier (mnp v11b4)]"]
    return mapping[classifier]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "brain"


def sample_type(row):
    classifier = row["Characteristics[methylation classifier (mnp v11b4)]"]
    mapping = {
        "CONTR, HEMI": "control",
    }
    return mapping.get(classifier, "primary")


def material_type(row):
    mapping = {
        "cell": "cell_line",
        "organism part": "tissue",
    }
    return mapping[row["Material Type"]]
