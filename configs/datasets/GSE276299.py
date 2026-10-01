def _diagnosis(row):
    return row["Title"].split(" [")[0]


def _is_control(row):
    return _diagnosis(row).lower() == "control brain"


def dataset_id(row):
    return "GSE276299"


def description(row):
    return (
        "Validation cohort of DNA methylation-based classification "
        "models for CNS tumors (St. Jude Children's Research "
        "Hospital, 2024)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return _diagnosis(row)


def methylation_class(row):
    # diagnosis text = Title prefix, lowercased
    mapping = {
        "adamantinomatous craniopharyngioma": "CPH_ADM",
        "adrenocortical tumor": None,
        "angiocentric glioma": "ACG",
        "angiomatoid fibrous histiocytoma": "AFH",
        "astrocytoma, idh-mutant": "ASTRO_IDH",
        "atypical choroid plexus papilloma": "PLEX_ATYP",
        "atypical teratoid/rhabdoid tumor": "ATRT",
        "choroid plexus carcinoma": "PLEX_CA_PED",
        "choroid plexus papilloma": None,
        "cic-rearranged sarcoma": "SARC_CIC",
        "clear cell sarcoma": "CCS",
        "cns neuroblastoma, foxr2-activated": "CNS_NB_FOXR2",
        "cns tumor with bcor-itd": "CNS_BCOR_ITD",
        "control brain": "CTRL_BRAIN",
        "desmoplastic small round cell tumor": "DSRCT",
        "diffuse astrocytoma, mapk pathway altered": "LGG_MAPK",
        "diffuse astrocytoma, myb-altered": "LGG_MYB",
        "diffuse astrocytoma, mybl1-altered": "LGG_MYB",
        "diffuse astrocytoma, nos": "LGG",
        "diffuse astroctyoma, mapk pathway altered": "LGG_MAPK",
        "diffuse hemispheric glioma, h3 g34-mutant": "DHG_G34",
        "diffuse low-grade glioma, mapk pathway-altered": "LGG_MAPK",
        "diffuse midline glioma, h3 k27-altered": "DMG_K27",
        "diffuse pediatric type high-grade glioma, "
        "idh-wildtype/h3-wildtype": None,
        "dysembryoplastic neuroepithelial tumor": "LGG_DNT",
        "embryonal tumor with multilayered rosettes": "ETMR",
        "embryonal tumor with multilayered rosettes, ch19mc-amplified": "ETMR",
        "embryonal tumor, nec": "CNS_EMB_NEC",
        "embryonal tumor, nos": "CNS_EMB_NEC",
        "epithelioid sarcoma": "EPSARC",
        "ganglioglioma": "LGG_GG",
        "glioblastoma, idh-wildtype": "GBM_NOS",
        "glioblastoma, idh-wildtype/h3-wildtype": "GBM_NOS",
        "glioblastoma, nos": "GBM_NOS",
        "high-grade astroctyoma, braf-altered": "HGG",
        "high-grade astroctyoma, nos": "HGG",
        "infantile fibrosarcoma": "IFS",
        "infantile hemispheric glioma": "IHG",
        "lipoblastoma": "LIPOBL",
        "medulloblastoma, non-wnt/non-shh": "MB",
        "medulloblastoma, shh-activated": "MB_SHH",
        "medulloblastoma, wnt-activated": "MB_WNT",
        "meningioma": "MNG",
        "myoepithelial tumor": "MYOEP_TUM",
        "myxoid liposarcoma": "LPS_MYX",
        "myxopapillary ependymoma": "EPN_MPE",
        "neuroblastoma": "NBL",
        "oligodendroglioma, idh-mutant and 1p/19q-codeleted": "OLIGO_IDH",
        "osteosarcoma": "OS",
        "papillary thryoid carcinoma": "THYR_PTC",
        "pediatric type diffuse glioma, idh-wildtype/h3 wildtype": "HGG",
        "pilocytic astrocytoma": "LGG",
        "pineoblastoma": "PINE_BL",
        "pleomorphic xanthoastrocytoma": "PXA",
        "posterior fossa group a (pfa) ependyoma": "EPN_PF_A",
        "posterior fossa group b (pfb) ependymoma": "EPN_PF_B",
        "retinoblastoma": "RB",
        "rhabdomyosarcoma": "RMS",
        "supratentorial ependymoma, yap1-fusion positive": "EPN_ST_YAP1",
        "supratentorial ependymoma, zfta-fusion positive": "EPN_ST_ZFTA",
        "synovial sarcoma": "SYNSARC",
        "wilms tumor": "WILMS",
    }
    return mapping[_diagnosis(row).lower()]


def sample_type(row):
    if _is_control(row):
        return "control"
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping.get(row["Sex"])
