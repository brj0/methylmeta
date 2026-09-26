def dataset_id(row):
    return "E-MTAB-9875"


def description(row):
    return (
        "Methylation profiling (450K and EPIC arrays) of bone and soft "
        "tissue tumours; validation of the DKFZ sarcoma classifier "
        "(Lyskjaer et al. 2021)"
    )


def sample_id(row):
    # Sentrix-style IDAT basename, e.g. '200550900071_R04C01'.
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "Adamantinoma": "ADAM",
        "Alveolar soft part sarcoma": "ASPS",
        "Aneurysmal bone cyst": "ABC",
        "Angiomatoid fibrous histiocytoma": "AFH",
        "Angiosarcoma": "ANGSARC",
        "Atypical neurofibroma": "NFIB_ATY",
        "Atypical plexiform neurofibroma": "NFIB_ATY",
        "BCOR-rearranged sarcoma": "SARC_BCOR",
        "Blood": "CTRL_BLOOD",
        "Carcinoma": None,
        "Chondroblastoma": "CHONDBL",
        "Chondromyxoid Fibroma": "CMF",
        "Chondrosarcoma": "CSA",
        "Chordoma": "CHORD",
        "CIC-rearranged sarcoma": "SARC_CIC",
        "Dermatofibrosarcoma protuberans": "DFSP",
        "Epithelioid sarcoma": "EPSARC",
        "EWSR1-NFATC2 rearranged sarcoma": "SARC_NFATC2",
        "Fibrous Dysplasia": "FIDYS",
        "Giant Cell Tumour of Bone": "GCTB",
        "Infantile fibrosarcoma": "IFS",
        "Leiomyosarcoma": "LMS",
        "Liposarcoma": "LPS",
        "Malignant peripheral nerve sheath tumour (MPNST)": "MPNST",
        "Melanoma": "MEL",
        "Myxofibrosarcoma": "MFS",
        "Myxoinflammatory fibroblastic sarcoma": "MIFS",
        "Myxoma": "MYX",
        "Non-ossifying Fibroma": "NOF",
        "Normal Bone": "CTRL_BONE",
        "Normal Nerve": "CTRL_NERVE",
        "Normal muscle": "CTRL_MUSCLE",
        "Normal tissue": "CTRL_NOS",
        "Ossifying fibromyxoid tumour": "OFMT",
        "Osteoblastoma": "OSTEOBL",
        "Osteoclast-rich sarcoma": None,
        "Osteofibrous Dysplasia": "OFD",
        "Osteosarcoma": "OS",
        "PEComa": "PEC",
        "Phosphaturic mesenchymal tumor (PMT)": "PMT",
        "Pigmented villonodular synovitis/Tenosynovial giant cell "
        "tumour": "TSGCT",
        "Pleomorphic hyalinising angiectatic tumour (PHAT)": "PHAT",
        "Pleomorphic sarcoma": "UPS",
        "PRDM10 rearranged undifferentiated sarcoma": None,
        "Rhabdomyosarcoma": "RMS",
        "Round cell sarcoma": "USRCS_BST",
        "Sarcoma, NOS": None,
        "Sclerosing epithelioid fibrosarcoma": "SEF",
        "Solitary fibrous tumour": "SFT",
        "Spindle Cell Sarcoma, MPNST like": "MPNST",
        "Spindle cell sarcoma of bone": "SCS",
        "Superficial CD34 fibroblastic tumour": "CD34FT",
        "Synovial sarcoma": "SYNSARC",
        "Undifferentiated pleomorphic sarcoma (UPS)": "UPS",
    }
    return mapping[value]


def sample_site(row):
    value = row["Characteristics[organism part]"]
    mapping = {
        "unknown": None,
        "na": None,
        "not specified": None,
        "control": None,
        "": None,
    }
    return mapping.get(value, value)


def sample_type(row):
    # Raw values mix tumour diagnoses with normal/control material; the
    # anatomical site of metastatic samples reads
    # '<site> - metastatic from <primary site>'.
    markers = {
        "normal": "control",
        "blood": "control",
        "control": "control",
        "metastatic": "metastasis",
    }
    disease_words = row["Characteristics[disease]"].lower().split()
    site_words = row["Characteristics[organism part]"].lower().split()
    for word in disease_words:
        if word in markers:
            return markers[word]
    for word in site_words:
        if word in markers:
            return markers[word]
    return "primary"


def material_type(row):
    mapping = {"Blood": "blood"}
    value = row["Characteristics[disease]"]
    return mapping.get(value, "tissue")


def sex(row):
    value = row["Characteristics[sex]"]
    if value is None:
        return None
    mapping = {"male": "male", "female": "female"}
    return mapping.get(value.strip().lower())


def age(row):
    value = row["Characteristics[age]"]
    if value is None:
        return None
    value = str(value).strip()
    placeholders = {"unknown", "Control", "na", ""}
    if value in placeholders:
        return None
    return float(value)
