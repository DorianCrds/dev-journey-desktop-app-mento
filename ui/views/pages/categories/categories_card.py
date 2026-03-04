# app/views/pages/categories/categories_card.py
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from app.domain.models.category import Category


class CategoryCard(QWidget):
    def __init__(self, category: Category):
        super().__init__()

        self.category = category

        self._main_h_layout = QHBoxLayout(self)

        self.title_label = QLabel(self.category.title)

        self._main_h_layout.addWidget(self.title_label)