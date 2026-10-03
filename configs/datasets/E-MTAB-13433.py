def dataset_id(row):
    return "E-MTAB-13433"


def description(row):
    return (
        "DNA methylation profiling of pheochromocytoma, paraganglioma and "
        "normal adrenal medulla samples"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pheochromocytoma": "pheochromocytoma",
        "extra-adrenal paraganglioma": "extra-adrenal paraganglioma",
        "head and neck paraganglioma": "head and neck paraganglioma",
        "normal": "normal adrenal medulla",
    }
    return mapping[value]


def methylation_class(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pheochromocytoma": "PHEO",
        "extra-adrenal paraganglioma": "PGL_EXAD",
        "head and neck paraganglioma": "HN_PGL",
        "normal": "CTRL_ADREN",
    }
    return mapping[value]


def sample_site(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pheochromocytoma": "adrenal medulla",
        "extra-adrenal paraganglioma": "extra-adrenal paraganglia",
        "head and neck paraganglioma": "head and neck",
        "normal": "adrenal medulla",
    }
    return mapping[value]


def primary_site(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pheochromocytoma": "adrenal medulla",
        "extra-adrenal paraganglioma": "extra-adrenal paraganglia",
        "head and neck paraganglioma": "head and neck",
        "normal": "adrenal medulla",
    }
    return mapping[value]


def sample_type(row):
    value = row["Characteristics[disease]"]
    mapping = {
        "pheochromocytoma": "primary",
        "extra-adrenal paraganglioma": "primary",
        "head and neck paraganglioma": "primary",
        "normal": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["Characteristics[specimen with known storage state]"]
    mapping = {
        "FFPE": "FFPE",
        "fresh": "FRESH",
    }
    return mapping[value]


def sex(row):
    return row["Characteristics[sex]"]
