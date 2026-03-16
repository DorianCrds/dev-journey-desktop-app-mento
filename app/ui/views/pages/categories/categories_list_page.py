# app/ui/views/pages/categories/categories_list_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea

from app.ui.views.components.sub_components.custom_buttons import CustomToolButton


class CategoriesListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)

        header = QWidget()
        header_layout = QHBoxLayout(header)

        self.add_category_button = CustomToolButton("Add")
        self.edit_category_button = CustomToolButton("Edit")
        self.delete_category_button = CustomToolButton("Delete")

        header_layout.addWidget(self.add_category_button)
        header_layout.addWidget(self.edit_category_button)
        header_layout.addWidget(self.delete_category_button)
        header_layout.addStretch()

        self._scroll_area = QScrollArea()
        self._scroll_area.setWidgetResizable(True)
        self._scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)

        self._cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self._cards_container)
        self.cards_layout.setSpacing(8)
        self.cards_layout.setContentsMargins(0, 0, 0, 0)
        self.cards_layout.addStretch()

        self._scroll_area.setWidget(self._cards_container)

        layout.addWidget(header)
        layout.addWidget(self._scroll_area)