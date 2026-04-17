# app/views/main_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

from app.views.components.main_components.custom_body import CustomBody
from app.views.components.main_components.custom_menu import CustomMenu


class MainWindow(QMainWindow):
    SIDEBAR_WIDTH = 240

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setObjectName("MainWindow")
        self.setWindowTitle("Mento")
        self.resize(1400, 900)
        self.setMinimumSize(1000, 700)

        central_widget = QWidget()
        central_widget.setObjectName("CentralWidget")
        central_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.menu = CustomMenu()
        self.menu.setFixedWidth(self.SIDEBAR_WIDTH)

        self.body = CustomBody()

        main_layout.addWidget(self.menu)
        main_layout.addWidget(self.body, 1)