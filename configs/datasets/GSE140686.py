def dataset_id(row):
    return "GSE140686"


def description(row):
    return "Sarcoma Classification by DNA-methylation profiling, Koelsche 2021"


def sample_id(row):
    return row["ID"]


def diagnosis(row):
    return row["Diagnosis"]


def methylation_class(row):
    value = row["Methylation Class Name"]
    mapping = {
        # controls
        "methylation class control (blood)": "CTRL_BLOOD",
        "methylation class control (muscle tissue)": "CTRL_SKM",
        "methylation class control (reactive tissue)": "CTRL_REACT",
        # bone tumours
        "methylation class chondroblastoma": "CHONDBL",
        "methylation class chondrosarcoma (clear cell)": "CSA_CC",
        "methylation class chondrosarcoma (IDH group A)": "CSA_IDH_MUT",
        "methylation class chondrosarcoma (IDH group B)": "CSA_IDH_MUT",
        "methylation class chondrosarcoma (group A)": "CSA",
        "methylation class chondrosarcoma (group B)": "CSA",
        "methylation class chondrosarcoma (mesenchymal)": "CSA_MES",
        "methylation class chordoma": "CHORD",
        "methylation class chordoma (dedifferentiated)": "CHORD_DD",
        "methylation class fibrous dysplasia": "FIDYS",
        "methylation class giant cell tumour of bone": "GCTB",
        "methylation class osteoblastoma": "OSTEOBL",
        "methylation class osteosarcoma (high grade)": "OS",
        # soft tissue tumours
        "methylation class alveolar soft part sarcoma": "ASPS",
        "methylation class angiomatoid fibrous histiocytoma": "AFH",
        "methylation class angioleiomyoma / myopericytoma": "ALMO_MPC",
        "methylation class angiosarcoma": "ANGSARC",
        "methylation class atypical fibroxanthoma / pleomorphic dermal sarcoma": "AFX_PDS",
        "methylation class clear cell sarcoma of soft parts": "CCS",
        "methylation class dermatofibrosarcoma protuberans": "DFSP",
        "methylation class desmoid-type fibromatosis": "DESMOID",
        "methylation class desmoplastic small round cell tumour": "DSRCT",
        "methylation class epithelioid haemangioendothelioma": "EHE",
        "methylation class epithelioid sarcoma": "EPSARC",
        "methylation class Ewing´s sarcoma": "EWS",
        "methylation class extraskeletal myxoid chondrosarcoma": "EMC",
        "methylation class infantile fibrosarcoma": "IFS",
        "methylation class inflammatory myofibroblastic tumour": "IMT",
        "methylation class Kaposi sarcoma": "KAPOSI_SARC",
        "methylation class leiomyoma": "LEIO",
        "methylation class leiomyosarcoma": "LMS",
        "methylation class lipoma": "LIPO",
        "methylation class low-grade fibromyxoid sarcoma": "LGFMS",
        "methylation class malignant peripheral nerve sheath tumour": "MPNST",
        "methylation class malignant rhabdoid tumour": "MRT",
        "methylation class myositis ossificans": "MYOS_OS",
        "methylation class myositis proliferans": "MYPROL",
        "methylation class myxoid liposarcoma": "LPS_MYX",
        "methylation class nodular fasciitis": "NFA",
        "methylation class ossifying fibromyxoid tumour": "OFMT",
        "methylation class rhabdomyosarcoma (alveolar)": "RMS_ALV",
        "methylation class rhabdomyosarcoma (embryonal)": "RMS_EMB",
        "methylation class rhabdomyosarcoma (MYOD1)": "RMS_MYOD1",
        "methylation class sarcoma (MPNST-like)": "MPNST",
        "methylation class sarcoma (RMS-like)": "SARC_RMSL",
        "methylation class sclerosing epithelioid fibrosarcoma": "SEF",
        "methylation class small blue round cell tumour with BCOR alteration": "SARC_BCOR",
        "methylation class small blue round cell tumour with CIC alteration": "SARC_CIC",
        "methylation class synovial sarcoma": "SYNSARC",
        "methylation class undifferentiated sarcoma": "USARC",
        "methylation class well- / dedifferentiated liposarcoma": "LPS_WD_DD",
        # other entities
        "methylation class clear cell sarcoma of the kidney": "REN_CCS",
        "methylation class endometrial stromal sarcoma (high grade)": "ESS_HG",
        "methylation class endometrial stromal sarcoma (low grade)": "ESS_LG",
        "methylation class gastrointestinal stromal tumour": "GIST",
        "methylation class Langerhans cell histiocytosis": "LCH",
        "methylation class melanoma (cutaneous)": "SKIN_MEL",
        "methylation class neurofibroma": "NFIB",
        "methylation class neurofibroma (plexiform)": "NFIB_PLEX",
        "methylation class schwannoma": "SCHW",
        "methylation class solitary fibrous tumour": "SFT",
        "methylation class squamous cell carcinoma (cutaneous)": "SKIN_SCC",
    }
    return mapping[value]


def sample_site(row):
    value = row["Site"]
    return value.strip() if value is not None else None


def sample_type(row):
    value = row["Manifestation"]
    mapping = {
        "Primary": "primary",
        "Metastasis": "metastasis",
        "Recurrence": "recurrence",
        None: None,
    }
    return mapping[value]


def material_type(row):
    value = row["DNA"]
    mapping = {
        "EDTA blood": "blood",
        "FFPE": "tissue",
        "KRYO": "tissue",
    }
    return mapping[value]


def preservation(row):
    value = row["DNA"]
    mapping = {
        "EDTA blood": None,
        "FFPE": "FFPE",
        "KRYO": "FROZEN",
    }
    return mapping[value]
