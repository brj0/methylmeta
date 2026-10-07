def dataset_id(row):
    return "GSE139410"


def description(row):
    return (
        "DNA methylation profiles of four chordoma and one osteosarcoma "
        "cell line (MethylationEPIC)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "Chordoma cell line": "chordoma",
        "Osteosarcoma cell line": "osteosarcoma",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Chordoma cell line": "CHORD",
        "Osteosarcoma cell line": "OS",
    }
    return mapping[value]


def sample_site(row):
    return row["tumour anatomical location"]


def primary_site(row):
    return row["tumour anatomical location"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "cell_line"
