# qute/widgets/theme_radio_group.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from qute.core.signals import theme_signals


class ThemeRadioGroup(QWidget):
    def __init__(self, themes):
        super().__init__()

        self._radios = {}

        layout = QVBoxLayout(self)
        group = QButtonGroup(self)

        for theme in themes:
            radio = QRadioButton(theme)
            self._radios[theme] = radio

            group.addButton(radio)
            layout.addWidget(radio)

            radio.toggled.connect(
                lambda checked, t=theme: checked and theme_signals.theme_change_requested.emit(t)
            )

        theme_signals.theme_applied.connect(self._sync)

    def _sync(self, theme_name):
        if theme_name in self._radios:
            self._radios[theme_name].setChecked(True)