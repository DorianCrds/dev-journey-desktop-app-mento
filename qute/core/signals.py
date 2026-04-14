# qute/core/signals.py
from PySide6.QtCore import QObject, Signal

class ThemeSignals(QObject):
    theme_change_requested = Signal(str)

    theme_applied = Signal(str)

theme_signals = ThemeSignals()
