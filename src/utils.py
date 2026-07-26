"""Shared helpers: config loading, seeding, timing. Nothing runs at import time."""
from __future__ import annotations

import random
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator

import numpy as np
import yaml


def load_config(path: str | Path = "config.yaml") -> Dict[str, Any]:
    """Read a YAML config file and return it as a plain dict."""
    with Path(path).open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def set_seed(seed: int = 42) -> None:
    """Seed Python's and NumPy's RNGs so a run is reproducible."""
    random.seed(seed)
    np.random.seed(seed)


@contextmanager
def timed() -> Iterator[Dict[str, float]]:
    """Context manager that records wall-clock seconds for the enclosed block."""
    record: Dict[str, float] = {}
    start = time.perf_counter()
    try:
        yield record
    finally:
        record["elapsed_s"] = time.perf_counter() - start
        