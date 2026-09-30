def dataset_id(row):
    return "E-MTAB-16763"


def description(row):
    return (
        "Paediatric diffuse-type high-grade gliomas and patient-derived "
        "orthotopic xenografts"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "DIPG": "Diffuse intrinsic pontine glioma",
        "HGG": "High-grade glioma",
    }
    return mapping[row["Characteristics[diagnosis]"]]


def methylation_class(row):
    mapping = {
        "DHG_G34": "DHG_G34",
        "DMG_K27": "DMG_K27",
    }
    return mapping[row["Characteristics[mnp12.8]"]]


def sample_site(row):
    mapping = {
        "Brainstem": "Brainstem",
        "Hemispheric": "Cerebral hemisphere",
    }
    return mapping[row["Characteristics[location]"]]


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def tumor_grade(row):
    return "high-grade"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Characteristics[sex]"]]


def age(row):
    value = row["Characteristics[age]"]
    return float(value) if value is not None else None
