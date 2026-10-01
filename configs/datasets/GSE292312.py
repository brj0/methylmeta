def dataset_id(row):
    return "GSE292312"


def description(row):
    return (
        "Pediatric brain tumors (CSF cell-free DNA and primary tumor "
        "tissue) classified by methylation, M-PACT study"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "A_IDH": "Astrocytoma, IDH-mutant",
        "ATRT_MYC": "Atypical teratoid/rhabdoid tumor, MYC subclass",
        "ATRT_SHH": "Atypical teratoid/rhabdoid tumor, SHH subclass",
        "ATRT_TYR": "Atypical teratoid/rhabdoid tumor, TYR subclass",
        "DMG_K27": "Diffuse midline glioma, H3 K27-altered",
        "EPN_PF_A": "Ependymoma, posterior fossa group A",
        "EPN_RELA": "Supratentorial ependymoma, ZFTA fusion-positive",
        "ETMR": "Embryonal tumor with multilayered rosettes",
        "GBM_CBM": "Glioblastoma",
        "GBM_MES": "Glioblastoma, IDH-wildtype, mesenchymal subclass",
        "GBM_MID": "Glioblastoma, IDH-wildtype, midline subclass",
        "GBM_MYCN": "Glioblastoma, IDH-wildtype, MYCN subclass",
        "GBM_RTK_III": "Glioblastoma, IDH-wildtype, RTK III",
        "GCT": "Central nervous system germ cell tumor",
        "HGNET_BCOR": "CNS tumor with BCOR internal tandem duplication",
        "MB_G3": "Medulloblastoma, group 3",
        "MB_G4": "Medulloblastoma, group 4",
        "MB_SHH": "Medulloblastoma, SHH-activated",
        "MB_WNT": "Medulloblastoma, WNT-activated",
        "MNG": "Meningioma",
        "PIN_T_PB": "Pineoblastoma",
        "PIN_T_PB_B": "Pineoblastoma group B",
        "PLEX_PED_A": "Choroid plexus tumor, pediatric A",
        "PLEX_PED_B": "Choroid plexus tumor, pediatric B",
        "PXA": "Pleomorphic xanthoastrocytoma",
    }
    return mapping[row["genotype"]]


def methylation_class(row):
    mapping = {
        "A_IDH": "ASTRO_IDH",
        "ATRT_MYC": "ATRT_MYC",
        "ATRT_SHH": "ATRT_SHH",
        "ATRT_TYR": "ATRT_TYR",
        "DMG_K27": "DMG_K27",
        "EPN_PF_A": "EPN_PF_A",
        "EPN_RELA": "EPN_ST_ZFTA",
        "ETMR": "ETMR",
        "GBM_CBM": "GBM_NOS",
        "GBM_MES": "GBM_MES",
        "GBM_MID": "GBM_MID",
        "GBM_MYCN": "GBM_MYCN",
        "GBM_RTK_III": "GBM_RTK3",
        "GCT": "CNS_GERMI",
        "HGNET_BCOR": "CNS_BCOR_ITD",
        "MB_G3": "MB_G3",
        "MB_G4": "MB_G4",
        "MB_SHH": "MB_SHH",
        "MB_WNT": "MB_WNT",
        "MNG": "MNG",
        "PIN_T_PB": "PINE_BL",
        "PIN_T_PB_B": "PINE_BL_B",
        "PLEX_PED_A": "PLEX_PED_A",
        "PLEX_PED_B": "PLEX_PED_B",
        "PXA": "PXA",
    }
    return mapping[row["genotype"]]


def sample_site(row):
    mapping = {
        "CSF": "Cerebrospinal fluid",
        "primary tumor": "Brain",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "CSF": "csf",
        "primary tumor": "tissue",
    }
    return mapping[row["tissue"]]
