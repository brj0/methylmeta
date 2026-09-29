def dataset_id(row):
    return "GSE246644"


def description(row):
    return (
        "MPNST and MPNST-like entities defined by DNA methylation profile "
        "in pediatric and juvenile population"
    )


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    return row["Description"].removeprefix("Final integrated diagnosis of ")


def methylation_class(row):
    value = row["Description"].removeprefix(
        "Final integrated diagnosis of ",
    )
    mapping = {
        "MPNST": "MPNST",
        "Malignant Triton Tumor in NF1": "MPNST",
        "Atypical neurofibroma": "NFIB_ATY",
        "High-grade undifferentiated spindle cell sarcoma": "SCS",
        "High-grade undifferentiated pleomorphic sarcoma": "UPS",
        "DICER1 syndrome-associated sarcoma": "CNS_SARC_DICER1",
        "BCOR-ITD sarcoma": "SARC_BCOR",
        "Spindle cell rhabdomyosarcoma, MYOD1-mutated": "RMS_MYOD1",
        "Rhabdomyosarcoma in NF1": "RMS",
        "Mesenchimal low-grade myofibroblastic neoplasia": "LGMS",
        "Mesenchimal TPM3-NTRK rearranged neoplasia (low-grade)": (
            "KINASE_SARC"
        ),
        "Mesenchimal EML4-NTRK3 rearranged neoplasia (high-grade)": (
            "KINASE_SARC"
        ),
        "Mesenchimal CLIP-RAF rearranged neoplasia (low-grade)": (
            "KINASE_SARC"
        ),
        "Spindle cell mesenchimal RPBMS-NTRK3 rearranged neoplasia": (
            "KINASE_SARC"
        ),
        "TRK-rearranged mesenchymal tumor": "KINASE_SARC",
        "Pediatric NTRK-rearranged spindle cell neoplasm": "KINASE_SARC",
    }
    return mapping[value]


def tumor_grade(row):
    value = row["Description"].lower()
    if "high-grade" in value:
        return "high-grade"
    if "low-grade" in value:
        return "low-grade"
    return None


def material_type(row):
    return "tissue"


def preservation(row):
    return "FFPE"


def sex(row):
    mapping = {"F": "female", "M": "male"}
    return mapping[row["gender"]]
