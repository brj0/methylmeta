def dataset_id(row):
    return "GSE76269"


def description(row):
    return (
        "Genome-wide profiling of the functional DNA methylation landscape "
        "in human cancer types and normal control tissues"
    )


def _prefix(row):
    # Title prefixes: ALL acute lymphoblastic leukemia, CLL chronic
    # lymphocytic leukemia, SCLC small cell lung carcinoma, LC liver
    # cancer, NB neuroblastoma, PC prostate cancer, and the normal
    # controls Blood/LYMPH/Liver/Prostate/Grey_matter.
    return row["Title"].rsplit("_", 1)[0]


def sample_id(row):
    return row["Title"]


def diagnosis(row):
    mapping = {
        "ALL": "acute lymphoblastic leukemia",
        "CLL": "chronic lymphocytic leukemia",
        "SCLC": "small cell lung carcinoma",
        "LC": "hepatocellular carcinoma",
        "NB": "neuroblastoma",
        "PC": "prostate adenocarcinoma",
        "Blood": "normal blood",
        "LYMPH": "normal lymph node",
        "Liver": "normal liver",
        "Prostate": "normal prostate",
        "Grey_matter": "normal grey matter",
    }
    return mapping[_prefix(row)]


def methylation_class(row):
    organ_mapping = {
        "Autonomic Ganglia": "Autonomic ganglia",
        "Central Nervous System": "Central nervous system",
        "Haematopoietic &amp; Lymphoid": "Haematolymphoid",
        "Liver": "Liver",
        "Lung": "Lung",
        "Prostate": "Prostate",
    }
    class_mapping = {
        ("Autonomic ganglia", "NB"): "NBL",
        ("Central nervous system", "Grey_matter"): "CTRL_GREY",
        ("Haematolymphoid", "ALL"): "B_ALL",
        ("Haematolymphoid", "CLL"): "CLL",
        ("Haematolymphoid", "Blood"): "CTRL_BLOOD",
        ("Haematolymphoid", "LYMPH"): "CTRL_LYMPH",
        ("Liver", "LC"): "HCC",
        ("Liver", "Liver"): "CTRL_LIV",
        ("Lung", "SCLC"): "SCLC",
        ("Prostate", "PC"): "PROS_ADCA",
        ("Prostate", "Prostate"): "CTRL_PROS",
    }
    organ = organ_mapping[row["Source"]]
    return class_mapping[(organ, _prefix(row))]


def sample_site(row):
    mapping = {
        "Autonomic Ganglia": "Autonomic ganglia",
        "Central Nervous System": "Central nervous system",
        "Haematopoietic &amp; Lymphoid": "Haematolymphoid",
        "Liver": "Liver",
        "Lung": "Lung",
        "Prostate": "Prostate",
    }
    return mapping[row["Source"]]


def primary_site(row):
    return sample_site(row)


def sample_type(row):
    mapping = {
        "cancer": "primary",
        "normal": "control",
    }
    return mapping[row["health state"]]


def material_type(row):
    if "blood" in diagnosis(row):
        return "blood"
    return "tissue"
