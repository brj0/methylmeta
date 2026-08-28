import logging
from pathlib import Path

import click

from methylmeta import MetadataMerger

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--config-dir", type=Path, default="configs/datasets", show_default=True
)
@click.option(
    "--classes", type=Path, default="data/classes.csv", show_default=True
)
@click.option("--global-config", type=Path, default=None)
@click.option("--input-dir", type=Path, required=True)
@click.option("--output", type=Path, required=True)
@click.option("--idat-dir", type=Path, default=None)
@click.option("--strict/--no-strict", default=True)
def main(
    config_dir, classes, global_config, input_dir, output, idat_dir, strict
):
    merger = MetadataMerger(
        config_dir=config_dir,
        classes_path=classes,
        global_config_path=global_config,
        strict=strict,
        idat_dir=idat_dir,
    )
    df = merger.merge_directory(input_dir)
    output = Path(output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output, sep="\t", index=False)
    click.echo(f"Wrote {len(df)} samples → {output}")


if __name__ == "__main__":
    main()
