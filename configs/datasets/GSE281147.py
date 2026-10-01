def dataset_id(row):
    return "GSE281147"


def description(row):
    return (
        "Somatic-type malignancies arising in germ cell tumors and "
        "conventional germ cell tumors, methylome analysis"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["disease state"]


def methylation_class(row):
    # The raw metadata records only the study group, not the histology of
    # each component. Conventional germ cell tumours are therefore assigned
    # the broad germ cell tumour class. The somatic-type malignancy groups
    # are histologically heterogeneous (adenocarcinoma, rhabdomyosarcoma,
    # sarcomatoid yolk sac tumour, ...); the vocabulary entries for
    # somatic-type malignancy (STMAD, STMRMS, TER_SOMMAL) are each tied to
    # one specific histology, so no single class fits the whole group.
    mapping = {
        "Conventional GCT": "GCT",
        "GCT-STM": "GCT",
        "SM-like": "GCT",
    }
    return mapping[row["disease state"]]


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"
