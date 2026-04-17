# app/views/components/sub_components/custom_cards_scroll_area.py
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from qute.design_system.spacing import Spacing


class CustomCardsScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.Shape.NoFrame)

        self._cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self._cards_container)
        self.cards_layout.setSpacing(Spacing.SM)
        self.cards_layout.setContentsMargins(Spacing.MD, 0, Spacing.MD, 0)
        self.cards_layout.addStretch()

        self.setWidget(self._cards_container)
