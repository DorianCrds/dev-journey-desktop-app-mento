# app/views/pages/notions_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QSizePolicy, QHBoxLayout, QLabel, QListWidget, \
    QTextEdit

from app.views.pages.notions.creation_form_page import CreationFormPage
from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_text import CustomViewTitleLabel, CustomPrimaryContentLabel


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

        self._list_page = QWidget()
        self._list_page_v_layout = QVBoxLayout(self._list_page)

        self._header_widget = QWidget()
        self._header_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self._header_h_layout = QHBoxLayout(self._header_widget)

        self._header_h_layout.addStretch()

        self.add_button = CustomToolButton("+ Add")
        self._header_h_layout.addWidget(self.add_button)

        self.edit_button = CustomToolButton("~ Edit")
        self._header_h_layout.addWidget(self.edit_button)

        self.delete_button = CustomToolButton("- Remove")
        self._header_h_layout.addWidget(self.delete_button)

        self._content_widget = QWidget()
        self._content_h_layout = QHBoxLayout(self._content_widget)

        self._list_container_widget = QWidget()
        self._list_container_v_layout = QVBoxLayout(self._list_container_widget)

        self._list_widget_header = QWidget()
        self._list_widget_header_h_layout = QHBoxLayout(self._list_widget_header)

        self._title_column_header = QLabel("Title")
        self._category_column_header = QLabel("Category")
        self._status_column_header = QLabel("Status")

        self._list_widget_header_h_layout.addWidget(self._title_column_header)
        self._list_widget_header_h_layout.addWidget(self._category_column_header)
        self._list_widget_header_h_layout.addWidget(self._status_column_header)

        self._list_widget_header_h_layout.setStretch(0, 3)
        self._list_widget_header_h_layout.setStretch(1, 2)
        self._list_widget_header_h_layout.setStretch(2, 1)

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.list_widget.setObjectName("notions_list_widget")

        self._list_container_v_layout.addWidget(self._list_widget_header)
        self._list_container_v_layout.addWidget(self.list_widget)

        self.detail_widget = QWidget()
        self.detail_widget.setObjectName("notions_detail_widget")
        self._detail_v_layout = QVBoxLayout(self.detail_widget)

        self._detail_title_label = CustomPrimaryContentLabel("Title")
        self.detail_title_value = QLabel("")

        self._detail_category_label = CustomPrimaryContentLabel("Category")
        self.detail_category_value = QLabel("")

        self._detail_context_label = CustomPrimaryContentLabel("Context")
        self.detail_context_value = QTextEdit("")
        self.detail_context_value.setReadOnly(True)

        self._detail_description_label = CustomPrimaryContentLabel("Description")
        self.detail_description_value = QTextEdit("")
        self.detail_description_value.setReadOnly(True)

        self._detail_status_label = CustomPrimaryContentLabel("Status")
        self.detail_status_value = QLabel("")

        self._detail_v_layout.addWidget(self._detail_title_label)
        self._detail_v_layout.addWidget(self.detail_title_value)
        self._detail_v_layout.addWidget(self._detail_category_label)
        self._detail_v_layout.addWidget(self.detail_category_value)
        self._detail_v_layout.addWidget(self._detail_context_label)
        self._detail_v_layout.addWidget(self.detail_context_value)
        self._detail_v_layout.addWidget(self._detail_description_label)
        self._detail_v_layout.addWidget(self.detail_description_value)
        self._detail_v_layout.addWidget(self._detail_status_label)
        self._detail_v_layout.addWidget(self.detail_status_value)
        self._detail_v_layout.addStretch()

        self._content_h_layout.addWidget(self._list_container_widget)
        self._content_h_layout.addWidget(self.detail_widget)

        self._content_h_layout.setStretch(0, 2)
        self._content_h_layout.setStretch(1, 1)

        self._list_page_v_layout.addWidget(self._header_widget)
        self._list_page_v_layout.addWidget(self._content_widget)

        self.content.addWidget(self._list_page)

        self.form_page = CreationFormPage()
        self.content.addWidget(self.form_page)

        self._main_v_layout.addWidget(self.content)

        self.content.setCurrentIndex(0)
