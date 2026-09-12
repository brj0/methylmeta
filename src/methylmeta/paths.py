from importlib.metadata import PackageNotFoundError, version
from importlib.resources import files
from pathlib import Path
from typing import cast

from platformdirs import user_cache_dir

APP_NAME = "methylmeta"

CACHE_DIR = Path(user_cache_dir(APP_NAME))
LOG_DIR = CACHE_DIR / "logs"


CACHE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_app_version() -> str:
    """Return the installed package version."""
    try:
        return version(APP_NAME)
    except PackageNotFoundError:
        return "unknown"


def get_resource_path(package: str, resource_name: str = "") -> Path:
    """Returns the full path to the resource within the specified package."""
    resource = files(package).joinpath(resource_name)
    return cast(Path, resource)


PACKAGE_DIR = get_resource_path(APP_NAME)
DATA_DIR = PACKAGE_DIR / "data"
CONFIGS_DIR = PACKAGE_DIR.parent.parent / "configs" / "datasets"
TUMOR_TYPES_PATH = DATA_DIR / "tumor_types.yaml"

# Hand-curated metadata spreadsheets, keyed by dataset_id (e.g.
# "GSE140686.tsv"). Some datasets' GEO/ArrayExpress sample sheets are
# useless (bare patient numbers, no diagnoses) while the authors publish
# the real annotation as a supplementary spreadsheet on the paper's page.
# A file placed here for a given dataset_id is used *instead of* whatever
# is found in that dataset's own directory under --dataset_dir - see
# `merger.MetadataMerger._resolve_metadata_file`.
METADATA_OVERRIDES_DIR = PACKAGE_DIR.parent.parent / "data" / "metadata"
