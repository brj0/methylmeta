def dataset_id(row):
    return "GSE116699"


def description(row):
    return (
        "Methylation signature distinguishing pulmonary enteric "
        "adenocarcinoma from metastatic colorectal cancer, Jurmeister 2019"
    )


def sample_id(row):
    # GEO-style IDAT basename, e.g. GSM3258616_201465940044_R08C01
    return row["Sample_ID"]


def diagnosis(row):
    title = row["Title"]
    lowered = title.lower()
    if "pulmonary enteric adenocarcinoma" in lowered:
        return "Pulmonary enteric adenocarcinoma"
    if "colorectal" in lowered:
        return "Colorectal adenocarcinoma"
    return title


def methylation_class(row):
    title = row["Title"].lower()
    if "pulmonary enteric adenocarcinoma" in title:
        # Enteric-type adenocarcinoma of the lung
        return "LU_ENTER_ADCA"
    if "colorectal" in title:
        # Pulmonary metastases of colorectal carcinoma
        return "CR_CA"
    return None


def sample_site(row):
    mapping = {
        "Lung biopsy": "Lung",
        "Lung resection": "Lung",
        "Lung metastasis resection": "Lung",
    }
    return mapping[row["Source"]]


def primary_site(row):
    value = row["primary site"]
    mapping = {"Indeterminable": None}
    return mapping.get(value, value)


def sample_type(row):
    mapping = {
        "Lung biopsy": "primary",
        "Lung resection": "primary",
        "Lung metastasis resection": "metastasis",
    }
    return mapping[row["Source"]]


def material_type(row):
    return "tissue"


def preservation(row):
    # Maxwell RSC FFPE Plus DNA Purification Kit used for extraction
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    return float(row["age"])
