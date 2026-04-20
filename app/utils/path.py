from pathlib import Path
import sys


def get_base_path() -> Path:
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent.parent.parent


def resource_path(relative_path: str) -> str:
    return str(get_base_path() / relative_path)