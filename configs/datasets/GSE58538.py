def dataset_id(row):
    return "GSE58538"


def description(row):
    return (
        "Genome wide DNA methylation profiles of type I-IV germ cell tumors "
        "and germ cell tumor cell lines"
    )


def sample_id(row):
    return row["Accession"]


def diagnosis(row):
    # histology code -> readable diagnosis of the sampled tissue
    mapping = {
        "EC": "embryonal carcinoma",
        "SE": "seminoma",
        "SS": "spermatocytic seminoma",
        "DG": "dysgerminoma",
        "mNS": "mixed non-seminomatous germ cell tumor",
        "DC": "dermoid cyst",
        "I.TE.o": "type I teratoma of the ovary",
        "I.TE.s.f": "type I teratoma, sacral, female",
        "I.TE.s.m": "type I teratoma, sacral, male",
        "I.TE.t": "type I teratoma of the testis",
        "II.TE.t": "type II teratoma of the testis",
    }
    if row["histology"] is None:
        return row["cell line"]
    return mapping[row["histology"]]


def methylation_class(row):
    # histology code -> methylation class (WHO acronym); the teratomas of
    # the type I group are prepubertal-type, those of type II postpubertal
    mapping = {
        "EC": "TES_EMB_CA",
        "SE": "SEMIN",
        "SS": "SPERMATO",
        "DG": "DYSGERM",
        "mNS": "TES_MGCT",
        "DC": "OVA_MAT_TER",
        "I.TE.o": "TER",
        "I.TE.s.f": "TER",
        "I.TE.s.m": "TER",
        "I.TE.t": "TER_PRE",
        "II.TE.t": "TER_POST",
    }
    # cell line -> class of the tumour it was derived from; NT2, NCCIT and
    # 2102Ep are embryonal carcinoma lines, TCam-2 resembles a seminoma
    cell_lines = {
        "2102Ep": "TES_EMB_CA",
        "NCCIT": "TES_EMB_CA",
        "NT2": "TES_EMB_CA",
        "TCam2": "SEMIN",
    }
    if row["histology"] is None:
        return cell_lines[row["Source"]]
    return mapping[row["histology"]]


def sample_type(row):
    if row["histology"] is None:
        return None
    return "primary"


def material_type(row):
    if row["cell line"] is not None:
        return "cell_line"
    return "tissue"


def sample_site(row):
    # the anatomical site is encoded in the histology code
    mapping = {
        "EC": "testis",
        "SE": "testis",
        "SS": "testis",
        "DG": "ovary",
        "mNS": "testis",
        "DC": "ovary",
        "I.TE.o": "ovary",
        "I.TE.s.f": "sacrum",
        "I.TE.s.m": "sacrum",
        "I.TE.t": "testis",
        "II.TE.t": "testis",
    }
    return mapping.get(row["histology"])


def primary_site(row):
    mapping = {
        "EC": "testis",
        "SE": "testis",
        "SS": "testis",
        "DG": "ovary",
        "mNS": "testis",
        "DC": "ovary",
        "I.TE.o": "ovary",
        "I.TE.s.f": "sacrum",
        "I.TE.s.m": "sacrum",
        "I.TE.t": "testis",
        "II.TE.t": "testis",
    }
    return mapping.get(row["histology"])
