def dataset_id(row):
    return "GSE249566"


def description(row):
    return "DNA methylation profiles of SMARCB1-deficient T cell lymphomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "PTCL-NOS": "peripheral T-cell lymphoma, not otherwise specified",
        "Cd3_cells": "non-neoplastic splenic CD3+ T cells",
        "Splenic_cells": "non-neoplastic spleen",
    }
    return mapping[row["Description"]]


def methylation_class(row):
    mapping = {
        "PTCL-NOS": "PTCL",
        "Cd3_cells": "CTRL_NOS",
        "Splenic_cells": "CTRL_NOS",
    }
    return mapping[row["Description"]]


def sample_site(row):
    mapping = {
        "PTCL-NOS": None,
        "Cd3_cells": "Spleen",
        "Splenic_cells": "Spleen",
    }
    return mapping[row["Description"]]


def sample_type(row):
    mapping = {
        "PTCL-NOS": "primary",
        "Cd3_cells": "control",
        "Splenic_cells": "control",
    }
    return mapping[row["Description"]]


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "Homo sapiens": "FFPE",
        "Mus musculus": None,
    }
    return mapping[row["Organism"]]
