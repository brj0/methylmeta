"""Every shipped dataset config must load and follow the contract."""

from pathlib import Path

import pytest

from methylmeta.merger import MetadataMerger, unknown_config_functions
from methylmeta.paths import CONFIGS_DIR

_MERGER = MetadataMerger(config_dir=CONFIGS_DIR, dataset_dir=Path("."))
DATASET_IDS = _MERGER.available_datasets()


def test_configs_found() -> None:
    assert DATASET_IDS


@pytest.mark.parametrize("dataset_id", DATASET_IDS)
def test_config_follows_contract(dataset_id: str) -> None:
    # load_config raises if dataset_id(None) != the filename stem.
    module = _MERGER.load_config(dataset_id)
    assert unknown_config_functions(module) == []
