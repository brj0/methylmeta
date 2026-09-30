# methylmeta
Curated metadata, class definitions, and sample annotations for DNA methylation-based tumor classification datasets.

## Finding the datasets for a project

`methylmeta find` tells you which datasets contain given tumor types, so you
know what to download *before* fetching anything. It reads the dataset
configs (`configs/datasets/`) statically, so no raw data is needed.

```bash
# By acronym (sub-entities are included, e.g. SKIN_MEL also selects ACR_MEL)
methylmeta find --classes SKIN_MEL,SCHW

# By family tag or anatomical site; selectors are OR-ed
methylmeta find --family glioma --site kidney

# Which of them are not downloaded yet? Then fetch exactly those.
methylmeta find --classes SCHW --dataset_dir ~/data --missing --format ids > ids.txt
methylmeta fetch $(cat ids.txt) --dataset_dir ~/data
```

Use `methylmeta search_vocab <text>` to look up acronyms.

For your own analysis, `--format tsv` writes one row per dataset/class pair
(columns: dataset_id, methylation_class, name, site, lineage_broad, families
`|`-joined, parent). It respects the selectors, so with none it is the whole
catalog:

```bash
methylmeta find --format tsv > catalog.tsv
```

```python
import polars as pl

df = pl.read_csv("catalog.tsv", separator="\t")
df.filter(pl.col("methylation_class").is_in(["SCHW", "MPNST"]))
  .group_by("dataset_id").agg(pl.col("methylation_class").unique())
```

`--format json` gives the same information as nested records.

Limits: a dataset matches if its config *can* produce a class (no case
counts), so a dataset with a single rare case matches too. Classes that are not
spelled out as a literal in the config (e.g. a bare `return row["class"]`) are
not seen.
