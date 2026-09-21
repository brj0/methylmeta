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
        "ADC": "SNAD",
        "Acinic cell carcinoma": "SACC",
        "Adenoid-cystic carcinoma": "ADCC",
        "Angiofibroma": "SNAF",
        "Basal cell adenoma": "BCA",
        "Basal cell carcinoma": "BCAC",
        "Biphasic myoepithelial carcinoma with 5p/5q loss": "SBMC5P5Q",
        "Biphenotypic sinonasal sarcoma": "BSNS",
        "Canalicular adenoma": "SCA",
        "Clear cell carcinoma": "HCCC",
        "Cribriform adenocarcinoma": "SCADC",
        "Epithelial-myoepithelial carcinoma": "EPMYOC",
        "Intercalated duct adenoma": "IDA",
        "Lymphoepithelial carcinoma": "LEC",
        "Microsecretory adenocarcinoma": "SMSAD",
        "Mucoepidermoid carcinoma": "MEC",
        "Myoepithelial carcinoma": "SMYOC",
        "Myoepithelioma/Pleomorphic adenoma": "PLEO_AD_MYO",
        "NEC-like IDH2": "NECIDH2",
        "NEC-like SMARCA4 ARID1A": "SNNEC_SMARCA4",
        "NUT-midline carcinoma": "NUT",
        "Olfactory Neuroblastoma": "ONB",
        "Oncocytoma": "SONCO",
        "Polymorphous adenocarcinoma": "PAD",
        "SMARCB1-deficient sinonasal carcinoma": "SMARCB1",
        "Salivary duct carcinoma": "SDC",
        "Secretory carcinoma": "SSC",
        "Squamous cell carcinoma": "SN_SCC",
    }
    return mapping[value]


def sample_site(row):
    return "Head and Neck"


def primary_site(row):
    return "Head and Neck"


def sample_type(row):
    return "primary"
