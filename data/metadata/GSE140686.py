"""Build the GSE140686 sample sheet (Koelsche et al. 2021, sarcoma classifier).

Merges the GEO annotation with the supplementary tables (reference/train
cohort, validation cohort, methylation class translation) and derives one final
`methylation_class` acronym per sample:

Inputs (in SPREADSHEET_DIR): annotation.csv (GEO, downloaded with mepylome) and
the three supplementary xlsx files. Output: GSE140686.tsv.
"""

from pathlib import Path
from typing import Any

import polars as pl

SPREADSHEET_DIR = Path.home() / "Downloads" / "GSE140686"

# From GEO downloaded with mepylome
ann_f = SPREADSHEET_DIR / "annotation.csv"

# From supplement
train_f = SPREADSHEET_DIR / "41467_2020_20603_MOESM4_ESM.xlsx"
cls_f = SPREADSHEET_DIR / "41467_2020_20603_MOESM5_ESM.xlsx"
val_f = SPREADSHEET_DIR / "41467_2020_20603_MOESM6_ESM.xlsx"

# GEO annotation; IDAT barcode = Sample_ID without the GSM prefix
ann = pl.read_csv(ann_f, infer_schema_length=0).with_columns(
    pl.col("Sample_ID")
    .str.split("_")
    .list.slice(1)
    .list.join("_")
    .alias("IDAT")
)

# Reference (train) and validation cohorts with harmonized column names
train = (
    pl.read_excel(train_f, infer_schema_length=0)
    .rename(
        {
            "ID": "Supp_ID",
            "Batch": "Batch_date",
            "Site": "Location",
            "Diagnosis": "Institutional_diagnosis",
            "DNA": "DNA_preparation",
            "Colour": "Class_colour",
        }
    )
    .with_columns(pl.lit("train").alias("Split"))
)

val = (
    pl.read_excel(val_f, infer_schema_length=0)
    .rename(
        {
            "__UNNAMED__0": "Supp_ID",
            "Batch date": "Batch_date",
            "Institutional diagnosis": "Institutional_diagnosis",
            "DNA preparation": "DNA_preparation",
        }
    )
    .drop("ARRAY")
    .with_columns(pl.lit("validation").alias("Split"))
)

supp = pl.concat([train, val], how="diagonal_relaxed")

# Methylation class name -> acronym, family, category
cls = pl.read_excel(
    cls_f, read_options={"header_row": 1}, infer_schema_length=0
)
cls = cls.select(
    pl.col(cls.columns[0]).alias("Methylation Class Name"),
    pl.col(cls.columns[1]).alias("Class_acronym"),
    pl.col(cls.columns[2]).alias("Methylation_class_family"),
    pl.col(cls.columns[3]).alias("methylation_class_family_acronym"),
    pl.col(cls.columns[4])
    .str.extract(r"(category \d)")
    .alias("Methylation_class_category"),
)

df = ann.join(supp, on="IDAT", how="left", validate="1:1").join(
    cls, on="Methylation Class Name", how="left", validate="m:1"
)

# Institutional diagnosis -> candidate acronyms (from the reference cohort)
ref = df.filter(pl.col("Split") == "train")
candidates = dict(
    ref.group_by("Institutional_diagnosis")
    .agg(pl.col("Class_acronym").unique())
    .iter_rows()
)
valid = set(ref["Class_acronym"])

# Classifier labels in the validation file that differ from the acronyms
alias = {
    "CSA (GROUP A)": "CSA (A)",
    "CSA (GROUP B)": "CSA (B)",
    "CSA (IDH GROUP A)": "CSA (IDH A)",
    "CSA (IDH GROUP B)": "CSA (IDH B)",
    "EWING": "EWS",
}


def final_class(row: dict[str, Any]) -> tuple[str | None, str]:
    """Return (final class acronym, rule that produced it) for one sample."""
    if row["Split"] == "train":
        return row["Class_acronym"], "reference"
    pred = alias.get(row["V12.2_MaxCalDiag"], row["V12.2_MaxCalDiag"])
    assert pred in valid, pred
    if row["V12.2 Result"] in {"concordant", "discrepant - reclassification"}:
        return pred, "classifier"
    cand = candidates.get(row["Institutional_diagnosis"], [])
    if len(cand) == 1:
        return cand[0], "institutional"
    if pred in cand:
        return pred, "institutional (matches classifier call)"
    return row["Institutional_diagnosis"], "institutional (no class acronym)"


res = [final_class(r) for r in df.iter_rows(named=True)]
df = df.with_columns(
    pl.Series("methylation_class", [r[0] for r in res], dtype=pl.String),
    pl.Series(
        "methylation_class_source", [r[1] for r in res], dtype=pl.String
    ),
)
assert df.height == ann.height and df["Split"].null_count() == 0

df = df.select(
    "Title",
    "Sample_ID",
    "Manifestation",
    "Location",
    "V12.2_MaxCalDiag",
    "V12.2_MaxCalScore",
    "V12.2_MaxCalDiag_MCF",
    "V12.2_MaxCalScore_MCF",
    "V12.2 Result",
    "Validation",
    "Institutional_diagnosis",
    "Methylation_class_family",
    "methylation_class_family_acronym",
    "Methylation_class_category",
    "methylation_class",
    "methylation_class_source",
    "Tumour cell content [absolute]",
    "Supplier",
    "Supplier study",
    "DNA_preparation",
)
path = SPREADSHEET_DIR / "GSE140686.tsv"
df.write_csv(path, separator="\t")
print(f"Wrote data frame of dimension {df.shape} to {path}")
