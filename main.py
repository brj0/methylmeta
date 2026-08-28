import logging
from pathlib import Path

import click

from methylmeta import MetadataMerger

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--config-dir", type=Path, default="configs/datasets", show_default=True
)
@click.option("--input-dir", type=Path, required=True)
@click.option("--output", type=Path, required=True)
@click.option("--idat-dir", type=Path, default=None)
@click.option("--strict/--no-strict", default=True)
def main(config_dir, input_dir, output, idat_dir, strict):
    merger = MetadataMerger(
        config_dir=config_dir,
        strict=strict,
        idat_dir=idat_dir,
    )
    df = merger.merge_directory(input_dir)
    output = Path(output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(output, separator="\t")
    click.echo(f"Wrote {len(df)} samples → {output}")


if __name__ == "__main__":
    main()
