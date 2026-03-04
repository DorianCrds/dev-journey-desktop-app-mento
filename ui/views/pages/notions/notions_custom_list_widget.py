# app/views/pages/notions/notions_custom_list_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget


class CustomNotionsListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)

        self._header_widget = QWidget()
        self._header_h_layout = QHBoxLayout(self._header_widget)

        self._notion_title_column_header = QLabel("Title")
        self._notion_category_column_header = QLabel("Category")
        self._notion_status_column_header = QLabel("Status")

        self._header_h_layout.addWidget(self._notion_title_column_header)
        self._header_h_layout.addWidget(self._notion_category_column_header)
        self._header_h_layout.addWidget(self._notion_status_column_header)

        self._header_h_layout.setStretch(0, 3)
        self._header_h_layout.setStretch(1, 2)
        self._header_h_layout.setStretch(2, 1)

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)

        self._main_v_layout.addWidget(self._header_widget)
        self._main_v_layout.addWidget(self.list_widget)
