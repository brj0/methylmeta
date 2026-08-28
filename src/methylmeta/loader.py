from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def load_dataset_module(py_path: Path) -> ModuleType:
    """Dynamically load a dataset .py file as a module."""
    py_path = Path(py_path).resolve()
    module_name = f"metadata.{py_path.stem}"

    spec = importlib.util.spec_from_file_location(module_name, py_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {py_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
