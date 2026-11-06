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
    calls: list[list[str]] = []

    def fake_predict(self, dataset_id, todo, methods, cache_dir, show):
        calls.append(sorted(todo))
        return {
            sid: {"purity_absolute": 0.8, "purity_estimate": 0.6}
            for sid in todo
        }

    monkeypatch.setattr(MetadataMerger, "_predict_purities", fake_predict)
    df = merger.add_idat_paths(table())

    cache_dir = merger.dataset_dir.parent / "cache"
    out = merger.add_purities(df, show_progress=False, cache_dir=cache_dir)
    assert out["purity_absolute"].to_list() == [0.8, 0.8, None]
    assert out["purity_estimate"].to_list() == [0.6, 0.6, None]
    assert calls == [["s1", "s2"]]  # one batched call per dataset

    cache = json.loads((cache_dir / "TST1.json").read_text())
    assert set(cache["samples"]) == {"s1", "s2"}
    assert not list((merger.dataset_dir / "TST1").glob("*.json"))

    merger.add_purities(df, show_progress=False, cache_dir=cache_dir)
    assert len(calls) == 1  # second run hits the cache

