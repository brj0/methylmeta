def dataset_id(row):
    return "GSE140686"


def description(row):
    return (
        "Sarcoma DNA methylation reference and validation cohort, Koelsche et "
        "al. 2021"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Institutional_diagnosis"]


def methylation_class(row):
    value = row["methylation_class"]
    mapping = {
        "OS (HG)": "OS",
        "LMS": "LMS",
        "EWS": "EWS",
        "CHORD": "CHORD",
        "CHORD (DD)": "CHORD_DD",
        "RMS (ALV)": "RMS_ALV",
        "RMS (EMB)": "RMS_EMB",
        "SYSA": "SYNSARC",
        "GIST": "GIST",
        "USARC": "USARC",
        "AS": "ANGSARC",
        "DSRCT": "DSRCT",
        "DFSP": "DFSP",
        "MLS": "LPS_MYX",
        "SFT": "SFT",
        "SWN": "SCHW",
        "CSA (IDH A)": "CSA_SB",
        "CSA (IDH B)": "CSA_IDH_MUT",
        "WDLS/DDLS": "LPS_WD_DD",
        "MPNST": "MPNST",
        "ASPS": "ASPS",
        "Sarcoma, NOS": "SARC_NOS",
        "MRT": "MRT",
        "ES": "EPSARC",
        "SARC (RMS-like)": "SARC_RMSL",
        "SARC (MPNST-like)": "MPNST_LIKE_SARC",
        "ESS (LG)": "ESS_LG",
        "ESS (HG)": "ESS_HG",
        "ALMO/MPC": "ALMO_MPC",
        "DTFM": "DESMOID",
        "IFS": "IFS",
        "AFX/PDS": "AFX_PDS",
        "RMS (MYOD1)": "RMS_MYOD1",
        "SBRCT (CIC)": "SARC_CIC",
        "SBRCT (BCOR)": "SARC_BCOR",
        "OFMT": "OFMT",
        "CCSK": "REN_CCS",
        "CCS": "CCS",
        "CSA (A)": "CSA_IDH_WT",
        "CSA (B)": "CSA_IDH_WT",
        "CSA (MES)": "CSA_MES",
        "CSA (CC)": "CSA_CC",
        "Chondrosarcoma": "CSA",
        "CB": "CHONDBL",
        "FDY": "FIDYS",
        "MEL (CUT)": "SKIN_MEL",
        "SCC (CUT)": "SKIN_SCC",
        "GCTB": "GCTB",
        "LCH": "LCH",
        "SEF": "SEF",
        "EMCS": "EMC",
        "LIPO": "LIPO",
        "Liposarcoma": "LPS",
        "Liposarcoma (dedifferentiated)": "LPS_DD",
        "Liposarcoma (pleomorphic)": "LPS_PLEO",
        "NFA": "NFA",
        "EHE": "EHE",
        "IMT": "IMT",
        "NFB": "NFIB",
        "NFB (PLEX)": "NFIB_PLEX",
        "MO": "MYOS_OS",
        "MP": "MYPROL",
        "AFH": "AFH",
        "LGFMS": "LGFMS",
        "Kaposi": "KAPOSI_SARC",
        "OB": "OSTEOBL",
        "LMO": "LEIO",
        "Osteosarcoma": "OS",
        "Rhabdoid tumour": "MRT",
        "Rhabdomyosarcoma": "RMS",
        "Rhabdomyosarcoma, NOS": "RMS",
        "Rhabdomyosarcoma (embryonal)": "RMS_EMB",
        "Spindle cell hemangioma": "HEM_SPIN",
        "Infantil myofibromatosis": "SKIN_MFIBROMA",
        "Fibrocartilaginous mesenchymoma of bone": "FCM",
        "Myoepithelioma": "MYOEP",
        "Malignant peripheral nerve sheath tumour": "MPNST",
        "Chondromyxoid fibroma": "CMF",
        "Intimal sarcoma": "INTIM_SARC",
        "PEComa": "PEC",
        "Lipoblastomatosis": "LIPOBL",
        "Clear cell sarcoma of soft tissue": "CCS",
        "Haemangioendothelioma": "EHE",
        "Malignant mixed mesodermal tumour ": None,
        "CTRL (REA)": "CTRL_REACT",
        "CTRL (BLOOD)": "CTRL_BLOOD",
        "CTRL (MUS)": "CTRL_SKM",
    }
    return mapping[value]


def sample_site(row):
    value = row["Location"]
    if value is None:
        return None
    return value.strip()


def sample_type(row):
    mapping = {
        "Primary": "primary",
        "Metastasis": "metastasis",
        "Recurrence": "recurrence",
        "Recurrence/Metastasis": "metastasis",
    }
    return mapping.get(row["Manifestation"])


def material_type(row):
    mapping = {
        "EDTA blood": "blood",
        "FFPE": "tissue",
        "KRYO": "tissue",
    }
    return mapping[row["DNA_preparation"].strip()]


def preservation(row):
    mapping = {
        "EDTA blood": None,
        "FFPE": "FFPE",
        "KRYO": "FROZEN",
    }
    return mapping[row["DNA_preparation"].strip()]
