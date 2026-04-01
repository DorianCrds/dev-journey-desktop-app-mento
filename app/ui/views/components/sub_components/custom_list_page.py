from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.ui.views.components.sub_components.custom_cards_scroll_area import CustomCardsScrollArea
from app.ui.views.components.sub_components.custom_headers import PageActionsHeader


class CustomListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(24)

        self.header = PageActionsHeader()

        self.scroll_area = CustomCardsScrollArea()

        layout.addWidget(self.header)
        layout.addWidget(self.scroll_area)