# app/views/notions/notions_card.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from app.domain.models.notion import Notion


class NotionCard(QWidget):
    def __init__(self, notion: Notion):
        super().__init__()

        self.notion = notion

        self._main_h_layout = QHBoxLayout(self)

        self.title_label = QLabel(self.notion.title)
        self.category_label = QLabel(str(self.notion.category_id))
        self.status_label = QLabel(self.notion.status)

        self._main_h_layout.addWidget(self.title_label)
        self._main_h_layout.addWidget(self.category_label)
        self._main_h_layout.addWidget(self.status_label)