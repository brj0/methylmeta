def dataset_id(row):
    return "E-MTAB-5528"


def description(row):
    return (
        "Paediatric high-grade gliomas and diffuse intrinsic pontine "
        "gliomas, Illumina 450K (E-MTAB-5528)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    # The histone mutation is the molecular feature that defines the
    # paediatric high-grade glioma methylation classes, so it takes
    # precedence over the histological diagnosis.
    mutation = row["Characteristics[histone mutation]"]
    if mutation in ("H3.1_K27M", "H3.3_K27M"):
        return "DMG_K27"
    if mutation == "H3.3_G34R":
        return "DHG_G34"
    # H3-wildtype tumours: fall back to the histological diagnosis.
    mapping = {
        "anaplastic astrocytoma": "GBM_NOS",
        "glioblastoma": "GBM_NOS",
        "gliosarcoma": "GBM_NOS",
        "diffuse intrinsic pontine glioma": "DMG_K27",
        "anaplastic oligodendroglioma": "OLIGO_IDH_ANA",
        "anaplastic ganglioglioma": "LGG_GG",
        "anaplastic pilomyxoid astrocytoma": "ANA_PA",
        "pleomorphic anaplastic xanthoastrocytoma": "PXA",
    }
    return mapping.get(row["Characteristics[disease]"], None)


def _location(row):
    mapping = {
        "brainstem": "Brainstem",
        "hemispheric": "Cerebral hemisphere",
        "midline": "Midline",
    }
    return mapping.get(row["Characteristics[location]"], None)


def sample_site(row):
    return _location(row)


def primary_site(row):
    return _location(row)


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Characteristics[sex]"].strip().lower()
    mapping = {"male": "male", "female": "female"}
    return mapping.get(value, None)


def age(row):
    value = row["Characteristics[age]"].strip()
    if value == "":
        return None
    return float(value)
