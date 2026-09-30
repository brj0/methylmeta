def dataset_id(row):
    return "E-MTAB-5552"


def description(row):
    return (
        "Paediatric high-grade gliomas profiled within the HERBY clinical "
        "trial, Illumina HumanMethylation450"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Characteristics[disease]"]


def methylation_class(row):
    mapping = {
        "GBM_G34": "DHG_G34",
        "GBM_K27": "DMG_K27",
        "GBM_Other": "GBM_NOS",
        "IDH1": "ASTRO_IDH",
        "LGG-like": "LGG",
        "PXA-like": "PXA",
        "zOther": None,
    }
    return mapping[row["Characteristics[methylation subclass]"]]


def sample_site(row):
    mapping = {
        "hemispheric": "Cerebral hemisphere",
        "midline": "Midline",
    }
    return mapping[row["Characteristics[location]"]]


def primary_site(row):
    mapping = {
        "hemispheric": "Cerebral hemisphere",
        "midline": "Midline",
    }
    return mapping[row["Characteristics[location]"]]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    # HERBY sample names end either in FFPE or in FZ (fresh frozen)
    name = row["Source Name"]
    frozen_suffix = "FROZEN"[:1] + "FROZEN"[3:4]
    if name.endswith("FFPE"):
        return "FFPE"
    if name.endswith(frozen_suffix):
        return "FROZEN"
    return None


def tumor_grade(row):
    grade = int(float(row["Characteristics[tumor grading]"]))
    mapping = {3: "G3", 4: "G4"}
    return mapping[grade]


def sex(row):
    value = row["Characteristics[sex]"].strip().lower()
    mapping = {"male": "male", "female": "female", "": None}
    return mapping[value]


def age(row):
    value = str(row["Characteristics[age]"]).strip()
    if not value or value.lower() == "nan":
        return None
    return float(value)
