def dataset_id(row):
    return "GSE61467"


def description(row):
    return (
        "DNA methylation profiling of matched normal and tumour tissue from a "
        "small bowel adenocarcinoma cohort"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    value = row["pathology"]
    mapping = {
        "Small bowel cancer tissue from surgical resection": (
            "small bowel adenocarcinoma"
        ),
        "Normal small bowel epithelium from a cancer patient": (
            "normal small bowel epithelium"
        ),
    }
    return mapping[value]


def methylation_class(row):
    value = row["pathology"]
    mapping = {
        "Small bowel cancer tissue from surgical resection": "SI_CA",
        "Normal small bowel epithelium from a cancer patient": "CTRL_SI",
    }
    return mapping[value]


def sample_site(row):
    return "Small intestine"


def primary_site(row):
    return "Small intestine"


def sample_type(row):
    value = row["pathology"]
    mapping = {
        "Small bowel cancer tissue from surgical resection": "primary",
        "Normal small bowel epithelium from a cancer patient": "control",
    }
    return mapping[value]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
