def dataset_id(row):
    return "GSE272656"


def description(row):
    return "VGLL-altered Schwannomas"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["fusion_type"]
    mapping = {
        "CHD7-VGLL3": "Schwannoma (CHD7-VGLL3 Mutation)",
        "EWSR1-VGLL1": "Schwannoma (EWSR1-VGLL1 Mutation)",
        "EWSR1-intergenic_HTATSF1-VGLL1": "Schwannoma (EWSR1-intergenic_HTATSF1-VGLL1 Mutation)",
        "SS18-VGLL3": "Schwannoma (SS18-VGLL3)",
        "": "Schwannoma",
    }
    return mapping[value]


def methylation_class(row):
    return "SCHW"


def sample_site(row):
    return "Vestibular Nerve"


def primary_site(row):
    return "Vestibular Nerve"


def preservation(row):
    return "FFPE"
