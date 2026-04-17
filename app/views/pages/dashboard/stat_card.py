# app/views/pages/dashboard/stat_card.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout

from app.views.components.sub_components.custom_texts import CustomDocumentTitle, CustomTitleMain


class StatCard(QFrame):
    def __init__(self, title: str, value: str):
        super().__init__()
        self._title = title
        self._value = value

        self.setObjectName("CardStat")
        self.setFrameShape(QFrame.Shape.StyledPanel)

        layout = QVBoxLayout(self)

        title_label = CustomDocumentTitle(self._title)
        title_label.setObjectName("StatName")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        value_label = CustomTitleMain(self._value)
        value_label.setObjectName("StatValue")
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)
        layout.addWidget(value_label)