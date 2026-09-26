def dataset_id(row):
    return "GSE167059"


def description(row):
    return "Methylation profiling reveals novel molecular classes of rhabdomyosarcoma"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["molecular group"]
    mapping = {
        "ARMS": "alveolar rhabdomyosarcoma",
        "Control": "skeletal muscle",
        "ERMS": "embryonal rhabdomyosarcoma",
        "PRMS": "pleomorphic rhabdomyosarcoma",
        "SC/SRMS": "spindle cell/sclerosing rhabdomyosarcoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["molecular group"]
    mapping = {
        "ARMS": "RMS_ALV",
        "Control": "CTRL_MUSCLE",
        "ERMS": "RMS_EMB",
        "PRMS": "RMS_PLEO",
        "SC/SRMS": "RMS_MYOD1",
    }
    return mapping[value]


def sample_type(row):
    value = row["molecular group"]
    mapping = {"Control": "control"}
    return mapping.get(value, "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
