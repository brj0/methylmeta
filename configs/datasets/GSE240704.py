def dataset_id(row):
    return "GSE240704"


def description(row):
    return (
        "Epigenetic neural signature study of high-grade glioma "
        "(glioblastoma cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tissue"]


def methylation_class(row):
    return "GBM_NOS"


def sample_site(row):
    lobes = {
        "frontal tumor location (0=no, 1=yes)": "Frontal lobe",
        "parietal tumor location (0=no, 1=yes)": "Parietal lobe",
        "temporal tumor location (0=no, 1=yes)": "Temporal lobe",
        "occipital tumor location (0=no, 1=yes)": "Occipital lobe",
    }
    sites = [name for column, name in lobes.items() if str(row[column]) == "1"]
    if not sites:
        return "Brain"
    return ", ".join(sites)


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = str(row["sex (0=male, 1=female)"])
    mapping = {"0": "male", "1": "female"}
    return mapping[value]


def age(row):
    value = row["age at time of surgery (years)"]
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
