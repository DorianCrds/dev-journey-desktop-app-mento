# app/ui/views/pages/notions/notions_list_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget

from app.ui.views.components.sub_components.custom_buttons import CustomToolButton


class NotionsListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(8)

        self.add_notion_button = CustomToolButton("Add Notion")
        header_layout.addWidget(self.add_notion_button)
        header_layout.addStretch()

        self.list_widget = QListWidget()
        self.list_widget.setSpacing(8)
        self.list_widget.setContentsMargins(0, 0, 0, 0)
        self.list_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout.addWidget(header)
        layout.addWidget(self.list_widget)