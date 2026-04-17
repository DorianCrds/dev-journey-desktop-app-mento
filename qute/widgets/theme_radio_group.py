# qute/widgets/theme_radio_group.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from qute.core.signals import theme_signals
from qute.manager.theme_manager import ThemeManager


class ThemeRadioGroup(QWidget):
    def __init__(self, themes):
        super().__init__()

        self._radios = {}

        layout = QVBoxLayout(self)
        group = QButtonGroup(self)

        for theme in themes:
            radio = CustomRadioButton(theme.capitalize())
            self._radios[theme] = radio

            group.addButton(radio)
            layout.addWidget(radio)

            radio.toggled.connect(
                lambda checked, t=theme: checked and theme_signals.theme_change_requested.emit(t)
            )

        theme_signals.theme_applied.connect(self._sync)

        current_theme = ThemeManager.instance().get_current_theme()
        if current_theme:
            self._sync(current_theme)

    def _sync(self, theme_name):
        if theme_name in self._radios:
            self._radios[theme_name].setChecked(True)


class CustomRadioButton(QRadioButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("RadioButton")