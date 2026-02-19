# app/views/notions_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QSizePolicy

from app.views.notions.creation_form_page import CreationFormPage
from app.views.notions.list_page import ListPage
from app.views.sub_components.custom_text import CustomViewTitleLabel


class NotionsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("notion_view")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

        self.setStyleSheet("""
            #notion_view {
                border: 2px solid green;
                border-radius: 6px;
                background-color: rgba(0, 255, 0, 30);
            }
            
            #list_page {
                border: 2px solid red;
                border-radius: 6px;
                background-color: rgba(255, 0, 0, 30);
            }

            #form_page {
                border: 2px solid blue;
                border-radius: 6px;
                background-color: rgba(0, 0, 255, 30);
            }
        """)

    def _setup_ui(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._main_v_layout = QVBoxLayout(self)

        self._view_label = CustomViewTitleLabel("Notions view")
        self._main_v_layout.addWidget(self._view_label)

        self.content = QStackedWidget()
        self.content.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.list_page = ListPage()
        self.content.addWidget(self.list_page)

        self.form_page = CreationFormPage()
        self.content.addWidget(self.form_page)

        self._main_v_layout.addWidget(self.content)

        self.content.setCurrentIndex(0)
