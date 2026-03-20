# app/ui/views/pages/tags/tags_view.py
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QScrollArea

from app.ui.views.components.sub_components.custom_buttons import CustomIconMediumToolButton
from app.ui.views.components.sub_components.custom_texts import CustomTitleMain


class TagsView(QWidget):
    refresh_notions_required = Signal()

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)

        title = CustomTitleMain("Handle available Tags")

        tags_page = QWidget()
        tags_page_layout = QVBoxLayout(tags_page)

        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.add_tag_button = CustomIconMediumToolButton("assets/icons/plus.svg")

        header_layout.addWidget(self.add_tag_button)
        header_layout.addStretch()

        tags_page_layout.addWidget(header)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)

        self._cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self._cards_container)
        self.cards_layout.setSpacing(8)
        self.cards_layout.setContentsMargins(0, 0, 0, 0)
        self.cards_layout.addStretch()

        scroll_area.setWidget(self._cards_container)

        tags_page_layout.addWidget(scroll_area)

        layout.addWidget(title)
        layout.addWidget(tags_page)
