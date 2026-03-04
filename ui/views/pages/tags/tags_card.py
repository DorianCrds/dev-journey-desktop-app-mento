# app/views/pages/tags/tags_card.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from app.domain.models.tag import Tag


class TagCard(QWidget):
    def __init__(self, tag: Tag):
        super().__init__()

        self.tag = tag

        self._main_h_layout = QHBoxLayout(self)

        self.title_label = QLabel(self.tag.title)

        self._main_h_layout.addWidget(self.title_label)