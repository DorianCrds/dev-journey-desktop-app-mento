# app/ui/views/pages/notions/notions_list_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget

from app.ui.views.components.sub_components.list_page_header import PageActionsHeader


class NotionsListPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        self.header = PageActionsHeader()
        self.header.add_button.show()

        # TODO: remove QListWidget
        self.list_widget = QListWidget()
        self.list_widget.setSpacing(8)
        self.list_widget.setContentsMargins(0, 0, 0, 0)
        self.list_widget.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout.addWidget(self.header)
        layout.addWidget(self.list_widget)