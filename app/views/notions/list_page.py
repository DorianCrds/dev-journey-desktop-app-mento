# app/views/notions/list_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QTableView,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QSizePolicy, QHeaderView,
)

from app.views.sub_components.custom_buttons import CustomToolButton


class ListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("list_page")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self):
        self._main_v_layout = QVBoxLayout(self)

        self._header_widget = QWidget()
        self._header_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self._header_h_layout = QHBoxLayout(self._header_widget)

        self._header_h_layout.addStretch()

        self.add_button = CustomToolButton("+ Add")
        self._header_h_layout.addWidget(self.add_button)

        self.edit_button = CustomToolButton("~ Edit")
        self._header_h_layout.addWidget(self.edit_button)

        self.delete_button = CustomToolButton("- Remove")
        self._header_h_layout.addWidget(self.delete_button)

        self._splitter = QSplitter(Qt.Orientation.Horizontal)

        self.table_view = QTableView()
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.table_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_view.setMinimumWidth(300)

        self._splitter.addWidget(self.table_view)

        self._detail_widget = QWidget()
        self._detail_widget.setMinimumWidth(400)
        self._detail_layout = QFormLayout(self._detail_widget)

        self.title_input = QLineEdit()
        self.title_input.setReadOnly(True)
        self.category_input = QLineEdit()
        self.category_input.setReadOnly(True)
        self.status_input = QLineEdit()
        self.status_input.setReadOnly(True)
        self.context_input = QTextEdit()
        self.context_input.setReadOnly(True)
        self.description_input = QTextEdit()
        self.description_input.setReadOnly(True)

        self._detail_layout.addRow("Title :", self.title_input)
        self._detail_layout.addRow("Category :", self.category_input)
        self._detail_layout.addRow("Status :", self.status_input)
        self._detail_layout.addRow("Context :", self.context_input)
        self._detail_layout.addRow("Description :", self.description_input)

        self._splitter.addWidget(self._detail_widget)

        self._splitter.setStretchFactor(0, 6)
        self._splitter.setStretchFactor(1, 4)

        self._splitter.setCollapsible(0, False)
        self._splitter.setCollapsible(1, False)

        self._main_v_layout.addWidget(self._header_widget)
        self._main_v_layout.addWidget(self._splitter)
