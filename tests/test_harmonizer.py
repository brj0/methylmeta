"""Config loading (filename == dataset_id) and the test() report."""

from pathlib import Path

import pytest

from methylmeta.merger import MetadataMerger

CONFIG = """
def dataset_id(row):
    return "TST1"


def sample_id(row):
    return row["ID"]


def diagnosis(row):
    return row["Dx"]


def methylation_class(row):
    return {"blood": "CTRL_BLOOD", "other": None}[row["Dx"]]
"""


def make_merger(
    tmp_path: Path, config: str, filename: str = "TST1.py"
) -> MetadataMerger:
    config_dir = tmp_path / "configs"
    config_dir.mkdir()
    (config_dir / filename).write_text(config)

    data_dir = tmp_path / "data" / "TST1"
    data_dir.mkdir(parents=True)
    (data_dir / "meta.csv").write_text("ID,Dx\ns1,blood\ns2,blood\ns3,other\n")

    return MetadataMerger(
        config_dir=config_dir,
        dataset_dir=tmp_path / "data",
        metadata_overrides_dir=tmp_path / "no_overrides",
    )


def test_valid_config_passes(tmp_path: Path) -> None:
    report = make_merger(tmp_path, CONFIG).test("TST1")
    assert report.success
    assert report.ok_rows == 3


def test_filename_must_match_dataset_id(tmp_path: Path) -> None:
    merger = make_merger(tmp_path, CONFIG, filename="OTHER.py")
    with pytest.raises(ValueError, match="filename requires 'OTHER'"):
        merger.load_config("OTHER")


def test_missing_config(tmp_path: Path) -> None:
    merger = make_merger(tmp_path, CONFIG)
    assert merger.missing_configs(["TST1", "GSE1"]) == ["GSE1"]
    assert merger.available_datasets() == ["TST1"]
    with pytest.raises(ValueError, match="No config found"):
        merger.load_config("GSE1")


def test_broken_config_does_not_affect_others(tmp_path: Path) -> None:
    merger = make_merger(tmp_path, CONFIG)
    (merger.config_dir / "BROKEN.py").write_text("def dataset_id(row:\n")
    assert merger.test("TST1").success


def test_unknown_function_is_a_failure(tmp_path: Path) -> None:
    config = CONFIG + '\n\ndef material(row):\n    return "tissue"\n'
    merger = make_merger(tmp_path, config)

    report = merger.test("TST1")
    assert not report.success
    assert "material_type" in report.summary()

    with pytest.raises(ValueError, match="material"):
        merger.merge(["TST1"])


def test_helpers_and_imports_are_allowed(tmp_path: Path) -> None:
    config = (
        "from os.path import join\n\n"
        + CONFIG
        + '\n\ndef _helper(row):\n    return join("a", "b")\n'
    )
    assert make_merger(tmp_path, config).test("TST1").success


def test_coverage_and_mapping_table(tmp_path: Path) -> None:
    report = make_merger(tmp_path, CONFIG).test("TST1")

    summary = report.summary()
    assert "methylation_class: 2 (67%)" in summary
    assert "sex: 0 (0%)" in summary

    table = report.mapping_table()
    assert "blood -> CTRL_BLOOD" in table
    assert "other -> <None>" in table
    assert "more" in report.mapping_table(max_rows=1)
