def dataset_id(row):
    return "E-MTAB-16762"


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
        "DMG": "Diffuse midline glioma",
        "HGG": "High-grade glioma",
    }
    return mapping[row["Characteristics[diagnosis]"]]


def methylation_class(row):
    mapping = {
        "DHG_G34": "DHG_G34",
        "DMG_EGFR": "DMG_EGFR",
        "DMG_K27": "DMG_K27",
        "GBM_MES_ATYP": "GBM_MES",
        "GBM_MES_TYP": "GBM_MES",
        "HGG_E": "HGG_E",
        "PXA": "PXA",
        "pedHGG_A": "HGG_PED_A",
        "pedHGG_MYCN": "HGG_PED_MYCN",
        "pedHGG_RTK1A": "HGG_PED_RTK1A",
        "pedHGG_RTK1B": "HGG_PED_RTK1B",
        "pedHGG_RTK1C": "HGG_PED_RTK1C",
        "pedHGG_RTK2A": "HGG_PED_RTK2A",
        "pedHGG_RTK2B": "HGG_PED_RTK2B",
    }
    return mapping.get(row["Characteristics[mnp12.8]"])


def sample_site(row):
    mapping = {
        "Brainstem": "Brainstem",
        "Hemispheric": "Cerebral hemisphere",
        "Thalamus": "Thalamus",
    }
    return mapping[row["Characteristics[location]"]]


def primary_site(row):
    return "Brain"


def sample_type(row):
    # both primary tumours and PDX models contain primary tumour material
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
