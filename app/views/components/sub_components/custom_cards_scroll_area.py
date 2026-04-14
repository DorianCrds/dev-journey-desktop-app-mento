from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout


class CustomCardsScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True)
        self.setFrameShape(QScrollArea.Shape.NoFrame)

        self._cards_container = QWidget()
        self.cards_layout = QVBoxLayout(self._cards_container)
        self.cards_layout.setSpacing(8)
        self.cards_layout.setContentsMargins(16, 0, 16, 0)
        self.cards_layout.addStretch()

        self.setWidget(self._cards_container)
