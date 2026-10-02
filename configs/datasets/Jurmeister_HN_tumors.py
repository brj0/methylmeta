def dataset_id(row):
    return "Jurmeister_HN_tumors"


def description(row):
    return "Head and Neck Tumors from P. Jurmeister"


def sample_id(row):
    return row["barcode"]


def diagnosis(row):
    return row["meth_class"]


def methylation_class(row):
    value = row["meth_class"]
    mapping = {
        "ADC": "SN_ADCA",
        "Acinic cell carcinoma": "SG_ACIN_CA",
        "Adenoid-cystic carcinoma": "ADCC",
        "Angiofibroma": "SN_ANGFIB",
        "Basal cell adenoma": "SG_BC_AD",
        "Basal cell carcinoma": "SG_BC_CA",
        "Biphasic myoepithelial carcinoma with 5p/5q loss": "SG_MYOEP_CA_5P5Q",
        "Biphenotypic sinonasal sarcoma": "SN_BIPHEN_SARC",
        "Canalicular adenoma": "SG_CANL_AD",
        "Clear cell carcinoma": "SG_HYAL_CCC",
        "Cribriform adenocarcinoma": "SG_CRIB_CA",
        "Epithelial-myoepithelial carcinoma": "SG_EPMYO_CA",
        "Intercalated duct adenoma": "SG_INTERC_AD",
        "Lymphoepithelial carcinoma": "LEC",
        "Microsecretory adenocarcinoma": "SG_MSECR_ADCA",
        "Mucoepidermoid carcinoma": "MEC",
        "Myoepithelial carcinoma": "SG_MYOEP_CA",
        "Myoepithelioma/Pleomorphic adenoma": "PLEO_AD_MYO",
        "NEC-like IDH2": "SN_NEC_IDH2",
        "NEC-like SMARCA4 ARID1A": "SN_NEC_SMARCA4",
        "NUT-midline carcinoma": "NUT",
        "Olfactory Neuroblastoma": "ONB",
        "Oncocytoma": "SG_ONC",
        "Polymorphous adenocarcinoma": "SG_POLYM_ADCA",
        "SMARCB1-deficient sinonasal carcinoma": "SN_SMARCB1",
        "Salivary duct carcinoma": "SG_DUCT_CA",
        "Secretory carcinoma": "SG_SECR_CA",
        "Squamous cell carcinoma": "SN_SCC",
    }
    return mapping[value]


def sample_site(row):
    return "Head and Neck"


def primary_site(row):
    return "Head and Neck"


def sample_type(row):
    return "primary"
