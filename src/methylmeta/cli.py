import logging
from pathlib import Path

import click

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
    help=(
        "Directory where the raw metadata and idat files are saved."
    ),
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


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
@metadata_dir_option
@click.option("--max_unique", type=int, default=15, show_default=True)
@click.argument("dataset_id")
def profile(
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
    max_unique: int,
    dataset_id: str,
) -> None:
    """Summarize metadata columns before writing a config."""
    merger = MetadataMerger(
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_dir,
    )
    click.echo(merger.profile(dataset_id, max_unique=max_unique).summary())


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
@metadata_dir_option
@click.argument("dataset_id")
def test(
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
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
    click.echo(report.summary())
    raise SystemExit(0 if report.success else 1)


@cli.command()
@click.argument("dataset_id")
@click.option("--dataset_dir", type=Path, required=True)
@click.option(
    "--idat/--no_idat",
    default=False,
    help="Also download IDAT files (large - opt in explicitly).",
)
def fetch(
    dataset_id: str,
    dataset_dir: Path,
    idat: bool,
) -> None:
    """Download metadata (and optionally IDATs) for one dataset.

    Skips anything already present on disk - only the missing piece(s)
    are downloaded, matching the layout MetadataMerger expects
    (dataset_dir/<dataset_id>/).
    """
    from methylmeta.fetch import check_datasets, download_missing

    dataset_dir = Path(dataset_dir).expanduser()
    dataset_dir.mkdir(parents=True, exist_ok=True)

    before = check_datasets([dataset_id], dataset_dir, check_idat=idat)[0]
    click.echo(f"before: {before}")

    if before.is_complete:
        click.echo(f"{dataset_id}: already complete, nothing to fetch.")
        return

    download_missing([before], dataset_dir)

    after = check_datasets([dataset_id], dataset_dir, check_idat=idat)[0]
    click.echo(f"after:  {after}")
    if not after.is_complete:
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
    default=40,
    show_default=True,
    help=(
        "Max LLM requests before the agent gives up (raise for messy/large "
        "datasets)."
    ),
)
@click.option(
    "--tool_calls_limit",
    type=int,
    default=100,
    show_default=True,
    help=(
        "Max tool calls before the agent gives up (raise for messy/large "
        "datasets)."
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
    )
    click.echo(result.summary)
    if result.config_path:
        click.echo(f"Config: {result.config_path}")
    if not result.success:
        raise SystemExit(1)


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
