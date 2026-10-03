def dataset_id(row):
    return "HCMI-CMDC"


def description(row):
    return "Human Cancer Models Initiative pan-cancer model cohort"


def sample_id(row):
    return row["Sample_ID"]


def diagnosis(row):
    value = row["diagnoses.primary_diagnosis"]
    mapping = {"Not Reported": None, "Unknown": None}
    return mapping.get(value, value)


def methylation_class(row):
    organ_map = {
        "Abdomen, NOS": None,
        "Adrenal gland, NOS": "adrenal",
        "Ampulla of Vater": "ampulla",
        "Appendix": "appendix",
        "Bladder, NOS": "bladder",
        "Bone marrow": "bone marrow",
        "Bone, NOS": "bone",
        "Brain, NOS": "brain",
        "Breast, NOS": "breast",
        "Colon, NOS": "colon",
        "Connective, subcutaneous and other soft tissues, NOS": "soft tissue",
        "Endometrium": "uterus",
        "Esophagus, NOS": "esophagus",
        "Extrahepatic bile duct": "bile duct",
        "Eye, NOS": "eye",
        "Gallbladder": "gallbladder",
        "Head, face or neck, NOS": "head and neck",
        "Intrahepatic bile duct": "bile duct",
        "Kidney, NOS": "kidney",
        "Larynx, NOS": "head and neck",
        "Liver": "liver",
        "Lung, NOS": "lung",
        "Lymph node, NOS": "lymph node",
        "Mouth, NOS": "head and neck",
        "Nasal cavity": "head and neck",
        "Not Reported": None,
        "Ovary": "ovary",
        "Pancreas, NOS": "pancreas",
        "Rectosigmoid junction": "rectum",
        "Rectum, NOS": "rectum",
        "Skin, NOS": "skin",
        "Small intestine, NOS": "small intestine",
        "Stomach, NOS": "stomach",
        "Thyroid gland": "thyroid",
        "Tongue, NOS": "head and neck",
        "Unknown primary site": None,
        "Uterus, NOS": "uterus",
    }
    organ = organ_map[row["diagnoses.tissue_or_organ_of_origin"]]
    class_map = {
        ("adrenal", "Neuroblastoma, NOS"): "NBL",
        ("ampulla", "Adenocarcinoma, NOS"): "AMP_ADCA",
        ("ampulla", "Adenocarcinoma, metastatic, NOS"): "AMP_ADCA",
        ("ampulla", "Neuroendocrine carcinoma, NOS"): "NEC",
        ("appendix", "Pseudomyxoma peritonei"): "APP_MUC_NEO",
        ("bile duct", "Adenocarcinoma, NOS"): "CCA",
        ("bile duct", "Cholangiocarcinoma"): "CCA",
        ("bile duct", "Not Reported"): None,
        # no methylome class for bladder intestinal-type adenocarcinoma
        ("bladder", "Adenocarcinoma, intestinal type"): None,
        ("bladder", "Carcinoma, metastatic, NOS"): "URO_CA",
        ("bladder", "Carcinoma, undifferentiated, NOS"): "URO_CA",
        ("bladder", "Combined small cell carcinoma"): "URO_SCNEC",
        ("bladder", "Papillary transitional cell carcinoma"): "URO_CA",
        (
            "bladder",
            "Papillary transitional cell carcinoma, non-invasive",
        ): "URO_NIPC",
        ("bladder", "Transitional cell carcinoma"): "URO_CA",
        ("bone", "Ewing sarcoma"): "EWS",
        ("bone", "Osteosarcoma, NOS"): "OS",
        ("bone", "Undifferentiated sarcoma"): None,
        ("bone marrow", "Malignant lymphoma, non-Hodgkin, NOS"): None,
        ("bone marrow", "Prolymphocytic leukemia, T-cell type"): "TPLL",
        ("brain", "Glioblastoma"): "GBM_NOS",
        ("brain", "Gliosarcoma"): "GBM_NOS",
        ("brain", "Large cell medulloblastoma"): "MB",
        ("breast", "Carcinoma, NOS"): "BR_CA",
        ("breast", "Infiltrating duct carcinoma, NOS"): "BR_CA_NST",
        ("breast", "Intraductal carcinoma, noninfiltrating, NOS"): "DCIS",
        ("breast", "Lobular carcinoma, NOS"): "BR_CA_LOB",
        ("breast", "Medullary carcinoma, NOS"): "BR_CA_NST",
        ("breast", "Metaplastic carcinoma, NOS"): "BR_CA_META",
        ("breast", "Not Reported"): None,
        ("breast", "Pleomorphic carcinoma"): "BR_CA_NST",
        ("colon", "Adenocarcinoma, NOS"): "CR_CA",
        ("colon", "Adenocarcinoma, intestinal type"): "CR_CA",
        ("colon", "Adenocarcinoma, metastatic, NOS"): "CR_CA",
        ("colon", "Carcinoma, NOS"): "CR_CA",
        ("colon", "Carcinoma, metastatic, NOS"): "CR_CA",
        ("colon", "Carcinoma, undifferentiated, NOS"): "CR_CA",
        ("colon", "Medullary carcinoma, NOS"): "CR_CA",
        ("colon", "Mucinous adenocarcinoma"): "CR_CA",
        ("colon", "Not Reported"): None,
        ("colon", "Tubular adenoma, NOS"): "CR_AD",
        ("colon", "Tubulovillous adenoma, NOS"): "CR_AD",
        ("esophagus", "Adenocarcinoma, NOS"): "ESO_ADCA",
        ("esophagus", "Adenocarcinoma, metastatic, NOS"): "ESO_ADCA",
        ("esophagus", "Carcinoma, NOS"): "ESO_CA",
        ("eye", "Malignant melanoma, NOS"): "UVE_MEL",
        # non-invasive biliary papillary neoplasm, no carcinoma class fits
        (
            "gallbladder",
            "Noninfiltrating intraductal papillary adenocarcinoma",
        ): None,
        ("head and neck", "Squamous cell carcinoma, NOS"): "HN_SCC",
        (
            "head and neck",
            "Squamous cell carcinoma, keratinizing, NOS",
        ): "HN_SCC",
        (
            "head and neck",
            "Squamous cell carcinoma, metastatic, NOS",
        ): "HN_SCC",
        ("kidney", "Clear cell adenocarcinoma, NOS"): "RCC_CC",
        ("kidney", "Medullary carcinoma, NOS"): "RCC_SMARCB1",
        ("kidney", "Nephroblastoma, NOS"): "WILMS",
        ("kidney", "Renal cell carcinoma, NOS"): "RCC",
        ("kidney", "Renal cell carcinoma, chromophobe type"): "RCC_CP",
        ("liver", "Hepatocellular carcinoma, NOS"): "HCC",
        ("lung", "Acinar cell carcinoma"): "LU_ADCA",
        ("lung", "Adenocarcinoma, NOS"): "LU_ADCA",
        ("lung", "Adenocarcinoma, metastatic, NOS"): "LU_ADCA",
        ("lung", "Bronchio-alveolar carcinoma, mucinous"): "LU_MUC_ADCA",
        ("lung", "Carcinoma, NOS"): "LU_CA",
        ("lung", "Carcinoma, metastatic, NOS"): "LU_CA",
        ("lung", "Large cell neuroendocrine carcinoma"): "LCNEC",
        ("lung", "Leiomyosarcoma, NOS"): "LMS",
        (
            "lung",
            "Minimally invasive adenocarcinoma, mucinous",
        ): "LU_MUC_ADCA",
        ("lung", "Mixed type rhabdomyosarcoma"): "RMS",
        ("lung", "Mucinous adenocarcinoma"): "LU_MUC_ADCA",
        ("lung", "Small cell carcinoma, NOS"): "SCLC",
        ("lung", "Solid carcinoma, NOS"): "LU_ADCA",
        ("lung", "Squamous cell carcinoma, NOS"): "LU_SCC",
        ("lung", "Squamous cell carcinoma, keratinizing, NOS"): "LU_SCC",
        ("lymph node", "Angioimmunoblastic T-cell lymphoma"): "AITL",
        ("lymph node", "Malignant lymphoma, non-Hodgkin, NOS"): None,
        ("lymph node", "Mature T-cell lymphoma, NOS"): "TCL_NOS",
        ("ovary", "Adenocarcinoma, metastatic, NOS"): "OVA_CA",
        ("ovary", "Carcinoma, metastatic, NOS"): "OVA_CA",
        ("ovary", "Clear cell adenocarcinoma, NOS"): "OVA_CCC",
        ("ovary", "Endometrioid adenocarcinoma, NOS"): "OVA_ENDOID_CA",
        ("ovary", "Mucinous adenocarcinoma"): "OVA_MUC_CA",
        (
            "ovary",
            "Mucinous cystic tumor of borderline malignancy",
        ): "OVA_MUC_BOT",
        ("ovary", "Mullerian mixed tumor"): "OVA_CSARC",
        (
            "ovary",
            "Serous cystadenoma, borderline malignancy",
        ): "OVA_SER_BOT",
        ("ovary", "Serous cystadenocarcinoma, NOS"): "OVA_CA",
        ("ovary", "Serous surface papillary carcinoma"): "OVA_HGSC",
        ("pancreas", "Adenocarcinoma, NOS"): "PAN_CA",
        ("pancreas", "Adenocarcinoma, metastatic, NOS"): "PAN_CA",
        ("pancreas", "Carcinosarcoma, NOS"): "PAN_CA",
        # cholangiocarcinoma reported for a pancreatic primary
        ("pancreas", "Cholangiocarcinoma"): None,
        ("pancreas", "Infiltrating duct carcinoma, NOS"): "PDAC",
        (
            "pancreas",
            "Intraductal papillary-mucinous carcinoma, invasive",
        ): "PAN_CA",
        ("pancreas", "Leiomyosarcoma, NOS"): "LMS",
        ("pancreas", "Mixed adenoneuroendocrine carcinoma"): "PAN_MINEN",
        ("pancreas", "Mucinous adenocarcinoma"): "PAN_CA",
        ("pancreas", "Neuroendocrine carcinoma, NOS"): "PAN_NEC",
        ("pancreas", "Not Reported"): None,
        ("pancreas", "Small cell carcinoma, NOS"): "PAN_NEC",
        ("rectum", "Adenocarcinoma, NOS"): "CR_CA",
        ("rectum", "Adenocarcinoma, metastatic, NOS"): "CR_CA",
        ("rectum", "Basaloid squamous cell carcinoma"): "SCC",
        ("rectum", "Mucinous adenocarcinoma"): "CR_CA",
        ("skin", "Malignant melanoma, NOS"): "SKIN_MEL",
        ("skin", "Nodular melanoma"): "SKIN_MEL",
        ("skin", "Not Reported"): None,
        ("skin", "Sezary syndrome"): "SEZARY",
        ("skin", "Spindle cell sarcoma"): "SCS",
        ("skin", "Squamous cell carcinoma, NOS"): "SKIN_SCC",
        ("small intestine", "Adenocarcinoma, NOS"): "SI_CA",
        ("small intestine", "Adenocarcinoma, metastatic, NOS"): "SI_CA",
        ("small intestine", "Atypical carcinoid tumor"): "SI_NET",
        ("small intestine", "Tubulovillous adenoma, NOS"): "DUO_AD",
        ("soft tissue", "Alveolar rhabdomyosarcoma"): "RMS_ALV",
        ("soft tissue", "Clear cell sarcoma, NOS"): "CCS",
        ("soft tissue", "Epithelioid sarcoma"): "EPSARC",
        ("soft tissue", "Giant cell sarcoma"): "GCTST",
        ("soft tissue", "Leiomyosarcoma, NOS"): "LMS",
        ("soft tissue", "Not Reported"): None,
        ("soft tissue", "Spindle cell sarcoma"): "SCS",
        ("stomach", "Adenocarcinoma, NOS"): "GAST_ADCA",
        ("stomach", "Adenocarcinoma, intestinal type"): "GAST_ADCA",
        ("stomach", "Adenocarcinoma, metastatic, NOS"): "GAST_ADCA",
        ("stomach", "Carcinoma, NOS"): "GAST_ADCA",
        ("stomach", "Carcinoma, metastatic, NOS"): "GAST_ADCA",
        ("stomach", "Metastatic signet ring cell carcinoma"): "GAST_ADCA",
        ("stomach", "Mucinous adenocarcinoma"): "GAST_ADCA",
        ("stomach", "Tubular adenocarcinoma"): "GAST_ADCA",
        ("thyroid", "Not Reported"): None,
        ("thyroid", "Papillary adenocarcinoma, NOS"): "THYR_PTC",
        ("uterus", "Adenocarcinoma with mixed subtypes"): "ENDOM_MIXC",
        ("uterus", "Carcinoma, undifferentiated, NOS"): "ENDOM_DDC",
        ("uterus", "Carcinosarcoma, NOS"): "UCS",
        ("uterus", "Endometrioid adenocarcinoma, NOS"): "ENDOM_EC",
        (
            "uterus",
            "Endometrioid adenocarcinoma, secretory variant",
        ): "ENDOM_EC",
        ("uterus", "Leiomyosarcoma, NOS"): "UT_LMS",
        ("uterus", "Not Reported"): None,
        ("uterus", "Serous cystadenocarcinoma, NOS"): "ENDOM_SC",
        ("uterus", "Serous surface papillary carcinoma"): "ENDOM_SC",
        (None, "Abdominal fibromatosis"): "DESMOID",
        (None, "Carcinoma, NOS"): None,
        (
            None,
            "Intraductal papillary-mucinous carcinoma, invasive",
        ): "PAN_CA",
        (
            None,
            "Intraductal papillary-mucinous carcinoma, non-invasive",
        ): "IPMN",
        (None, "Serrated adenoma"): "SSL",
    }
    return class_map.get((organ, row["diagnoses.primary_diagnosis"]))


