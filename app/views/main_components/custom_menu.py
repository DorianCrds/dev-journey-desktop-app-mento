from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QToolButton

from app.views.sub_components.custom_buttons import CustomMenuToolButton


class CustomMenu(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

        self.setStyleSheet(
            """
                #menu {
                    border: 1px solid gray;
                    border-radius: 7px;
                }
                
                #app_name_label {
                    border: 1px solid gray;
                    border-left: none;
                    border-top: none;
                    border-right: none;
                    padding: 10px;
                }
            """
        )

    def _setup_ui(self):
        self.setObjectName("menu")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._main_v_layout = QVBoxLayout(self)

        self._title_label = QLabel("MENTO")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._title_label.setObjectName("app_name_label")

        self.dashboard_button = CustomMenuToolButton()
        self.dashboard_button.setText("Dashboard")
        self.notions_button = CustomMenuToolButton()
        self.notions_button.setText("Notions")
        self.categories_button = CustomMenuToolButton()
        self.categories_button.setText("Categories")
        self.tags_button = CustomMenuToolButton()
        self.tags_button.setText("Tags")
        self.infos_button = CustomMenuToolButton()
        self.infos_button.setText("Infos")
        self.settings_button = CustomMenuToolButton()
        self.settings_button.setText("Settings")

        self._main_v_layout.addWidget(self._title_label)
        self._main_v_layout.addWidget(self.dashboard_button)
        self._main_v_layout.addWidget(self.notions_button)
        self._main_v_layout.addWidget(self.categories_button)
        self._main_v_layout.addWidget(self.tags_button)
        self._main_v_layout.addStretch()
        self._main_v_layout.addWidget(self.infos_button)
        self._main_v_layout.addWidget(self.settings_button)


