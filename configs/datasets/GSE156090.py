def dataset_id(row):
    return "GSE156090"


def description(row):
    return (
        "Methylation profiling of pediatric choroid plexus tumors "
        "(FFPE and fresh frozen tissue)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Choroid plexus tumor"


def methylation_class(row):
    return "PLEX_PED"


def sample_site(row):
    return "Choroid plexus"


def primary_site(row):
    return "Choroid plexus"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["Description"]]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
