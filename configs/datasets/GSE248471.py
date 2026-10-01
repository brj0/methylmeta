def dataset_id(row):
    return "GSE248471"


def description(row):
    return (
        "GLASS longitudinal cohort of primary and recurrent IDH-mutant and "
        "IDH-wildtype glioma methylation profiles"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["who.classification.2021"]
    mapping = {"Unknown": None}
    return mapping.get(value, value)


def methylation_class(row):
    value = row["heidelberg_meth_subtype"]
    # "control"/"hypothalamus": profile called control tissue, no tumour class.
    mapping = {
        None: None,
        "RTK I": "GBM_RTK1",
        "RTK II": "GBM_RTK2",
        "mesenchymal": "GBM_MES",
        "midline": "GBM_MID",
        "astrocytoma": "ASTRO_IDH",
        "high grade astrocytoma": "ASTRO_IDH_HG",
        "1p/19q codeleted oligodendroglioma": "OLIGO_IDH",
        "subclass 1p/19q codeleted oligodendroglioma": "OLIGO_IDH",
        "meningioma": "MNG",
        "control": None,
        "hypothalamus": None,
        "no class": None,
    }
    return mapping[value]


def sample_type(row):
    value = row["recurrent_status"]
    mapping = {"Primary": "primary", "Recurrence": "recurrence"}
    return mapping[value]


def material_type(row):
    return "tissue"


def tumor_grade(row):
    value = row["who.classification.2021"]
    if value is None:
        return None
    # Grades appear at the end of the diagnosis, as "(WHO grade N)".
    mapping = {"2": "G2", "3": "G3", "4": "G4"}
    return mapping.get(value[-2])


def sex(row):
    return row["gender"]


def age(row):
    value = row["age_diagnosis_years"]
    if value is None:
        return None
    return float(value)
