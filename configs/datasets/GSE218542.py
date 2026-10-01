def dataset_id(row):
    return "GSE218542"


def description(row):
    return (
        "Low-grade epilepsy-associated brain tumours, mostly PTPN11/RAS-MAPK "
        "altered ganglioglioma (GEO, 2022)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "DNT": "dysembryoplastic neuroepithelial tumor",
        "GG": "ganglioglioma",
        "PXA": "pleomorphic xanthoastrocytoma",
        "PXA/GG": "pleomorphic xanthoastrocytoma / ganglioglioma",
        "isomorphic astro.": "diffuse astrocytoma, MYB/MYBL1-altered",
    }
    return mapping[row["diagnosis"]]


def methylation_class(row):
    mapping = {
        "GG, PTPN11": "LGG_GG",
        "LGG, DNT": "LGG_DNT",
        "LGG, GG": "LGG_GG",
        "LGG, MYB": "LGG_MYB",
        "LGG, PXA": "PXA",
    }
    return mapping[row["methylation class"]]


def sample_site(row):
    return row["Source"]


def primary_site(row):
    return row["Source"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    value = int(row["cns who grade"])
    mapping = {1: "G1", 2: "G2", 3: "G3"}
    return mapping[value]
