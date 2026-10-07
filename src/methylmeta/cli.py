import logging
from pathlib import Path

import click

from methylmeta.catalog import OUTPUT_FORMATS, query_datasets, render
from methylmeta.merger import MetadataMerger
from methylmeta.paths import CONFIGS_DIR, METADATA_OVERRIDES_DIR

metadata_dir_option = click.option(
    "--metadata_dir",
    type=Path,
    default=METADATA_OVERRIDES_DIR,
    show_default=True,
    help=(
        "Directory of hand-curated <dataset_id>.<ext> spreadsheets that "
        "override a dataset's GEO/ArrayExpress sample sheet (for datasets "
        "whose real annotation was only published on the paper's page)."
    ),
)

logging.basicConfig(level=logging.INFO)


@click.group()
def cli() -> None:
    """Methylmeta command-line interface."""
    pass


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option(
    "--dataset_dir",
    type=Path,
    required=True,
    help=("Directory where the raw metadata and idat files are saved."),
)
@metadata_dir_option
@click.option("--output", type=Path, default=None)
@click.option("--strict/--no_strict", default=True)
@click.option(
    "--array_types/--no_array_types",
    default=True,
    help=(
        "Fill in array_type by reading each sample's IDAT header. Slow on "
        "large merges - a checkpoint of the merge is written to --output "
        "before this step starts, so an interrupted array-type pass "
        "doesn't lose the metadata merge itself."
    ),
)
@click.option(
    "--idat_paths/--no_idat_paths",
    default=True,
    help="Add idat_path: absolute IDAT basepath (null if no IDAT on disk).",
)
@click.option(
    "--drop_invalid/--keep_invalid",
    default=False,
    help=(
        "Drop rows without IDAT or with array_type invalid_array "
        "(needs --idat_paths)."
    ),
)
@click.option(
    "--purities/--no_purities",
    default=False,
    help=(
        "Add purity_absolute / purity_estimate (RFpurify, needs IDATs). "
        "Cached per dataset in the methylmeta cache dir."
    ),
)
@click.option(
    "--datasets",
    default=None,
    help=(
        "Comma-separated dataset IDs to merge (default: everything with an "
        "existing config)."
    ),
)
@click.option(
    "--list_missing",
    is_flag=True,
    help=(
        "With --datasets, just print which of them have no config yet "
        "(for an agent to generate) and exit, instead of merging."
    ),
)
def merge(
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
    output: Path | None,
    strict: bool,
    array_types: bool,
    idat_paths: bool,
    drop_invalid: bool,
    purities: bool,
    datasets: str | None,
    list_missing: bool,
) -> None:
    """Harmonize and merge dataset(s) into one metadata table."""
    merger = MetadataMerger(
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_dir,
        strict=strict,
    )
    dataset_ids = (
        [d.strip() for d in datasets.split(",") if d.strip()]
        if datasets
        else []
    )

    if list_missing:
        missing = merger.missing_configs(dataset_ids)
        if missing:
            click.echo("Missing configs for:\n" + "\n".join(missing))
        else:
            click.echo("All requested datasets already have a config.")
        return

    if output is None:
        raise click.UsageError("--output is required unless --list_missing.")
    if (drop_invalid or purities) and not idat_paths:
        raise click.UsageError("--drop_invalid/--purities need --idat_paths.")

    output = Path(output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)

    df = merger.merge(dataset_ids=dataset_ids or None)
    df.write_csv(output, separator="\t")
    click.echo(
        f"Wrote {len(df)} samples → {output} (checkpoint, no array_type yet)"
    )

    if array_types:
        df = merger.add_array_types(df)
        df.write_csv(output, separator="\t")
        click.echo(f"Wrote {len(df)} samples → {output} (with array_type)")

    if idat_paths:
        df = merger.add_idat_paths(df)
        if drop_invalid:
            df = merger.drop_invalid(df)
        if purities:
            df = merger.add_purities(df)
        df.write_csv(output, separator="\t")
        click.echo(f"Wrote {len(df)} samples → {output} (with idat_path)")


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
@metadata_dir_option
@click.option("--max_unique", type=int, default=15, show_default=True)
@click.option("--sample_size", type=int, default=5, show_default=True)
@click.argument("dataset_id")
def profile(
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
    max_unique: int,
    sample_size: int,
    dataset_id: str,
) -> None:
    """Summarize metadata columns before writing a config."""
    merger = MetadataMerger(
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_dir,
    )
    click.echo(
        merger.profile(
            dataset_id, max_unique=max_unique, sample_size=sample_size
        ).summary()
    )


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
@metadata_dir_option
@click.option(
    "--max_mapping_rows",
    type=int,
    default=100,
    show_default=True,
    help="Max rows of the diagnosis -> methylation_class table (0 = all).",
)
@click.argument("dataset_id")
def test(
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
    max_mapping_rows: int,
    dataset_id: str,
) -> None:
    """Dry-run one dataset's config against its real metadata.

    Reports every failing row and why (grouped by identical error), without
    aborting on the first bad row - the fast loop for writing/fixing configs.
    """
    merger = MetadataMerger(
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_dir,
    )
    report = merger.test(dataset_id)
    click.echo(
        report.summary(
            max_mapping_rows=max_mapping_rows or None,
        )
    )
    raise SystemExit(0 if report.success else 1)


