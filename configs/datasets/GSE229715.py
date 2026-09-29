def dataset_id(row):
    return "GSE229715"


def description(row):
    return (
        "Technical validation of brain tumor methylation classification "
        "across two Illumina methylation array generations"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    dx = row["disease state"]
    if dx == "Pilocytic astrocytoma":
        pa_site_class = {
            "Brain": None,
            "Brain, fourth ventricle": "LGG_PA_PF",
            "Brain, left cerebellar pontine mass": "LGG_PA_PF",
            "Brain, left parasagittal": "LGG_PA_GG_ST",
            "Brain, left parietal lobe": "LGG_PA_GG_ST",
            "Brain, left temporal tumor": "LGG_PA_GG_ST",
            "Brain, meninges, right sphenoid wing": None,
            "Brain, posterior fossa": "LGG_PA_PF",
            "Brain, posterior fossa, CP angle": "LGG_PA_PF",
            "Brain, right frontal": "LGG_PA_GG_ST",
            "Brain, right frontal lobe": "LGG_PA_GG_ST",
            "Brain, suprasellar": "LGG_PA_MID",
            "Brain, third ventricular": "LGG_PA_MID",
            "Cervical spine": None,
        }
        return pa_site_class[row["tumor_site"]]
    mapping = {
        "Astrocytoma with foci with high-grade features, consider HGAP": "HGAP",
        "Atypical teratoid/rhabdoid tumor": "ATRT",
        "Choroid Glioma": "CHGL",
        "DLGNT vs. PA": None,
        "Diffuse pediatric-type high-grade glioma": None,
        "Dysembryoplastic neuroepithelial tumor": "LGG_DNT",
        "GBM": "GBM_NOS",
        "Glioma with mitoses": None,
        "High-grade glioma": None,
        "High-grade glioma (astrocytoma), grade 3-4": None,
        "Left craniotomy for tumor resection": None,
        "Medulloblastoma, grade 4": "MB",
        "Medulloblastoma, non-WNT/non-SHH": "MB",
        "Meningioma, WHO grade G3": "MNG_MAL",
        "Meningioma, meningothelial subtype": "MNG",
    }
    return mapping[dx]


def sample_site(row):
    return row["tumor_site"]


def primary_site(row):
    site = row["tumor_site"]
    if site.startswith("Brain"):
        return "Brain"
    return site


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def tumor_grade(row):
    mapping = {
        "Astrocytoma with foci with high-grade features, consider HGAP": (
            "high-grade"
        ),
        "Diffuse pediatric-type high-grade glioma": "high-grade",
        "High-grade glioma": "high-grade",
        "High-grade glioma (astrocytoma), grade 3-4": "high-grade",
        "Medulloblastoma, grade 4": "G4",
        "Meningioma, WHO grade G3": "G3",
    }
    return mapping.get(row["disease state"])


def sex(row):
    return {
        "Female": "female",
        "Male": "male",
    }[row["Sex"]]


def age(row):
    value = row["age"]
    if value.endswith("M"):
        return round(float(value[:-1]) / 12, 2)
    return float(value)
