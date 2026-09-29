def dataset_id(row):
    return "GSE103659"


def description(row):
    return (
        "Radiomic subtyping of newly diagnosed glioblastoma, "
        "Kickingereder 2018"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    # Local (partly German) histopathological diagnosis of the sampled tumor.
    return row["histology"]


def methylation_class(row):
    # Pilocytic astrocytoma subclasses are site-specific (posterior fossa,
    # midline, hemispheric) and no sampling site is recorded, so the broader
    # low-grade glioma class is used. The non-specific German diagnoses and
    # the ganglioneuroblastoma (peripheral neuroblastic tumour) cannot be
    # assigned to a class from the available metadata.
    mapping = {
        "Glioblastoma (WHO grade IV)": "GBM_NOS",
        "Gliosarcoma (WHO grade IV)": "GBM_NOS",
        "Anaplastic Astrocytoma (WHO grade III)": "ASTRO_IDH_HG",
        "Anaplastic astrocytoma (WHO grade III)": "ASTRO_IDH_HG",
        "Diffuse Astrocytoma (WHO grade II)": "ASTRO_IDH",
        "Diffuse astrocytoma (WHO grade II)": "ASTRO_IDH",
        "Pilocytic Astrocytoma (WHO grade I)": "LGG",
        "Maligner glialer Tumor": None,
        "Malignes Hirnstammgliom": None,
        "Ganglioneuroblastom": "GNBL",
    }
    return mapping[row["histology"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"


def age(row):
    value = row["age"]
    if value is None:
        return None
    return float(value)
