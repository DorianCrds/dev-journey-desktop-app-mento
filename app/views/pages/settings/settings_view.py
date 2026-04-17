# app/views/settings_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from app.views.components.main_components.basic_view import BasicView
from app.views.components.sub_components.custom_texts import CustomDocumentTitle, CustomTextNormal
from qute.design_system.spacing import Spacing
from qute.manager.theme_manager import ThemeManager
from qute.widgets.theme_radio_group import ThemeRadioGroup
from qute.design_system.typography import Typography


class SettingsView(BasicView):
    def __init__(self):
        super().__init__("Settings")

        self._setup_ui()

    def _setup_ui(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setSpacing(Spacing.V_FORM)

        title = CustomDocumentTitle("Theme")
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setFont(Typography.from_preset("body_md"))

        description = CustomTextNormal("Choose the appearance of the application.")
        description.setFont(Typography.from_preset("meta"))
        description.setObjectName("TextSecondary")

        self.theme_radio_group = ThemeRadioGroup(
            ThemeManager.instance().available_themes()
        )

        # --- Layout
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(8)
        layout.addWidget(self.theme_radio_group)

        # --- Add to main view
        self.content_layout.addWidget(container)
        self.content_layout.addStretch()