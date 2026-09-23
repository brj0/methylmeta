r"""Batch pipeline: fetch -> harmonize (agent) -> merge, for many datasets.

For each dataset in --dataset_list:
  1. Fetch metadata (and optionally IDATs) if not already on disk.
  2. If no config exists yet (or --force), invoke the AI agent to write one.
  3. Test the config against the real metadata.
Then, optionally, merge every dataset that passed into one table.

Failures on individual datasets never abort the run - they're logged and
collected into a report, so a 300-dataset run survives the 5 messy datasets
that need a human. Re-running is cheap: anything already fetched/harmonized
is skipped unless you pass --force / --refetch.

Usage:
    python scripts/harmonize_pipeline.py \\
        --dataset_list ~/methylmeta/datasets.txt \\
        --dataset_dir ~/methylmeta/data \\
        --output ~/methylmeta/merged.tsv

datasets.txt is one dataset ID per line; blank lines and lines starting
with '#' are ignored.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

import click

from methylmeta.agent import run_agent
from methylmeta.fetch import check_datasets, download_missing
from methylmeta.merger import MetadataMerger
from methylmeta.paths import CONFIGS_DIR, METADATA_OVERRIDES_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class DatasetResult:
    """Outcome of the pipeline for one dataset."""

    dataset_id: str
    fetched: bool = False
    agent_ran: bool = False
    harmonized_ok: bool = False
    error: str | None = None

    def line(self) -> str:
        status = "OK" if self.harmonized_ok else "FAILED"
        bits = [f"fetched={self.fetched}", f"agent_ran={self.agent_ran}"]
        if self.error:
            bits.append(f"error={self.error}")
        return f"{self.dataset_id}: {status} ({', '.join(bits)})"


def read_dataset_list(path: Path) -> list[str]:
    """Read dataset IDs from a text file, one per line."""
    ids = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#"):
            ids.append(line)
    return ids


def ensure_data(
    dataset_id: str,
    dataset_dir: Path,
    idat: bool,
) -> tuple[bool, str | None]:
    """Fetch metadata (and optionally IDATs) if missing. Returns (ok, err)."""
    status = check_datasets([dataset_id], dataset_dir, check_idat=idat)[0]
    if status.is_complete:
        return True, None

    download_missing([status], dataset_dir)

    status = check_datasets([dataset_id], dataset_dir, check_idat=idat)[0]
    if not status.is_complete:
        return False, f"download incomplete ({status})"
    return True, None


def harmonize_one(
    dataset_id: str,
    *,
    merger: MetadataMerger,
    config_dir: Path,
    dataset_dir: Path,
    metadata_dir: Path,
    idat: bool,
    model: str,
    force: bool,
    request_limit: int,
    tool_calls_limit: int,
) -> DatasetResult:
    """Run fetch + agent + test for one dataset, never raising."""
    result = DatasetResult(dataset_id=dataset_id)

    try:
        ok, err = ensure_data(dataset_id, dataset_dir, idat)
        result.fetched = ok
        if not ok:
            result.error = err
            return result

        has_config = not merger.missing_configs([dataset_id])
        if not has_config or force:
            agent_result = run_agent(
                dataset_id,
                config_dir=config_dir,
                dataset_dir=dataset_dir,
                metadata_overrides_dir=metadata_dir,
                model=model,
                allow_write=True,
                force=force,
                request_limit=request_limit,
                tool_calls_limit=tool_calls_limit,
            )
            result.agent_ran = True
            if not agent_result.success:
                result.error = agent_result.summary.splitlines()[0]
                return result

        report = merger.test(dataset_id)
        result.harmonized_ok = report.success
        if not report.success:
            result.error = "config exists but test() fails"
    except Exception as exc:  # noqa: BLE001 - isolate failures per dataset
        result.error = f"{type(exc).__name__}: {exc}"

    return result


@click.command()
@click.option(
    "--dataset_list",
    type=Path,
    required=True,
    help="Text file with one dataset ID per line.",
)
@click.option("--dataset_dir", type=Path, required=True)
@click.option(
    "--config_dir", type=Path, default=CONFIGS_DIR, show_default=True
)
@click.option(
    "--metadata_dir",
    type=Path,
    default=METADATA_OVERRIDES_DIR,
    show_default=True,
)
@click.option(
    "--idat/--no_idat",
    default=False,
    help="Also fetch IDATs (large - only needed for array_type/training).",
)
@click.option(
    "--model", default="deepseek:deepseek-v4-flash", show_default=True
)
@click.option(
    "--force",
    is_flag=True,
    help="Re-run the agent even for datasets that already have a config.",
)
@click.option("--request_limit", type=int, default=80, show_default=True)
@click.option("--tool_calls_limit", type=int, default=200, show_default=True)
@click.option(
    "--merge/--no_merge",
    default=True,
    help="Merge every successfully-harmonized dataset at the end.",
)
@click.option(
    "--array_types/--no_array_types",
    default=False,
    help="Fill array_type from IDAT headers after merging (needs --idat).",
)
@click.option("--output", type=Path, default=None)
@click.option(
    "--report",
    type=Path,
    default=None,
    help="Where to write the per-dataset run report (default: alongside "
    "--output, or printed only if --output is not given).",
)
def main(
    dataset_list: Path,
    dataset_dir: Path,
    config_dir: Path,
    metadata_dir: Path,
    idat: bool,
    model: str,
    force: bool,
    request_limit: int,
    tool_calls_limit: int,
    merge: bool,
    array_types: bool,
    output: Path | None,
    report: Path | None,
) -> None:
    """Fetch, harmonize (via agent), and optionally merge many datasets."""
    dataset_dir = dataset_dir.expanduser()
    dataset_dir.mkdir(parents=True, exist_ok=True)

    dataset_ids = read_dataset_list(dataset_list)
    if not dataset_ids:
        raise SystemExit(f"No dataset IDs found in {dataset_list}")
    logger.info("Pipeline for %d dataset(s)", len(dataset_ids))

    merger = MetadataMerger(
        config_dir=config_dir,
        dataset_dir=dataset_dir,
        metadata_overrides_dir=metadata_dir,
    )

    results = []
    for i, dataset_id in enumerate(dataset_ids, start=1):
        logger.info("[%d/%d] %s", i, len(dataset_ids), dataset_id)
        result = harmonize_one(
            dataset_id,
            merger=merger,
            config_dir=config_dir,
            dataset_dir=dataset_dir,
            metadata_dir=metadata_dir,
            idat=idat,
            model=model,
            force=force,
            request_limit=request_limit,
            tool_calls_limit=tool_calls_limit,
        )
        results.append(result)
        logger.info(result.line())

    ok_ids = [r.dataset_id for r in results if r.harmonized_ok]
    failed = [r for r in results if not r.harmonized_ok]

    report_lines = [r.line() for r in results]
    report_lines.append(
        f"\n{len(ok_ids)}/{len(results)} datasets harmonized OK."
    )
    report_text = "\n".join(report_lines)
    click.echo(report_text)

    if report is None and output is not None:
        report = output.with_suffix(".report.txt")
    if report is not None:
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(report_text, encoding="utf-8")
        click.echo(f"Report -> {report}")

    if not merge:
        return
    if not ok_ids:
        raise SystemExit("Nothing harmonized successfully - nothing to merge.")
    if failed:
        logger.warning(
            "Merging only the %d dataset(s) that passed; excluding: %s",
            len(ok_ids),
            [r.dataset_id for r in failed],
        )

    df = merger.merge(dataset_ids=ok_ids)

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        df.write_csv(output, separator="\t")
        click.echo(f"Wrote {len(df)} samples -> {output}")

    if array_types:
        df = merger.add_array_types(df)
        if output is not None:
            df.write_csv(output, separator="\t")
            click.echo(f"Wrote {len(df)} samples -> {output} (array_type)")


if __name__ == "__main__":
    main()
