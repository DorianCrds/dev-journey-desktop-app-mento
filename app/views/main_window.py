# app/views/main_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from app.views.components.main_components.custom_body import CustomBody
from app.views.components.main_components.custom_menu import CustomMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):
        self.setObjectName("main_window")
        self.setWindowTitle("Mento")
        self.resize(1400, 900)
        self.setMinimumWidth(900)
        self.setMinimumHeight(700)

        self._central_widget = QWidget()
        self._central_widget.setObjectName("central_widget")
        self._main_layout = QHBoxLayout(self._central_widget)
        self.setCentralWidget(self._central_widget)

        self.menu = CustomMenu()
        self._menu_v_layout = QVBoxLayout(self.menu)
        self.body = CustomBody()
        self._body_v_layout = QVBoxLayout(self.body)

        self._main_layout.addWidget(self.menu)
        self._main_layout.addWidget(self.body)

        self._main_layout.setStretch(0, 1)
        self._main_layout.setStretch(1, 6)

        # self.setStyleSheet("""
        #     #central_widget {
        #         background-color: white;
        #     }
        # """)
