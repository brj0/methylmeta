def dataset_id(row):
    return "E-MTAB-9282"


def description(row):
    return (
        "Methylation profiling of DIPG tumours and patient-derived models "
        "from the BIOMEDE phase II trial"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "CNS_NB_FOXR2": "CNS_NB_FOXR2",
        "DMG_K27": "DMG_K27",
        "GBM_G34": "DHG_G34",
        "GBM_MYCN": "GBM_MYCN",
        "GBM_RTK_I": "GBM_RTK_1",
        "GBM_RTK_III": "GBM_RTK_3",
        "PLEX_PED_B": "PLEX_PED_B",
    }
    return mapping[row["Characteristics[methylation group]"]]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "brain"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "cell culture": "cell_line",
        "in vivo neoplasm": "tissue",
        "organoid culture": "cell_line",
        "xenograft": "tissue",
    }
    return mapping[row["Characteristics[growth condition]"]]
