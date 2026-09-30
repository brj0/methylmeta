def dataset_id(row):
    return "GSE152035"


def description(row):
    return (
        "Patient-derived orthotopic xenografts and cell lines from "
        "pediatric high-grade glioma"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "CONTR_INFLAM": "Inflammatory non-neoplastic brain tissue",
        "DMG_K27": "Diffuse midline glioma, H3 K27-altered",
        "GBM_G34": "Diffuse hemispheric glioma, H3 G34-mutant",
        "GBM_MID": "Glioblastoma, IDH-wildtype",
        "GBM_MYCN": "Glioblastoma, IDH-wildtype",
        "GBM_RTK_II": "Glioblastoma, IDH-wildtype",
        "GBM_RTK_III": "Glioblastoma, IDH-wildtype",
        "No Match": "Pediatric high-grade glioma",
        "PXA": "Pleomorphic xanthoastrocytoma",
    }
    return mapping[row["methylation classification"]]


def methylation_class(row):
    mapping = {
        "CONTR_INFLAM": "CTRL_BRAIN",
        "DMG_K27": "DMG_K27",
        "GBM_G34": "DHG_G34",
        "GBM_MID": "GBM_MID",
        "GBM_MYCN": "GBM_MYCN",
        "GBM_RTK_II": "GBM_RTK_2",
        "GBM_RTK_III": "GBM_RTK_3",
        "No Match": None,
        "PXA": "PXA",
    }
    return mapping[row["methylation classification"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "CONTR_INFLAM": "control",
        "Primary": "primary",
        "PDX": "primary",
        "Cell": "primary",
    }
    value = row["methylation classification"]
    if value in mapping:
        return mapping[value]
    return mapping[row["Source"].split()[-1]]


def material_type(row):
    mapping = {"Primary": "tissue", "PDX": "tissue", "Cell": "cell_line"}
    return mapping[row["Source"].split()[-1]]
