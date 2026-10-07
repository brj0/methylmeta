"""idat_path / drop_invalid / purity columns (IDATs are empty stubs)."""

import json
from pathlib import Path

import polars as pl
import pytest

from methylmeta.merger import MetadataMerger


@pytest.fixture
def merger(tmp_path: Path) -> MetadataMerger:
    data = tmp_path / "data" / "TST1"
    data.mkdir(parents=True)
    for sid in ("s1", "s2"):
        for color in ("Grn", "Red"):
            (data / f"{sid}_{color}.idat").touch()
    return MetadataMerger(config_dir=tmp_path, dataset_dir=tmp_path / "data")


def table() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "dataset_id": ["TST1"] * 3,
            "sample_id": ["s1", "s2", "s3"],  # s3 has no IDAT
            "array_type": ["450k", "invalid_array", "EPIC"],
        }
    )


def test_add_idat_paths(merger: MetadataMerger) -> None:
    df = merger.add_idat_paths(table())
    paths = df["idat_path"].to_list()
    assert paths[0] == str(merger.dataset_dir.resolve() / "TST1" / "s1")
    assert paths[2] is None
    assert df.height == 3


def test_drop_invalid(merger: MetadataMerger) -> None:
    df = merger.drop_invalid(merger.add_idat_paths(table()))
    assert df["sample_id"].to_list() == ["s1"]


def test_drop_invalid_needs_paths() -> None:
    with pytest.raises(ValueError, match="idat_path"):
        MetadataMerger.drop_invalid(table())


def test_add_purities_uses_cache(
    merger: MetadataMerger, monkeypatch: pytest.MonkeyPatch
) -> None:
    import mepylome

    calls: list[str] = []

    class FakeMethylData:
        def __init__(self, file: str, prep: str) -> None:
            calls.append(file)

        def predict_purity(self, method: str) -> object:
            import pandas as pd

            return pd.Series([0.8 if method == "absolute" else 0.6])

    monkeypatch.setattr(mepylome, "MethylData", FakeMethylData)
    df = merger.add_idat_paths(table())

    cache_dir = merger.dataset_dir.parent / "cache"
    out = merger.add_purities(df, show_progress=False, cache_dir=cache_dir)
    assert out["purity_absolute"].to_list() == [0.8, 0.8, None]
    assert out["purity_estimate"].to_list() == [0.6, 0.6, None]
    assert len(calls) == 2

    cache = json.loads((cache_dir / "TST1.json").read_text())
    assert set(cache["samples"]) == {"s1", "s2"}
    assert not list((merger.dataset_dir / "TST1").glob("*.json"))

    merger.add_purities(df, show_progress=False, cache_dir=cache_dir)
    assert len(calls) == 2  # second run hits the cache
