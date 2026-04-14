# app/ui/views/pages/notions_view.py

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStackedWidget, QSizePolicy

from app.views.components.main_components.basic_view import BasicView
from app.views.components.sub_components.custom_list_page import CustomListPage
from app.views.pages.notions.notion_detail_page import NotionDetailPage
from app.views.pages.notions.notion_form_page import NotionFormPage


class NotionsView(BasicView):
    def __init__(self):
        super().__init__("Organize your Notions")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._setup_ui()

    def _setup_ui(self):
        self.notions_stacked_widget = QStackedWidget()
        self.notions_stacked_widget.setContentsMargins(0, 0, 0, 0)

        self.notions_list_page = CustomListPage()
        self.notions_list_page.header.add_button.show()
        self.notion_detail_page = NotionDetailPage()
        self.notion_form_page = NotionFormPage()

        self.notions_stacked_widget.addWidget(self.notions_list_page)
        self.notions_stacked_widget.addWidget(self.notion_detail_page)
        self.notions_stacked_widget.addWidget(self.notion_form_page)

        self.content_layout.addWidget(self.notions_stacked_widget)
        self.content_layout.setSpacing(0)
