# app/ui/views/components/main_components/custom_menu.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from app.ui.views.components.sub_components.custom_buttons import CustomMenuToolButton


class CustomMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Sidebar")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)
        self._main_v_layout.setContentsMargins(16, 24, 16, 24)
        self._main_v_layout.setSpacing(8)

        self._title_label = QLabel("Mento")
        self._title_label.setObjectName("SidebarTitle")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.dashboard_button = CustomMenuToolButton("Dashboard")
        self.notions_button = CustomMenuToolButton("Notions")
        self.categories_button = CustomMenuToolButton("Categories")
        self.tags_button = CustomMenuToolButton("Tags")
        self.infos_button = CustomMenuToolButton("Infos")
        self.settings_button = CustomMenuToolButton("Settings")

        self._main_v_layout.addWidget(self._title_label)
        self._main_v_layout.addSpacing(24)
        self._main_v_layout.addWidget(self.dashboard_button)
        self._main_v_layout.addWidget(self.notions_button)
        self._main_v_layout.addWidget(self.categories_button)
        self._main_v_layout.addWidget(self.tags_button)
        self._main_v_layout.addStretch()
        self._main_v_layout.addWidget(self.infos_button)
        self._main_v_layout.addWidget(self.settings_button)
