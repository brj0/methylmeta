def dataset_id(row):
    return "GSE198855"


def description(row):
    return (
        "Validation of a whole genome methylation profiling classifier for "
        "central nervous system tumors (84 brain tumors)"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["tumor type/grade"]


def methylation_class(row):
    # CNS entities whose subclass depends on location, age or molecular
    # subgroup that this metadata does not provide map to None.
    mapping = {
        "astrocytoma, IDH-mutant, WHO grade 3": "ASTRO_IDH_HG",
        "Astrocytoma, IDH-mutant (IHC), at least WHO grade 3": (
            "ASTRO_IDH_HG"
        ),
        (
            "Residual/recurrent astrocytoma, IDH-mutant (R132G per "
            "previous molecular testing), at least WHO grade 3"
        ): "ASTRO_IDH_HG",
        (
            "Anaplastic oligodendroglioma, IDH-mutant (IHC), WHO grade 3"
        ): "OLIGO_IDH_ANA",
        (
            "Recurrent/residual anaplastic oligodendroglioma, IDH-mutant "
            "(IHC), WHO grade 3"
        ): "OLIGO_IDH_ANA",
        "glioblastoma, IDH-wildtype, WHO grade 4": "GBM_NOS",
        "Glioblastoma, IDH-wildtype (IHC), WHO grade 4": "GBM_NOS",
        (
            "Recurrent/residual glioblastoma, IDH-wildtype (IHC), WHO grade 4"
        ): "GBM_NOS",
        (
            "Recurrent/residual glioblastoma, IDH-wildtype, WHO grade 4"
        ): "GBM_NOS",
        (
            "Recurrent glioblastoma, IDH wild type (pyrosequencing), "
            "WHO grade 4"
        ): "GBM_NOS",
        "Glioblastoma with giant cell features, WHO grade 4": "GBM_NOS",
        (
            "High grade astrocytoma, IDH-wildtype (IHC), at least WHO grade 3"
        ): "GBM_NOS",
        (
            "High grade malignancy favor glioblastoma, IDH-wildtype "
            "(IHC), WHO grade IV"
        ): "GBM_NOS",
        "pilocytic astrocytoma, WHO grade 1": "LGG",
        "Pilocytic astrocytoma, WHO grade 1": "LGG",
        "dysembryoplastic neuroepithelial tumor, WHO grade 1": "LGG_DNT",
        "Ganglioglioma, WHO grade I": "LGG_GG",
        "pleomorphic xanthoastrocytoma": "PXA",
        "Residual pleomorphic xanthoastrocytoma": "PXA",
        (
            "Large cell/anaplastic medulloblastoma, WHO grade 4, SHH"
        ): "MB_SHH_CHL_AD",
        (
            "classic medulloblastoma with focal anaplasia, WHO grade 4, "
            "non-WNT/non-SHH"
        ): "MB",
        "Medulloblastoma": "MB",
        "Atypical teratoid/rhabdoid tumor": "ATRT",
        (
            "pineal parenchymal tumor of intermediate differentiation "
            "(PPTID), WHO grade 3"
        ): "PINE_PPT",
        "Papillary tumor of pineal region": "PTPR",
        "Craniopharyngioma, adamantinomatous type, WHO grade 1": "CPH_ADM",
        "Hemangioblastoma, WHO grade 1": "HMB",
        "Schwannoma, WHO grade 1": "SCHW",
        "Solitary fibrous tumor": "SFT",
        "Pituitary adenoma": "PIT_AD",
        "pituitary adenoma": "PIT_AD",
        # brain biopsy of a diffuse large B cell lymphoma without any
        # systemic disease reported: a primary CNS lymphoma
        "Diffuse large B cell lymphoma": "CNSL",
        "meningioma, WHO grade 1": "MNG",
        "Meningioma, WHO grade 1": "MNG",
        "Atypical meningioma, WHO grade 2": "MNG",
        "atypical meningioma, WHO Grade 2": "MNG",
        "Atypical meningioma, WHO Grade 2": "MNG",
        "metastatic lung adenocarcinoma": "LU_ADCA",
        ("Metastatic adenocarcinoma, consistent with lung primary"): "LU_ADCA",
        "Metastatic melanoma": "MEL",
        "Metastatic poorly differentiated adenocarcinoma": "EPN",
        "Ependymoma, WHO grade 2": "EPN",
        "Recurrent anaplastic ependymoma, WHO grade 3": "EPN",
        "Subependymoma, WHO grade 1": "EPN",
        "Choroid plexus papilloma, WHO grade 1": None,
        "Glial neoplasm": None,
        "Focal cortical dysplasia, type IIa": None,
    }
    return mapping[row["tumor type/grade"]]


def sample_site(row):
    return "Brain"


def primary_site(row):
    value = row["tumor type/grade"].lower()
    if "metastatic" not in value:
        return "Brain"
    if "lung" in value:
        return "Lung"
    if "melanoma" in value:
        return "Skin"
    return None


def sample_type(row):
    value = row["tumor type/grade"].lower()
    markers = {
        "metastatic": "metastasis",
        "recurrent": "recurrence",
        "residual": "recurrence",
    }
    for marker, kind in markers.items():
        if marker in value:
            return kind
    return "primary"


def material_type(row):
    return "tissue"


def preservation(row):
    return row["sample type"]


def tumor_grade(row):
    value = row["tumor type/grade"].lower()
    # roman numerals are substrings of each other, check longest first
    grades = {
        "who grade 4": "G4",
        "who grade iv": "G4",
        "who grade 3": "G3",
        "who grade iii": "G3",
        "who grade 2": "G2",
        "who grade ii": "G2",
        "who grade 1": "G1",
        "who grade i": "G1",
    }
    for marker, grade in grades.items():
        if marker in value:
            return grade
    return None
