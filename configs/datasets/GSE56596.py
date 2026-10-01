def dataset_id(row):
    return "GSE56596"


def description(row):
    return (
        "Genome-wide methylation profiling of vestibular and non-vestibular "
        "schwannomas and healthy peripheral nerves"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "Healthy Nerve": "Normal peripheral nerve",
        "Non-Vestibular Schwannoma": "Schwannoma, non-vestibular",
        "Vestibular Schwannoma (NF2)": "Vestibular schwannoma, NF2-associated",
        "Vestibular Schwannoma (Sporadic)": "Vestibular schwannoma, sporadic",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Healthy Nerve": "CTRL_NERVE",
        "Non-Vestibular Schwannoma": "SCHW",
        "Vestibular Schwannoma (NF2)": "SCHW",
        "Vestibular Schwannoma (Sporadic)": "SCHW",
    }
    return mapping[value]


def sample_site(row):
    source = row["Source"]
    if source == "Healthy Nerve":
        subtype = row["subtype"]
        if "Auricular" in subtype:
            return "Auricular nerve"
        return "Cervical nerve"
    mapping = {
        "Non-Vestibular Schwannoma": "Peripheral nerve",
        "Vestibular Schwannoma (NF2)": "Vestibulocochlear nerve",
        "Vestibular Schwannoma (Sporadic)": "Vestibulocochlear nerve",
    }
    return mapping[source]


def primary_site(row):
    return sample_site(row)


def sample_type(row):
    value = row["tissue type"]
    mapping = {
        "Control": "control",
        "Tumor": "primary",
    }
    return mapping[value]


def material_type(row):
    return "tissue"
