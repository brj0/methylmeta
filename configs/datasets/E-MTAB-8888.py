def dataset_id(row):
    return "E-MTAB-8888"


def description(row):
    return (
        "Histone H3 wild-type DIPG/DMG overexpressing EZHIP and "
        "H3-K27M mutant diffuse midline gliomas (Antin et al., 2020)"
    )


def sample_id(row):
    # Sentrix-style IDAT basename, e.g. '200397860077_R06C01'.
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    # Every sample is a diffuse intrinsic pontine glioma; the H3-WT cases
    # are EZHIP-overexpressing, i.e. also H3 K27-altered.
    return "DMG_K27"


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return row["Characteristics[organism part]"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Material Type"]
    mapping = {
        "DNA_FFPE": "FFPE",
        "DNA_KRYO": "FROZEN",
    }
    return mapping[value]


def sex(row):
    return row["Characteristics[sex]"]


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    return float(value)
