# qute/widgets/theme_toggle_button.py
from PySide6.QtWidgets import QPushButton
from qute.core.signals import theme_signals


class ThemeToggleButton(QPushButton):
    def __init__(self, light="light", dark="dark"):
        super().__init__("Toggle theme")

        self.light = light
        self.dark = dark

        self.setCheckable(True)

        self.toggled.connect(self._on_toggled)

        theme_signals.theme_applied.connect(self._sync)

    def _on_toggled(self, checked):
        theme = self.dark if checked else self.light
        theme_signals.theme_change_requested.emit(theme)

    def _sync(self, theme_name):
        self.setChecked(theme_name == self.dark)