@cli.command()
@click.argument("dataset_ids", nargs=-1, required=True)
@click.option("--dataset_dir", type=Path, required=True)
@click.option(
    "--idat/--no_idat",
    default=False,
    help="Also download IDAT files (large - opt in explicitly).",
)
def fetch(
    dataset_ids: tuple[str, ...],
    dataset_dir: Path,
    idat: bool,
) -> None:
    r"""Download metadata (and optionally IDATs) for dataset(s).

    Skips anything already present on disk - only the missing piece(s)
    are downloaded, matching the layout MetadataMerger expects
    (dataset_dir/<dataset_id>/). Combine with `find`:

    \b
        methylmeta find --classes GBM_RTK2 --format ids > ids.txt
        methylmeta fetch $(cat ids.txt) --dataset_dir DIR
    """
    from methylmeta.fetch import check_datasets, download_missing

    dataset_dir = Path(dataset_dir).expanduser()
    dataset_dir.mkdir(parents=True, exist_ok=True)
    ids = list(dict.fromkeys(dataset_ids))

    before = check_datasets(ids, dataset_dir, check_idat=idat)
    for status in before:
        click.echo(f"before: {status}")

    incomplete = [s for s in before if not s.is_complete]
    if not incomplete:
        click.echo("All datasets already complete, nothing to fetch.")
        return

    download_missing(incomplete, dataset_dir)

    after = check_datasets(
        [s.dataset_id for s in incomplete], dataset_dir, check_idat=idat
    )
    for status in after:
        click.echo(f"after:  {status}")
    if not all(s.is_complete for s in after):
        raise SystemExit(1)


@cli.command()
@click.argument("dataset_id")
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
@metadata_dir_option
@click.option(
    "--model", default="deepseek:deepseek-v4-flash", show_default=True
)
@click.option(
    "--prompt", default=None, help="Additional instructions for the agent."
)
@click.option(
    "--force", is_flag=True, help="Allow replacing an existing config."
)
@click.option(
    "--write/--no-write",
    default=True,
    help="Allow the agent to write the dataset config.",
)
@click.option(
    "--request_limit",
    type=int,
    default=80,
    show_default=True,
    help=(
        "Max LLM requests before the agent gives up (raise for messy/large "
        "datasets)."
    ),
)
@click.option(
    "--tool_calls_limit",
    type=int,
    default=200,
    show_default=True,
    help=(
        "Max tool calls before the agent gives up (raise for messy/large "
        "datasets)."
    ),
)
@click.option(
    "--log_dir",
    type=Path,
    default=None,
    help=(
        "Write the full run trace (reasoning, tool calls, tool results) "
        "here as .log/.json files, for reviewing or improving the agent."
    ),
)
def agent(
    dataset_id: str,
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
    model: str,
    prompt: str | None,
    force: bool,
    write: bool,
    request_limit: int,
    tool_calls_limit: int,
    log_dir: Path | None,
) -> None:
    """Create or repair a dataset config with an AI agent."""
    from methylmeta.agent import run_agent

    result = run_agent(
        dataset_id,
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_dir,
        model=model,
        prompt=prompt,
        allow_write=write,
        force=force,
        request_limit=request_limit,
        tool_calls_limit=tool_calls_limit,
        log_dir=log_dir,
    )
    if log_dir is not None:
        click.echo(f"Trace log: {log_dir}")
    click.echo(result.summary)
    if result.config_path:
        click.echo(f"Config: {result.config_path}")
    if not result.success:
        raise SystemExit(1)


