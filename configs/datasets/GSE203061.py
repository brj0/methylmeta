def dataset_id(row):
    return "GSE203061"


def description(row):
    return (
        "DNA methylation-based classification of pleural mesothelioma and "
        "its histopathological mimics (chronic pleuritis, pleural carcinosis, "
        "and pleomorphic lung carcinomas)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["diagnosis"]


def methylation_class(row):
    mapping = {
        "Chronic pleuritis": "CHRPL",
        "Lung adenocarcinoma, pleural carcinosis": "LU_ADCA",
        "Lung squamous cell carcinoma, pleural carcinosis": "LU_SCC",
        "Mesothelioma, biphasic": "MESOT_BIPHASIC",
        "Mesothelioma, epitheloid": "MESOT_EPITH",
        "Mesothelioma, sarcomatoid": "MESOT_SARC",
        "Pleomorphic lung carcinoma, lung adenocarcinoma "
        "with >10% spindle cells": "LU_PLEO_CA",
        "Pleomorphic lung carcinoma, lung squamous cell carcinoma "
        "with >10% spindle cells": "LU_PLEO_CA",
    }
    return mapping[row["diagnosis"]]


def sample_site(row):
    return "Pleura"


def primary_site(row):
    mapping = {
        "Chronic pleuritis": "Pleura",
        "Lung adenocarcinoma, pleural carcinosis": "Lung",
        "Lung squamous cell carcinoma, pleural carcinosis": "Lung",
        "Mesothelioma, biphasic": "Pleura",
        "Mesothelioma, epitheloid": "Pleura",
        "Mesothelioma, sarcomatoid": "Pleura",
        "Pleomorphic lung carcinoma, lung adenocarcinoma "
        "with >10% spindle cells": "Lung",
        "Pleomorphic lung carcinoma, lung squamous cell carcinoma "
        "with >10% spindle cells": "Lung",
    }
    return mapping[row["diagnosis"]]


def sample_type(row):
    mapping = {
        "Chronic pleuritis": "control",
        "Lung adenocarcinoma, pleural carcinosis": "metastasis",
        "Lung squamous cell carcinoma, pleural carcinosis": "metastasis",
        "Mesothelioma, biphasic": "primary",
        "Mesothelioma, epitheloid": "primary",
        "Mesothelioma, sarcomatoid": "primary",
        "Pleomorphic lung carcinoma, lung adenocarcinoma "
        "with >10% spindle cells": "primary",
        "Pleomorphic lung carcinoma, lung squamous cell carcinoma "
        "with >10% spindle cells": "primary",
    }
    return mapping[row["diagnosis"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    return row["gender"]


def age(row):
    value = row["age"]
    return float(value) if value is not None else None
