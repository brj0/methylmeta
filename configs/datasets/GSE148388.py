def dataset_id(row):
    return "GSE148388"


def description(row):
    return (
        "miR-1253 tumour-suppressor study: methylation profiling of "
        "medulloblastoma subgroups, cell lines and normal brain controls"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["tissue"]
    if value == "UNKNOWN":
        return None
    return value


def methylation_class(row):
    mapping = {
        "Grp3 MB": "MB_G3",
        "Grp3 MB cell line": "MB_G3",
        "Grp4 MB": "MB_G4",
        "SHH MB": "MB_SHH",
        "SHH MB cell line": "MB_SHH",
        "WNT MB": "MB_WNT",
        "NORMAL": "CTRL_CEBM",
        "Normal Astroglia, SV40 transformed": "CTRL_BRAIN",
        "Normal human astrocyte cell line": "CTRL_BRAIN",
        "Normal progenitor cell line": "CTRL_BRAIN",
        "UNKNOWN": None,
    }
    return mapping[row["subgroup"]]


def sample_site(row):
    mapping = {
        "Grp3 MB": "Cerebellum",
        "Grp3 MB cell line": "Cerebellum",
        "Grp4 MB": "Cerebellum",
        "SHH MB": "Cerebellum",
        "SHH MB cell line": "Cerebellum",
        "WNT MB": "Cerebellum",
        "NORMAL": "Cerebellum",
        "Normal Astroglia, SV40 transformed": "Brain",
        "Normal human astrocyte cell line": "Brain",
        "Normal progenitor cell line": "Brain",
        "UNKNOWN": None,
    }
    return mapping[row["subgroup"]]


def primary_site(row):
    mapping = {
        "Grp3 MB": "Cerebellum",
        "Grp3 MB cell line": "Cerebellum",
        "Grp4 MB": "Cerebellum",
        "SHH MB": "Cerebellum",
        "SHH MB cell line": "Cerebellum",
        "WNT MB": "Cerebellum",
        "NORMAL": None,
        "Normal Astroglia, SV40 transformed": None,
        "Normal human astrocyte cell line": None,
        "Normal progenitor cell line": None,
        "UNKNOWN": None,
    }
    return mapping[row["subgroup"]]


def sample_type(row):
    mapping = {
        "Grp3 MB": "primary",
        "Grp3 MB cell line": "primary",
        "Grp4 MB": "primary",
        "SHH MB": "primary",
        "SHH MB cell line": "primary",
        "WNT MB": "primary",
        "NORMAL": "control",
        "Normal Astroglia, SV40 transformed": "control",
        "Normal human astrocyte cell line": "control",
        "Normal progenitor cell line": "control",
        "UNKNOWN": None,
    }
    return mapping[row["subgroup"]]


def material_type(row):
    mapping = {
        "Grp3 MB": "tissue",
        "Grp3 MB cell line": "cell_line",
        "Grp4 MB": "tissue",
        "SHH MB": "tissue",
        "SHH MB cell line": "cell_line",
        "WNT MB": "tissue",
        "NORMAL": "tissue",
        "Normal Astroglia, SV40 transformed": "cell_line",
        "Normal human astrocyte cell line": "cell_line",
        "Normal progenitor cell line": "cell_line",
        "UNKNOWN": None,
    }
    return mapping[row["subgroup"]]


def sex(row):
    mapping = {"F": "female", "M": "male", "UNKNOWN": None, None: None}
    return mapping[row["Sex"]]


def age(row):
    value = row["age (years)"]
    if value is None:
        return None
    return float(value)
