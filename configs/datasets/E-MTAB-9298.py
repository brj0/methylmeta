def dataset_id(row):
    return "E-MTAB-9298"


def description(row):
    return (
        "Methylation profiling of patient-derived primary cultures and "
        "tumours of paediatric high-grade glioma and DIPG"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    classifier = row["Characteristics[methylation classifier (mnp v11b4)]"]
    if classifier.startswith("PLEX"):
        return "choroid plexus tumour"
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "A IDH, HG": "ASTRO_IDH_HG",
        "DMG, K27": "DMG_K27",
        "GBM, G34": "DHG_G34",
        "IHG": "IHG",
        "PLEX, PED B": "PLEX_PED_B",
    }
    classifier = row["Characteristics[methylation classifier (mnp v11b4)]"]
    return mapping[classifier]


def sample_site(row):
    return row["Characteristics[organism part]"]


def primary_site(row):
    return "brain"


def sample_type(row):
    return "primary"


def material_type(row):
    mapping = {
        "cells": "cell_line",
        "tumour": "tissue",
    }
    return mapping[row["Factor Value[culture type]"]]
