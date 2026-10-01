def dataset_id(row):
    return "GSE99994"


def description(row):
    return (
        "Patient-derived orthotopic xenograft models, cell lines and matching "
        "human tumors of paediatric brain tumors (Brabetz et al. 2018)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "ATRT_MYC": "Atypical teratoid/rhabdoid tumor, MYC subclass",
        "ATRT_SHH": "Atypical teratoid/rhabdoid tumor, SHH subclass",
        "EPN_PFA": "Ependymoma, posterior fossa group A",
        "EPN_RELA": "Supratentorial ependymoma, ZFTA fusion-positive",
        "HGG_K27": "Diffuse midline glioma, H3 K27-altered",
        "HGG_MYCN": (
            "Diffuse paediatric-type high-grade glioma, H3-wildtype and "
            "IDH-wildtype, MYCN"
        ),
        "HGG_pedRKT1": (
            "Diffuse paediatric-type high-grade glioma, H3-wildtype and "
            "IDH-wildtype, RTK1"
        ),
        "HGG_pedRTK1": (
            "Diffuse paediatric-type high-grade glioma, H3-wildtype and "
            "IDH-wildtype, RTK1"
        ),
        "HGG_pedRTK2": (
            "Diffuse paediatric-type high-grade glioma, H3-wildtype and "
            "IDH-wildtype, RTK2"
        ),
        "MB_GRP3": "Medulloblastoma, group 3",
        "MB_GRP4": "Medulloblastoma, group 4",
        "MB_SHH": "Medulloblastoma, SHH",
        "MB_WNT": "Medulloblastoma, WNT",
        "PB": "Pineoblastoma",
    }
    return mapping[row["tumor subgroup"]]


def methylation_class(row):
    mapping = {
        "ATRT_MYC": "ATRT_MYC",
        "ATRT_SHH": "ATRT_SHH",
        "EPN_PFA": "EPN_PF_A",
        "EPN_RELA": "EPN_ST_ZFTA",
        "HGG_K27": "DMG_K27",
        "HGG_MYCN": "HGG_PED_MYCN",
        # RTK1/RTK2 are given without the A/B/C subclass, so they stay
        # unclassified rather than being assigned an unsupported subclass.
        "HGG_pedRKT1": "HGG_PED_RTK1",
        "HGG_pedRTK1": "HGG_PED_RTK1",
        "HGG_pedRTK2": "HGG_PED_RTK2",
        "MB_GRP3": "MB_G3",
        "MB_GRP4": "MB_G4",
        "MB_SHH": "MB_SHH",
        "MB_WNT": "MB_WNT",
        "PB": "PINE_BL",
    }
    return mapping[row["tumor subgroup"]]


def sample_site(row):
    return "Central nervous system"


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "PDOX": "tissue",
        "cell line": "cell_line",
        "human tumor": "tissue",
    }
    return mapping[row["Source"]]


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["material"]]
