def dataset_id(row):
    return "GSE283928"


def description(row):
    return (
        "DNA methylation profiling of pituitary neuroendocrine tumors "
        "reveals distinct clinical and pathological subtypes (2024)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["pathologic immunophenotying"]


def methylation_class(row):
    value = row["pathologic immunophenotying"]
    mapping = {
        "Densely granulated corticotroph tumor": "PIT_AD_ACTH",
        "Densely granulated lactotroph tumor": "PIT_AD_PRL",
        "Densely granulated mammosomatotroph tumor": "PIT_AD",
        "Densely granulated somatotroph tumor": "PIT_AD_STH_DGA",
        "Gonadotroph tumor": "PIT_AD_FSH_LH",
        "Immature PIT1-lineage tumor": "PIT_AD",
        "Null cell tumor": "PIT_AD",
        "Sparsely granulated lactotroph": "PIT_AD_PRL",
        "Sparsely granulated lactotroph tumor": "PIT_AD_PRL",
        "Sparsely granulated mammosomatotroph tumor": "PIT_AD",
        "Sparsely granulated multiple lineage tumor": "PIT_AD",
        "Sparsely granulated somatotroph": "PIT_AD_STH_SPA",
        "Sparsely granulated somatotroph tumor": "PIT_AD_STH_SPA",
        "Sparsely-granulated mammosomatotroph tumor": "PIT_AD",
    }
    return mapping[value]


def sample_site(row):
    return "Pituitary gland"


def primary_site(row):
    return "Pituitary gland"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"Female": "female", "Male": "male"}
    return mapping[row["gender"]]
