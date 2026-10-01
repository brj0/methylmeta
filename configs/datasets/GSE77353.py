def dataset_id(row):
    return "GSE77353"


def description(row):
    return (
        "Spatial and temporal homogeneity of driver mutations in diffuse "
        "intrinsic pontine glioma: methylation profiling of multiple "
        "neuroanatomical samples from four adult DIPGs (Nikbakht et al., 2016)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mutation = row["histone h3 mutations"]
    if mutation is None:
        return "Diffuse intrinsic pontine glioma"
    mapping = {
        "H3.1 K27M": "H3.1 K27M mutant",
        "H3.2 K27M": "H3.2 K27M mutant",
        "H3.3 K27M": "H3.3 K27M mutant",
        "WT": "H3 wildtype",
    }
    return "Diffuse intrinsic pontine glioma, " + mapping[mutation]


def methylation_class(row):
    mutation = row["histone h3 mutations"]
    if mutation is None:
        return None
    mapping = {
        "H3.1 K27M": "DMG_K27",
        "H3.2 K27M": "DMG_K27",
        "H3.3 K27M": "DMG_K27",
        # H3-wildtype tumours: no specific methylation class can be assigned
        "WT": None,
    }
    return mapping[mutation]


def sample_site(row):
    mapping = {
        "cerebellum": "Cerebellum",
        "frontal lobe": "Frontal lobe",
        "hippocampus": "Hippocampus",
        "medulla": "Medulla",
        "occipital lobe": "Occipital lobe",
        "parietal lobe": "Parietal lobe",
        "pons": "Pons",
        "temporal lobe": "Temporal lobe",
        "thalmus": "Thalamus",
        "ventricle": "Ventricle",
    }
    return mapping[row["tissue"]]


def primary_site(row):
    return "Pons"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE sample": "FFPE", "Frozen tissue": "FROZEN"}
    return mapping[row["Description"]]
