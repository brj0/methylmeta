def dataset_id(row):
    return "GSE215240"


def description(row):
    return (
        "Multiomic neuropathology (MNP) study of 1124 pediatric CNS tumours "
        "profiled at primary diagnosis (2023)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row['""tumor type""']


def _region(row):
    location = row['""tumor location""']
    if not location:
        return None
    location = location.lower()
    if "spinal cord" in location:
        return "spinal"
    posterior_fossa = (
        "cerebell",
        "fourth ventricle",
        "pons",
        "medulla",
        "brain stem",
    )
    if any(key in location for key in posterior_fossa):
        return "posterior fossa"
    midline = (
        "hypothalamus",
        "thalamus",
        "third ventricle",
        "midline",
        "pineal",
        "pituitary",
        "basal ganglia",
    )
    if any(key in location for key in midline):
        return "midline"
    return "hemispheric"


def methylation_class(row):
    value = row['""tumor type""']
    if value is None:
        return None
    # pilocytic astrocytoma and ependymoma classes are defined by location
    pa = {
        "posterior fossa": "LGG_PA_PF",
        "midline": "LGG_PA_MID",
        "hemispheric": "LGG_PA_GG_ST",
    }
    epn = {
        "posterior fossa": "EPN_PF",
        "spinal": "EPN_SPINE",
    }
    by_region = {
        "Pilocytic Astrocytoma": pa,
        "Pilomyxoid astrocytoma (PMA)": pa,
        "Ependymoma, WHO grade II": epn,
        "Ependymoma, WHO grade III": epn,
    }
    if value in by_region:
        return by_region[value].get(_region(row))
    mapping = {
        # --- Medulloblastoma ---
        "Medulloblastoma, non-WNT/SHH": "MB",
        "Medulloblastoma, SHH": "MB",
        "Medulloblastoma, WNT": "MB_WNT",
        "Medulloblastoma, NOS": "MB",
        # --- Glial / Glioma ---
        "Ganglioglioma": "LGG_GG",
        "Anaplastic ganglioglioma": "LGG_GG",
        "Glioblastoma (GBM)": "GBM_NOS",
        "Anaplastic astrocytoma": None,
        "Diffuse midline glioma, H3 K27-mutated": "DMG_K27",
        "Dysembryoplastic neuroepithelial tumor (DNET)": "LGG_DNT",
        "Pleomorphic xanthoastrocytoma (PXA)": "PXA",
        "Anaplastic pilocytic astrocytoma": "ANA_PA",
        "Low-grade astrocytoma, NOS": "LGG",
        "Diffuse astrocytoma": "LGG_MYB",
        "Anaplastic astrocytoma, IDH-mutated": "ASTRO_IDH_HG",
        "Glioblastoma, IDH-mutated": "ASTRO_IDH_HG",
        "Glioblastoma, H3 G34-mutated": "DHG_G34",
        "Diffuse astrocytoma, IDH-mutated": "ASTRO_IDH",
        "Anaplastic pleomorphic xanthoastrocytoma": "PXA",
        "Anaplastic oligodendroglioma": "OLIGO_IDH_ANA",
        "Oligodendroglioma, IDH-mutated": "OLIGO_IDH",
        "Oligoastrocytoma": None,
        "Anaplastic oligoastrocytoma, IDH-mutated": None,
        "Anaplastic oligodendroglioma, IDH-mutated": "OLIGO_IDH_ANA",
        "Anaplastic oligoastrocytoma": None,
        "High-grade glioma, NOS": None,
        # --- Ependymoma (non-location-defined) ---
        "Ependymoma, ZFTA fusion-positive": "EPN_ST_ZFTA",
        "Myxopapillary ependymoma (MPE)": "EPN_MPE",
        "Ependymoma, YAP1 fusion-positive": "EPN_ST_YAP1",
        # --- Embryonal ---
        "Embryonal tumor with multilayered rosettes (ETMR)": "ETMR",
        "Atypical teratoid/rhabdoid tumor (AT/RT)": "ATRT",
        "Primitive neuroectodermal tumor": "CNS_EMB_NEC",
        "Embryonal rhabdomyosarcoma (ERMS)": "RMS_EMB",
        "CNS Neuroblastoma": "CNS_NB_FOXR2",
        "CNS tumor with BCOR internal tandem duplication": "CNS_BCOR_ITD",
        "Cribriform neuroepithelial tumor (CRINET)": "CRIB_NET",
        "Rhabdoid tumor": "ATRT",
        # --- Other specific entities ---
        "Schwannoma": "SCHW",
        "Adamantinomatous craniopharyngioma": "CPH_ADM",
        "Pineoblastoma": "PINE_BL",
        "Germinoma": "CNS_GERMI",
        "Meningioma, WHO grade I": "MNG",
        "Meningioma, WHO grade II": "MNG",
        "Atypical meningioma, WHO grade II": "MNG",
        "CNS sarcoma": "SARC_NOS",
        "Rosette-forming glioneuronal tumor (RGNT)": "LGG_RGNT",
        "CNS Ewing family tumor": "EWS",
        "Astroblastoma": "ASTRO_BL_MN1",
        "Subependymal giant cell astrocytoma (SEGA)": "LGG_SEGA",
        "Chordoma": "CHORD",
        "Papillary tumor of pineal region (PTPR)": "PTPR",
        "Papillary glioneuronal tumor (PGNT)": "PGNT",
        "Hemangioblastoma": "HMB",
        "Choroid plexus carcinoma": "CPC_PED",
        "Malignant peripheral nerve sheath tumor (MPNST)": "MPNST",
        "Ganglioneuroblastoma": "GNBL",
        "Polymorphous low-grade neuroepithelial tumor of the young (PLNTY)": "PLNTY",
        "CNS Ewing family tumor, CIC-altered": "SARC_CIC",
        "Extraventricular neurocytoma": "EVN",
        "Retinoblastoma": "RB",
        "Intraocular medulloepithelioma": "MEDULLOEPI",
        "Langerhans cell histiocytosis (LCH)": "LCH",
        "Neurofibroma": "NFIB",
        "Pineocytoma": "PINE_CYT",
        "Paraganglioma": "PGG",
        "Pineal parenchymal tumor of intermediate differentiation (PPTID)": "PINE_PPT",
        "Pituitary adenoma": "PIT_AD",
        "Angiocentric neuroepithelial tumor (ANET)": "ACG",
        "Chondrosarcoma": "CSA",
        # --- Non-neoplastic ---
        "Non-neoplastic tissue": "CTRL_BRAIN",
        # --- No specific methylation class available / not classifiable ---
        "Descriptive diagnosis": None,
        "Malignant melanoma": None,
        "Germ cell tumor": None,
        "Odontogenic tumor": None,
        "Non-Langerhans cell histiocytosis": None,
        "Teratoma": None,
        "Atypical choroid plexus papilloma": "PLEX_ATYP",
        "Choroid plexus papilloma": "PLEX_PED_A",
        "Desmoplastic infantile ganglioglioma/astrocytoma": "LGG_DIG_DIA",
    }

    return mapping[value]


def sample_site(row):
    return row['""tumor location""']


def primary_site(row):
    return "Central nervous system"


def sample_type(row):
    mapping = {"Non-neoplastic tissue": "control"}
    return mapping.get(row['""tumor type""'], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {
        "Ependymoma, WHO grade III": "G3",
        "Ependymoma, WHO grade II": "G2",
        "Meningioma, WHO grade I": "G1",
        "Meningioma, WHO grade II": "G2",
        "Atypical meningioma, WHO grade II": "G2",
        "Glioblastoma (GBM)": "G4",
        "Glioblastoma, IDH-mutated": "G4",
        "Glioblastoma, H3 G34-mutated": "G4",
        "Diffuse midline glioma, H3 K27-mutated": "G4",
        "Medulloblastoma, WNT": "G4",
        "Medulloblastoma, SHH": "G4",
        "Medulloblastoma, non-WNT/SHH": "G4",
        "Medulloblastoma, NOS": "G4",
        "Embryonal tumor with multilayered rosettes (ETMR)": "G4",
        "Atypical teratoid/rhabdoid tumor (AT/RT)": "G4",
        "High-grade glioma, NOS": "high-grade",
        "Low-grade astrocytoma, NOS": "low-grade",
    }
    return mapping.get(row['""tumor type""'])


def sex(row):
    return row['""patient gender""']


def age(row):
    value = row['""patient age (years)""']
    if value is None:
        return None
    return float(value)
