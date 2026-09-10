"""Example: run the methylmeta agent on selected datasets."""

from pathlib import Path

from methylmeta.agent import run_agent
from methylmeta.paths import CONFIGS_DIR

DATASET_DIR = Path("~/methylmeta/data").expanduser()
MODEL = "deepseek:deepseek-flash"

DATASET_IDS = [
    "GSE320217",
]


def main() -> None:
    for dataset_id in DATASET_IDS:
        result = run_agent(
            dataset_id,
            config_dir=CONFIGS_DIR,
            dataset_dir=DATASET_DIR,
            model=MODEL,
            allow_write=True,
            force=True,
        )

        usage = result.usage

        print(f"\n{dataset_id}: {'OK' if result.success else 'FAILED'}")
        print(
            f"Requests: {usage.requests}"
            f" | Input: {usage.input_tokens:,}"
            f" | Output: {usage.output_tokens:,}"
            f" | Cost: ${usage.cost:.4f}"
        )

        if result.config_path:
            print(f"Config: {result.config_path}")

        print(result.summary)

        if not result.success:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
