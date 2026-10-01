def dataset_id(row):
    return "GSE243465"


def description(row):
    return "Concurrent gliomas in patients with multiple sclerosis"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Source"]
    mapping = {
        "GBM_MS": "Glioblastoma, IDH-wildtype",
        "GBM_ctl": "Glioblastoma, IDH-wildtype",
        "IDHmut Astro_MS": "Astrocytoma, IDH-mutant",
        "IDHmut Astro_ctl": "Astrocytoma, IDH-mutant",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "GBM_MS": "GBM_NOS",
        "GBM_ctl": "GBM_NOS",
        "IDHmut Astro_MS": "ASTRO_IDH",
        "IDHmut Astro_ctl": "ASTRO_IDH",
    }
    return mapping[value]


def sample_site(row):
    return row["tissue"]


def primary_site(row):
    return row["tissue"]


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    value = row["Sex"]
    mapping = {
        "F": "female",
        "M": "male",
    }
    return mapping[value]
