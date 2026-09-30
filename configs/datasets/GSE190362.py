def dataset_id(row):
    return "GSE190362"


def description(row):
    return (
        "IDH-mutant oligosarcomas and reference brain tumours, "
        "DNA methylation profiling (2022)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return mappings[row["Source"]]


def methylation_class(row):
    value = row["Source"]
    mapping = {
        "Astrocytoma, IDH-mutant, infratentorial, high grade": "ASTRO_IDH_HG",
        "Astrocytoma, IDH-mutant, infratentorial, low grade": "ASTRO_IDH",
        "Astrocytoma, IDH-mutant, supratentorial, high": "ASTRO_IDH_HG",
        "Astrocytoma, IDH-mutant, supratentorial, low": "ASTRO_IDH",
        "GBM MES": "GBM_MES",
        "GBM RTKI": "GBM_RTK_1",
        "GBM RTKII": "GBM_RTK_2",
        "Oligodendroglioma, IDH-mutant and 1p/19q codeleted": "OLIGO_IDH",
        "Primary tumor of oligosarcoma": "OLIGO_IDH",
        # no methylation class in the vocabulary for these tumour entities yet
        "Oligosarcoma, IDH-mutant": None,
        "PMMRDIA": None,
    }
    return mapping[value]


def sample_site(row):
    return "Brain"


def primary_site(row):
    return "Brain"


def material_type(row):
    return "tissue"


def preservation(row):
    value = row["material"]
    mapping = {
        "FFPE": "FFPE",
        "Frozen": "FROZEN",
    }
    return mapping[value]


def tumor_grade(row):
    value = row["Source"]
    mapping = {
        "Astrocytoma, IDH-mutant, infratentorial, high grade": "high-grade",
        "Astrocytoma, IDH-mutant, infratentorial, low grade": "low-grade",
        "Astrocytoma, IDH-mutant, supratentorial, high": "high-grade",
        "Astrocytoma, IDH-mutant, supratentorial, low": "low-grade",
        "GBM MES": "G4",
        "GBM RTKI": "G4",
        "GBM RTKII": "G4",
    }
    return mapping.get(value)
