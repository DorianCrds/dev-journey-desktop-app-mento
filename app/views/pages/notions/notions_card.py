# app/views/pages/notions/notions_card.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from app.services.dto.notion_dto import NotionReadDTO


class NotionCard(QWidget):
    def __init__(self, notion: NotionReadDTO):
        super().__init__()

        self.notion = notion

        self._main_h_layout = QHBoxLayout(self)

        self.title_label = QLabel(self.notion.title)
        self.category_label = QLabel(self.notion.category_title)
        self.status_label = QLabel(self.notion.status)

        self._main_h_layout.addWidget(self.title_label)
        self._main_h_layout.addWidget(self.category_label)
        self._main_h_layout.addWidget(self.status_label)

        self._main_h_layout.setStretch(0, 3)
        self._main_h_layout.setStretch(1, 2)
        self._main_h_layout.setStretch(2, 1)