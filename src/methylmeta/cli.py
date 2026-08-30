import logging
from pathlib import Path

import click

from methylmeta.merger import MetadataMerger
from methylmeta.paths import CONFIGS_DIR

logging.basicConfig(level=logging.INFO)


@click.group()
def cli() -> None:
    """Methylmeta command-line interface."""
    pass


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
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

    df = merger.merge(dataset_ids=dataset_ids)
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
@click.option("--max_unique", type=int, default=15, show_default=True)
@click.argument("dataset_id")
def profile(
    config_dir: Path,
    dataset_dir: Path,
    max_unique: int,
    dataset_id: str,
) -> None:
    """Summarize metadata columns before writing a config."""
    merger = MetadataMerger(config_dir=config_dir, dataset_dir=dataset_dir)
    click.echo(merger.profile(dataset_id, max_unique=max_unique).summary())


@cli.command()
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option("--dataset_dir", type=Path, required=True)
@click.argument("dataset_id")
def test(
    config_dir: Path,
    dataset_dir: Path,
    dataset_id: str,
) -> None:
    """Dry-run one dataset's config against its real metadata.

    Reports every failing row and why (grouped by identical error), without
    aborting on the first bad row - the fast loop for writing/fixing configs.
    """
    merger = MetadataMerger(config_dir=config_dir, dataset_dir=dataset_dir)
    report = merger.test(dataset_id)
    click.echo(report.summary())
    raise SystemExit(0 if report.success else 1)


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
