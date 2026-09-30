def dataset_id(row):
    return "GSE131482"


def description(row):
    return (
        "Methylation profiling of radiation-induced gliomas after cranial "
        "irradiation and of a pediatric brain tumor reference cohort "
        "(Deng et al., 2020)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    if row["Title"].startswith("dkfz_RIG_"):
        return "radiation-induced glioma"
    mapping = {
        "DMG_K27": "Diffuse midline glioma, H3 K27-altered",
        "G34": "Diffuse hemispheric glioma, H3 G34-mutant",
        "MYCN": "Pediatric glioblastoma, MYCN subclass",
        "PXA": "Pleomorphic xanthoastrocytoma",
        "pedGBM_RTK1": "Pediatric glioblastoma, RTK1 subclass",
        "pedGBM_RTK2": "Pediatric glioblastoma, RTK2 subclass",
    }
    return mapping[row["methylation class"]]


def methylation_class(row):
    mapping = {
        "DMG_K27": "DMG_K27",
        "G34": "DHG_G34",
        "MYCN": "GBM_MYCN",
        "PXA": "PXA",
        "pedGBM_RTK1": "GBM_RTK_1",
        "pedGBM_RTK2": "GBM_RTK_2",
    }
    return mapping[row["methylation class"]]


def sample_site(row):
    return row["location"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def sex(row):
    value = row["gender"]
    if value is None:
        return None
    mapping = {"f": "female", "m": "male"}
    return mapping[value]


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
