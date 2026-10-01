def _cohort(row):
    return row["Title"].split("-")[0].rstrip("0123456789")


def dataset_id(row):
    return "GSE67043"


def description(row):
    return (
        "St. Jude pediatric acute lymphoblastic leukemia cohort profiled "
        "for DNA methylation"
    )


def sample_id(row):
    return row["Sample_ID"].removesuffix(".tsv.gz")


def diagnosis(row):
    mapping = {
        "SJBALL": "B-lymphoblastic leukemia",
        "SJTALL": "T-lymphoblastic leukemia",
        "SJHYPER": "B-lymphoblastic leukemia with high hyperdiploidy",
        "SJHYPO": "B-lymphoblastic leukemia with hypodiploidy",
        "SJETV": "B-lymphoblastic leukemia with ETV6::RUNX1 fusion",
        "SJE2A": "B-lymphoblastic leukemia with TCF3::PBX1 fusion",
        "SJMLL": "B-lymphoblastic leukemia with KMT2A rearrangement",
        "SJPHALL": "B-lymphoblastic leukemia with BCR::ABL1 fusion",
        "SJINF": "infant acute lymphoblastic leukemia",
    }
    return mapping[_cohort(row)]


def methylation_class(row):
    mapping = {
        "SJBALL": "B_ALL",
        "SJTALL": "T_ALL",
        "SJHYPER": "B_ALL_HYPERDIP",
        "SJHYPO": "B_ALL_HYPODIP",
        "SJETV": "B_ALL_ETV6_RUNX1",
        "SJE2A": "B_ALL_TCF3_PBX1",
        "SJMLL": "B_ALL_KMT2A",
        "SJPHALL": "B_ALL_BCR_ABL1",
        "SJINF": "B_ALL",
    }
    return mapping[_cohort(row)]


def sample_type(row):
    return "primary"


def material_type(row):
    return "blood"
