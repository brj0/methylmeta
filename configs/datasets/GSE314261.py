def dataset_id(row):
    return "GSE314261"


def description(row):
    return (
        "Epigenome-wide DNA methylation of blood and saliva DNA from "
        "childhood cancer survivors and community controls of the St. Jude "
        "Lifetime Cohort"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "peripheral blood mononuclear cells": (
            "normal peripheral blood mononuclear cells"
        ),
        "saliva": "normal saliva",
    }
    return mapping[row["tissue"]]


def methylation_class(row):
    mapping = {
        "blood": "CTRL_SALIVA",
        "saliva": "CTRL_HN",
    }
    return mapping[row["source"]]


def sample_site(row):
    mapping = {
        "blood": "peripheral blood",
        "saliva": "saliva",
    }
    return mapping[row["source"]]


def sample_type(row):
    return "control"


def material_type(row):
    mapping = {
        "blood": "blood",
        "saliva": "tissue",
    }
    return mapping[row["source"]]


def sex(row):
    mapping = {"male": "male", "female": "female"}
    return mapping.get(row["Sex"])


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
