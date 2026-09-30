def dataset_id(row):
    return "GSE144894"


def description(row):
    return (
        "DNA methylation of sorted intraclonal fractions of circulating CLL "
        "cells, Duran-Ferrer et al. 2020"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "chronic lymphocytic leukemia"


def methylation_class(row):
    # IGHV mutation status separates the two CLL methylation subclasses.
    mapping = {
        "M": "CLL_IGHV_MUT",
        "U": "CLL_IGHV_UNMUT",
    }
    return mapping[row["ighv"]]


def sample_site(row):
    return "peripheral blood"


def primary_site(row):
    return "peripheral blood"


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"


def preservation(row):
    return "FROZEN"


def sex(row):
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping[row["Sex"]]
