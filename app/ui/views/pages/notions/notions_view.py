# app/ui/views/pages/notions_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QSizePolicy

from app.ui.views.components.sub_components.custom_texts import CustomTitleMain
from app.ui.views.pages.notions.notion_detail_page import NotionDetailPage
from app.ui.views.pages.notions.notion_form_page import NotionFormPage
from app.ui.views.pages.notions.notions_list_page import NotionsListPage


class NotionsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)

        title = CustomTitleMain("Organize your Notions")

        self.notions_stacked_widget = QStackedWidget()

        self.notions_list_page = NotionsListPage()
        self.notion_detail_page = NotionDetailPage()
        self.notion_form_page = NotionFormPage()

        self.notions_stacked_widget.addWidget(self.notions_list_page)
        self.notions_stacked_widget.addWidget(self.notion_detail_page)
        self.notions_stacked_widget.addWidget(self.notion_form_page)

        layout.addWidget(title)
        layout.addWidget(self.notions_stacked_widget)