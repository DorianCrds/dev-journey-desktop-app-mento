# app/views/categories_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class CategoriesView(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):
        self._main_v_layout = QVBoxLayout(self)

        self._view_label = QLabel("Categories view")
        self._main_v_layout.addWidget(self._view_label)
        self._main_v_layout.addStretch()