def sample_site(row):
    value = row["diagnoses.site_of_resection_or_biopsy"]
    mapping = {"Not Reported": None}
    return mapping.get(value, value)


def primary_site(row):
    value = row["diagnoses.tissue_or_organ_of_origin"]
    mapping = {"Not Reported": None, "Unknown primary site": None}
    return mapping.get(value, value)


def sample_type(row):
    value = row["diagnoses.classification_of_tumor"]
    mapping = {
        "primary": "primary",
        "metastasis": "metastasis",
        "recurrence": "recurrence",
        "Premalignant": "primary",
    }
    if value in mapping:
        return mapping[value]
    fallback = {
        "Primary Tumor": "primary",
        "Metastatic": "metastasis",
        "Additional Metastatic": "metastasis",
        "Recurrent Tumor": "recurrence",
        "FFPE Recurrent": "recurrence",
        "Next Generation Cancer Model": "primary",
        "Expanded Next Generation Cancer Model": "primary",
        "Human Tumor Original Cells": "primary",
        "FFPE Scrolls": "primary",
        "Slides": "primary",
        "Neoplasms of Uncertain and Unknown Behavior": "primary",
    }
    return fallback[row["sample_type"]]


def material_type(row):
    value = row["sample_type"]
    mapping = {
        "Next Generation Cancer Model": "cell_line",
        "Expanded Next Generation Cancer Model": "cell_line",
        "Human Tumor Original Cells": "cell_line",
    }
    return mapping.get(value, "tissue")


def preservation(row):
    mapping = {
        "FFPE": "FFPE",
        "Cryopreserved": "FROZEN",
        "Frozen": "FROZEN",
        "Snap Frozen": "FROZEN",
    }
    return mapping[row["preservation_method"]]


def tumor_grade(row):
    mapping = {
        "G1": "G1",
        "G2": "G2",
        "G3": "G3",
        "G4": "G4",
        "High Grade": "high-grade",
        "GB": None,
        "GX": None,
        "Not Reported": None,
        "Unknown": None,
        None: None,
    }
    return mapping[row["diagnoses.tumor_grade"]]


def age(row):
    value = row["diagnoses.age_at_diagnosis"]
    if value is None:
        return None
    return round(float(value) / 365.25, 1)
