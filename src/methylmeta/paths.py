from importlib.metadata import PackageNotFoundError, version
from importlib.resources import files
from pathlib import Path
from typing import cast

from platformdirs import user_cache_dir

APP_NAME = "methylmeta"

CACHE_DIR = Path(user_cache_dir(APP_NAME))
DATASETS_DIR = CACHE_DIR / "datasets"
LOG_DIR = CACHE_DIR / "logs"
CONFIGS_DIR = Path("configs/datasets/").resolve()


CACHE_DIR.mkdir(parents=True, exist_ok=True)
DATASETS_DIR.mkdir(parents=True, exist_ok=True)
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
