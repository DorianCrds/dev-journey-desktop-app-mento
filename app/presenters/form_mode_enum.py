# app/presenters/form_mode_enum.py
from enum import Enum, auto


class FormMode(Enum):
    CREATE = auto()
    EDIT = auto()