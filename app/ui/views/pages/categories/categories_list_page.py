# app/ui/views/pages/categories/categories_list_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea

from app.ui.views.components.sub_components.custom_cards_scroll_area import CustomCardsScrollArea
from app.ui.views.components.sub_components.custom_headers import PageActionsHeader


class CategoriesListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        self.header = PageActionsHeader(create_mode=True, edit_mode=True, delete_mode=True)

        self.scroll_area = CustomCardsScrollArea()

        layout.addWidget(self.header)
        layout.addWidget(self.scroll_area)