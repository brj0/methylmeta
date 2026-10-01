def dataset_id(row):
    return "GSE289137"


def description(row):
    return (
        "Cross-platform DNA methylation-based classification of central "
        "nervous system and related tumours (crossNN validation cohort)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor type"]


def methylation_class(row):
    mapping = {
        "Adamantinomatous craniopharyngioma": "CPH_ADM",
        "Anaplastic meningioma": "MNG_MAL",
        "Astrocytoma (CNS WHO grade 2), IDH-mutant": "ASTRO_IDH",
        "Astrocytoma (CNS WHO grade 3), IDH-mutant": "ASTRO_IDH_HG",
        "Astrocytoma (CNS WHO grade 4), IDH-mutant": "ASTRO_IDH_HG",
        "Astrocytoma, IDH-mutant": "ASTRO_IDH",
        "Atypical choroid plexus papilloma": "PLEX_ATYP",
        "Atypical meningioma": "MNG",
        "Atypical teratoid/rhabdoid tumour": "ATRT",
        "CIC-rearranged sarcoma": "SARC_CIC",
        "CNS neuroblastoma, FOXR2-activated": "CNS_NB_FOXR2",
        "Cauda equina neuroendocrine tumour": "CAUDA_EQ_NET",
        "Central neurocytoma": "CNEUROCYT",
        "Chordoma": "CHORD",
        "Choroid plexus carcinoma": None,
        "Choroid plexus papilloma": None,
        "Corticotroph pituitary adenoma": "PIT_AD_ACTH",
        "Densely granulated somatotroph pituitary adenoma": "PIT_AD",
        "Diffuse hemispheric glioma, H3 G34-mutant": "DHG_G34",
        "Diffuse large B-cell lymphoma of the CNS": "CNSL",
        "Diffuse leptomeningeal glioneuronal tumor": "DLGNT",
        "Diffuse midline glioma, H3 K27-altered": "DMG_K27",
        "Diffuse midline glioma, H3 K27-mutant": "DMG_K27",
        "Diffuse paediatric-type high-grade glioma, "
        "H3-wildtype and IDH-wildtype": None,
        "Dysembryoblastic neuroepithelial tumour": "LGG_DNT",
        "Embryonal tumour with multilayered rosettes": "ETMR",
        "Ewing sarcoma": "EWS",
        "Ganglioglioma": "LGG_GG",
        "Glioblastoma, IDH-wildtype": "GBM_NOS",
        "Haemangioblastoma": "HMB",
        "High-grade astrocytoma with piloid features": "HGAP",
        "Infant-type hemispheric glioma": "IHG",
        "Medulloblastoma, SHH-activated": "MB_SHH",
        "Medulloblastoma, SHH-activated and TP53-wildtype": "MB_SHH",
        "Medulloblastoma, WNT-activated": "MB_WNT",
        "Medulloblastoma, non-WNT/non-SHH": "MB",
        "Melanocytoma": "MELCYT",
        "Melanoma": "MEL",
        "Meningioma": "MNG",
        "Myxopapillary ependymoma": "EPN_MPE",
        "Oligodendroglioma, IDH-mutant and 1p/19q-codeleted": "OLIGO_IDH",
        "Papillary craniopharyngioma": "CPH_PAP",
        "Papillary tumor of the pineal region": "PTPR",
        "Papillary tumour of the pineal region": "PTPR",
        "Pilocytic astrocytoma": "LGG",
        "Pineal parenchymal tumour of intermediate differentiation": "PINE_PPT",
        "Pineoblastoma": "PINE_BL",
        "Pituitary adenoma densely granulated GH/STH producing": "PIT_AD",
        "Pituitary adenoma gonadotropin producing": "PIT_AD_FSH_LH",
        "Pleomorphic xanthoastrocytoma": "PXA",
        "Posterior fossa group A (PFA) ependymoma": "EPN_PF_A",
        "Posterior fossa group B (PFB) ependymoma": "EPN_PF_B",
        "Posterior fossa subependymoma": "SUBEPN_PF",
        "Rosette-forming glioneuronal tumour": "LGG_RGNT",
        "Schwannoma": "SCHW",
        "Solitary fibrous tumour": "SFT",
        "Somatotroph pituitary adenoma": "PIT_AD",
        "Sparsely granulated somatotroph pituitary adenoma": "PIT_AD_STH_SPA",
        "Spinal ependymoma": "EPN_SPINE",
        "Subependymal giant cell astrocytoma": "LGG_SEGA",
        "Subependymoma": None,
        "Supratentorial ependymoma, YAP1 fusion-positive": "EPN_ST_YAP1",
        "Supratentorial ependymoma, ZFTA fusion positive": "EPN_ST_ZFTA",
        "Supratentorial ependymoma, ZFTA fusion-positive": "EPN_ST_ZFTA",
    }
    return mapping[row["tumor type"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def sex(row):
    mapping = {"Female": "female", "Male": "male", "Unknown": None}
    return mapping.get(row["Sex"])


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
