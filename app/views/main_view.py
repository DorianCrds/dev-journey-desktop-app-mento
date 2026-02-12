# app/views/main_view.py
from PySide6.QtWidgets import QMainWindow


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mento")
        self.resize(1050, 750)