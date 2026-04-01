# app/ui/views/pages/tags/tags_view.py

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea

from app.ui.views.components.main_components.basic_view import BasicView
from app.ui.views.components.sub_components.custom_buttons import CustomIconMediumToolButton
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
        tags_page_layout.setSpacing(24)

        self.header = PageActionsHeader(create_mode=True)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)

        self._cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self._cards_container)
        self.cards_layout.setSpacing(12)
        self.cards_layout.setContentsMargins(0, 0, 0, 0)
        self.cards_layout.addStretch()

        scroll_area.setWidget(self._cards_container)

        tags_page_layout.addWidget(self.header)
        tags_page_layout.addWidget(scroll_area)

        self.content_layout.addWidget(tags_page)
