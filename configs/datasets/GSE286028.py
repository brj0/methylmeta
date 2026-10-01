def dataset_id(row):
    return "GSE286028"


def description(row):
    return (
        "Subtyping of Burkitt lymphoma by DNA methylation (primary "
        "tumours, BL-derived cell lines and lymphoblastoid cell lines)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"].split(",")[0]


def methylation_class(row):
    value = row["Description"]
    mapping = {
        "Lymphoblastoid cell lines (LCL)": "CTRL_LYMPH",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-negative": "BURK_EBVN",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-positive": "BURK_EBVP",
        "endemic Burkitt lymphoma-derived cell line": "BURK",
        "sporadic Burkitt lymphoma, FFPE, EBV-negative": "BURK_EBVN",
        "sporadic Burkitt lymphoma, FFPE, EBV-positive": "BURK_EBVP",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-negative": "BURK_EBVN",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-positive": "BURK_EBVP",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-unknown": "BURK",
        "sporadic Burkitt lymphoma-derived cell line": "BURK",
    }
    return mapping[value]


def sample_site(row):
    value = row["Source"]
    mapping = {"unknown": None}
    return mapping.get(value, value)


def sample_type(row):
    value = row["Description"]
    mapping = {
        "Lymphoblastoid cell lines (LCL)": "control",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-negative": "primary",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-positive": "primary",
        "endemic Burkitt lymphoma-derived cell line": "primary",
        "sporadic Burkitt lymphoma, FFPE, EBV-negative": "primary",
        "sporadic Burkitt lymphoma, FFPE, EBV-positive": "primary",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-negative": "primary",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-positive": "primary",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-unknown": "primary",
        "sporadic Burkitt lymphoma-derived cell line": "primary",
    }
    return mapping[value]


def material_type(row):
    value = row["Description"]
    mapping = {
        "Lymphoblastoid cell lines (LCL)": "cell_line",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-negative": "tissue",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-positive": "tissue",
        "endemic Burkitt lymphoma-derived cell line": "cell_line",
        "sporadic Burkitt lymphoma, FFPE, EBV-negative": "tissue",
        "sporadic Burkitt lymphoma, FFPE, EBV-positive": "tissue",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-negative": "tissue",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-positive": "tissue",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-unknown": "tissue",
        "sporadic Burkitt lymphoma-derived cell line": "cell_line",
    }
    return mapping[value]


def preservation(row):
    value = row["Description"]
    mapping = {
        "Lymphoblastoid cell lines (LCL)": None,
        "endemic Burkitt lymphoma, cryo-preserved, EBV-negative": "FROZEN",
        "endemic Burkitt lymphoma, cryo-preserved, EBV-positive": "FROZEN",
        "endemic Burkitt lymphoma-derived cell line": None,
        "sporadic Burkitt lymphoma, FFPE, EBV-negative": "FFPE",
        "sporadic Burkitt lymphoma, FFPE, EBV-positive": "FFPE",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-negative": "FROZEN",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-positive": "FROZEN",
        "sporadic Burkitt lymphoma, cryo-preserved, EBV-unknown": "FROZEN",
        "sporadic Burkitt lymphoma-derived cell line": None,
    }
    return mapping[value]