@cli.command()
@click.option(
    "--classes",
    multiple=True,
    help=(
        "WHO acronym(s) from tumor_types.yaml, comma-separated and/or "
        "repeated (see `search_vocab`)."
    ),
)
@click.option(
    "--family",
    "families",
    multiple=True,
    help="Tumor family tag(s), e.g. 'glioma' (comma-separated/repeated).",
)
@click.option(
    "--site",
    "sites",
    multiple=True,
    help="Substring of the tumor type's site, e.g. 'kidney' (repeatable).",
)
@click.option(
    "--descendants/--no_descendants",
    default=True,
    show_default=True,
    help="Also select sub-entities (via `parent`) of every selected class.",
)
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option(
    "--dataset_dir",
    type=Path,
    default=None,
    help="If given, report which datasets are already downloaded there.",
)
@click.option(
    "--idat/--no_idat",
    default=False,
    help="With --dataset_dir, only count a dataset as downloaded with IDATs.",
)
@click.option(
    "--missing",
    is_flag=True,
    help="With --dataset_dir, only list datasets that are not yet complete.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(OUTPUT_FORMATS),
    default="table",
    show_default=True,
    help=(
        "'ids': one dataset_id per line (for `methylmeta fetch`). "
        "'tsv': one row per dataset/class pair, for polars/pandas."
    ),
)
@click.option(
    "--max_classes",
    type=int,
    default=8,
    show_default=True,
    help="Max classes shown per dataset in the table (0 = all).",
)
def find(
    classes: tuple[str, ...],
    families: tuple[str, ...],
    sites: tuple[str, ...],
    descendants: bool,
    config_dir: Path,
    dataset_dir: Path | None,
    idat: bool,
    missing: bool,
    output_format: str,
    max_classes: int,
) -> None:
    """Find the datasets that contain given tumor types.

    Reads the dataset configs statically - no raw data needed, so use this
    before downloading. A dataset matches if its config can produce any of
    the selected classes (no case counts; a dataset with one rare case
    matches too). Several selectors are OR-ed. Without any selector, all
    datasets are listed with all their classes.

    Results go to stdout, warnings to stderr, so `--format ids` is safe to
    pipe.
    """
    try:
        result = query_datasets(
            config_dir,
            classes=classes,
            families=families,
            sites=sites,
            descendants=descendants,
            dataset_dir=dataset_dir,
            idat=idat,
            missing=missing,
        )
    except (ValueError, FileNotFoundError) as exc:
        raise click.UsageError(str(exc)) from exc

    for label in result.uncovered:
        click.echo(f"warning: no dataset covers {label}", err=True)
    text = render(result, output_format, max_classes)
    if text:
        click.echo(text)
    click.echo(f"{len(result.matches)} dataset(s)", err=True)


@cli.command("search_vocab")
@click.argument("query")
@click.option("--limit", type=int, default=10, show_default=True)
def search_vocab(query: str, limit: int) -> None:
    """Search WHO tumor types by free-text."""
    from methylmeta import search_tumor_types

    for tt in search_tumor_types(query, limit=limit):
        click.echo(str(tt))


if __name__ == "__main__":
    cli()
