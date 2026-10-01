def dataset_id(row):
    return "GSE283494"


def description(row):
    return (
        "Recurrent glioblastoma, IDH-wildtype, methylation profiling of FFPE "
        "tumors resected at first surgery (2024)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return "Glioblastoma, IDH-wildtype"


def methylation_class(row):
    value = row["dna methylation class"]
    mapping = {
        "MC Glioblastoma IDH-wildtype RTK1 subtype": "GBM_RTK1",
        "MC Glioblastoma IDH-wildtype RTK2 subtype": "GBM_RTK2",
        "MC Glioblastoma IDH-wildtype mesenchymal subtype": "GBM_MES",
        "MC Glioblastoma IDH-wildtype mesenchymal subtype subclass B (novel)": "GBM_MES",
        "MC Glioblastoma IDH-wildtype with primitive neuronal component "
        "(novel)": "GBM_PNC",
        "MC Glioblastoma IDH-wildtype subtype posterior fossa (novel)": "GBM_NOS",
        "MC Diffuse paediatric-type high grade glioma MYCN subtype": "GBM_MYCN",
    }
    return mapping[value]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def sample_type(row):
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
