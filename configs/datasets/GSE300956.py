def dataset_id(row):
    return "GSE300956"


def description(row):
    return (
        "Tracing the molecular route to progression in miRNA "
        "biogenesis-defective thyroid lesions"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor type"]


def methylation_class(row):
    mapping = {
        "Encapsulated angioinvasive follicular thyroid cancer (EAIFTC)": (
            "THYR_FTC"
        ),
        "Follicular thyroid carcinoma (FTC)": "THYR_FTC",
        "Follicular variant of papillary thyroid carcinoma (FVPTC)": "THYR_PTC",
        "Minimally invasive follicular thyroid carcinoma (MIFTC)": "THYR_FTC",
        "Poorly differentiated thyroid carcinoma (PDTC)": "THYR_PDC",
        "Thyroid follicular nodular disease (TFND)": "THYR_FND",
    }
    return mapping[row["tumor type"]]


def sample_site(row):
    return "Thyroid"


def primary_site(row):
    return "Thyroid"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "FFT": "FROZEN",
    }
    return mapping[row["Source"]]


def sex(row):
    mapping = {
        "Female": "female",
        "Male": "male",
    }
    return mapping.get(row["Sex"])
