"""Auto-translated from legacy dataset YAML. Please review."""

from methylmeta.mapping import regex_map


def dataset_id(row):
    return "E-MTAB-10576"


def description(row):
    return "HNSCC_HPV_NEG"


def sample_id(row):
    return row["Source Name"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    return "HNSCC_HPV_NEG"


def sample_site(row):
    return "Head and Neck"


def primary_site(row):
    return "Head and Neck"


def sample_type(row):
    return "primary"


def sex(row):
    return row["Characteristics[sex]"]
