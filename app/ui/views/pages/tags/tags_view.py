# app/ui/views/pages/tags/tags_view.py

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.ui.views.components.main_components.basic_view import BasicView
from app.ui.views.components.sub_components.custom_cards_scroll_area import CustomCardsScrollArea
from app.ui.views.components.sub_components.custom_headers import PageActionsHeader


class TagsView(BasicView):
    refresh_notions_required = Signal()

    def __init__(self):
        super().__init__("Handle available Tags")

        self._setup_ui()

    def _setup_ui(self):
        tags_page = QWidget()
        tags_page_layout = QVBoxLayout(tags_page)
        tags_page_layout.setContentsMargins(0, 0, 0, 0)
        tags_page_layout.setSpacing(16)

        self.header = PageActionsHeader(create_mode=True)

        self.scroll_area = CustomCardsScrollArea()

        tags_page_layout.addWidget(self.header)
        tags_page_layout.addWidget(self.scroll_area)

        self.content_layout.addWidget(tags_page)
