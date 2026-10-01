def dataset_id(row):
    return "GSE279950"


def description(row):
    return (
        "MGMT promoter methylation score in IDH-mutant low-grade glioma for "
        "predicting benefit from temozolomide treatment (2025)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["nmpclassif_class_v12.5"]


def methylation_class(row):
    value = row["nmpclassif_class_v12.5"]
    mapping = {
        "control tissue, hemispheric cortex": "CTRL_BRAIN",
        "control tissue, white matter (corpus callosum)": "CTRL_BRAIN",
        (
            "diffuse glioma, IDH-mutant and 1p19q co-deleted "
            "[oligodendroglial type]"
        ): "OLIGO_IDH",
        (
            "diffuse glioma, IDH-mutant and 1p19q retained [astroglial type]"
        ): "ASTRO_IDH",
        (
            "diffuse glioma, IDH-mutant and 1p19q retained [astroglial type], "
            "high grade"
        ): "ASTRO_IDH_HG",
        "glioblastoma, IDH-wildtype, mesenchymal type": "GBM_MES",
        "medulloblastoma Group 3": "MB_G3",
    }
    return mapping[value]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    value = row["nmpclassif_family_v12.5"]
    mapping = {
        "control brain tissues": "control",
        "diffuse glioma, IDH mutant": "primary",
        "Glioblastoma, IDH-wildtype": "primary",
        "medulloblastoma non-WNT/non-SHH activated": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def sex(row):
    value = row["Sex"]
    mapping = {"F": "female", "M": "male"}
    return mapping[value]


def age(row):
    value = row["age_at_diagnosis"]
    if value is None:
        return None
    return float(value)
