def dataset_id(row):
    return "GSE260850"


def description(row):
    return (
        "Longitudinal epigenome analysis of IDH-mutant astrocytomas from "
        "initial and recurrent surgical specimens"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Source"]


def methylation_class(row):
    return "ASTRO_IDH"


def primary_site(row):
    return "Brain"


def sample_type(row):
    mapping = {
        "initial": "primary",
        "recurrent": "recurrence",
    }
    return mapping[row["tumor category"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
