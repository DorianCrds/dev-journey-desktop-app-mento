# app/utils/path.py
from pathlib import Path
import sys


def get_base_path() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    return Path(__file__).resolve().parents[2]


def resource_path(relative_path: str | Path) -> Path:
    return get_base_path() / relative_path
