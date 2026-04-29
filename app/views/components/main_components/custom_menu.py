# app/views/components/main_components/custom_menu.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from app.views.components.sub_components.custom_buttons import CustomMenuToolButton
from qute.design_system.spacing import Spacing


class CustomMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Sidebar")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)
        self._main_v_layout.setContentsMargins(Spacing.MD, Spacing.LG, Spacing.MD, Spacing.LG)
        self._main_v_layout.setSpacing(Spacing.SM)

        self._title_label = QLabel("Mento")
        self._title_label.setObjectName("SidebarTitle")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.dashboard_button = CustomMenuToolButton("Dashboard")
        self.notions_button = CustomMenuToolButton("Notions")
        self.categories_button = CustomMenuToolButton("Categories")
        self.tags_button = CustomMenuToolButton("Tags")
        self.getting_started_button = CustomMenuToolButton("Start Here")
        self.settings_button = CustomMenuToolButton("Settings")

        self._main_v_layout.addWidget(self._title_label)
        self._main_v_layout.addSpacing(Spacing.LG)
        self._main_v_layout.addWidget(self.dashboard_button)
        self._main_v_layout.addWidget(self.notions_button)
        self._main_v_layout.addWidget(self.categories_button)
        self._main_v_layout.addWidget(self.tags_button)
        self._main_v_layout.addStretch()
        self._main_v_layout.addWidget(self.getting_started_button)
        self._main_v_layout.addWidget(self.settings_button)
