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
        "Acinic cell carcinoma": "SG_ACICC",
        "Adenoid-cystic carcinoma": "ADCC",
        "Angiofibroma": "SN_ANGFIB",
        "Basal cell adenoma": "BCA",
        "Basal cell carcinoma": "BCAC",
        "Biphasic myoepithelial carcinoma with 5p/5q loss": "SG_MYOEP_5P5Q",
        "Biphenotypic sinonasal sarcoma": "BSNS",
        "Canalicular adenoma": "SG_CAN_AD",
        "Clear cell carcinoma": "HCCC",
        "Cribriform adenocarcinoma": "SG_CRIB_CA",
        "Epithelial-myoepithelial carcinoma": "EPMYOC",
        "Intercalated duct adenoma": "IDA",
        "Lymphoepithelial carcinoma": "LEC",
        "Microsecretory adenocarcinoma": "MSA",
        "Mucoepidermoid carcinoma": "MEC",
        "Myoepithelial carcinoma": "SG_MYOEP_CA",
        "Myoepithelioma/Pleomorphic adenoma": "PLEO_AD_MYO",
        "NEC-like IDH2": "SN_NEC_IDH2",
        "NEC-like SMARCA4 ARID1A": "SN_NEC_SMARCA4",
        "NUT-midline carcinoma": "NUT",
        "Olfactory Neuroblastoma": "ONB",
        "Oncocytoma": "SG_ONC",
        "Polymorphous adenocarcinoma": "PMA",
        "SMARCB1-deficient sinonasal carcinoma": "SMARCB1",
        "Salivary duct carcinoma": "SDC",
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
