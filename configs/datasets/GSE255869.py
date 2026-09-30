def dataset_id(row):
    return "GSE255869"


def description(row):
    return (
        "Large B-cell lymphomas (DLBCL, HGBL, PCNSL and transformed "
        "DLBCL) with normal germinal center B-cells as control; "
        "DNA methylation profiling"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    mapping = {
        "DLBCL.GC": "Diffuse large B-cell lymphoma, germinal-centre type",
        "DLBCL.nonGC": (
            "Diffuse large B-cell lymphoma, non-germinal-centre type"
        ),
        "HGBL": "High-grade B-cell lymphoma",
        "PCNSL": "Primary central nervous system lymphoma",
        "t.DLBCL": "Transformed diffuse large B-cell lymphoma",
        "Normal germinal center B-cells from tonsil": (
            "Normal germinal center B-cells from tonsil"
        ),
    }
    return mapping[row["entity"]]


def methylation_class(row):
    mapping = {
        "DLBCL.GC": "DLBCL_GCB",
        "DLBCL.nonGC": "DLBCL_ABC",
        "HGBL": "HGBCL",
        "PCNSL": "CNSL",
        "t.DLBCL": "DLBCL",
        "Normal germinal center B-cells from tonsil": "CTRL_LYMPH",
    }
    return mapping[row["entity"]]


def sample_type(row):
    mapping = {"Normal germinal center B-cells from tonsil": "control"}
    return mapping.get(row["entity"], "primary")


def material_type(row):
    return "tissue"


def preservation(row):
    return "FROZEN"
