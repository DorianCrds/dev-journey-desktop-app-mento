# app/utils/path.py
from pathlib import Path
import os
import sys


APP_NAME = "Mento"


def get_base_path() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    return Path(__file__).resolve().parents[2]


def resource_path(relative_path: str | Path) -> Path:
    return get_base_path() / relative_path


def get_user_data_path() -> Path:
    if sys.platform == "win32":
        base_dir = os.environ.get("LOCALAPPDATA")
        if base_dir:
            return Path(base_dir) / APP_NAME
        return Path.home() / "AppData" / "Local" / APP_NAME

    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / APP_NAME

    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / APP_NAME