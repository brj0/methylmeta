def dataset_id(row):
    return "GSE317578"


def description(row):
    return (
        "Pediatric and adolescent/young adult (0-39 years) meningiomas, "
        "molecular profiling (Sievers et al., 2026)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "meningioma"


def methylation_class(row):
    # "ben" and "int" are benign/intermediate meningioma groups that cannot
    # be resolved to a single WHO subtype, and the SMARCE1 cluster has no
    # matching methylation class, so all three use the broader MNG class.
    mapping = {
        "SMARCE1": "MNG",
        "ben": "MNG",
        "int": "MNG",
        "mal": "MNG_MAL",
    }
    return mapping[row["methylation class"]]


def sample_site(row):
    mapping = {
        None: None,
        "orbital": "Orbit",
        "posterior fossa": "Posterior fossa",
        "skull base": "Skull base",
        "spinal": "Spinal",
        "supratentoriell": "Supratentorial",
        "tentorial": "Tentorium",
        "ventricel": "Ventricle",
    }
    return mapping[row["localisation"]]


def primary_site(row):
    return sample_site(row)


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {"FFPE": "FFPE", "Frozen": "FROZEN"}
    return mapping[row["material"]]


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["Sex"]]
