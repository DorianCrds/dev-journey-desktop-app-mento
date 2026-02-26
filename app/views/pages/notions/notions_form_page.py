# app/views/pages/notions/notions_form_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox, QLineEdit, QTextEdit, \
    QScrollArea, QCheckBox, QSizePolicy

from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_texts import CustomFormErrorLabel


class NotionsFormPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("creation_form_page")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.tag_checkboxes: list[QCheckBox] = []

        self._setup_ui()

        self.setStyleSheet("""
            #creation_form_page {
                border: 2px solid red;
            }
            
            #notion_form_header {
                border: 2px solid orange;
            }
            
            #notion_form_container {
                border: 2px solid blue;
            }
            
            #notion_form_widget {
                border: 2px solid green;
            }
        """)

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)

        self._header_widget = QWidget()
        self._header_widget.setObjectName("notion_form_header")
        self._header_h_layout = QHBoxLayout(self._header_widget)

        self.back_button = CustomToolButton("< Back")
        self._header_h_layout.addWidget(self.back_button)
        self._header_h_layout.addStretch()

        self._main_v_layout.addWidget(self._header_widget)

        self._form_container = QWidget()
        self._form_container.setObjectName("notion_form_container")
        self._form_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._form_container_layout = QHBoxLayout(self._form_container)

        self._form_container_layout.addStretch()

        self._form_widget = QWidget()
        self._form_widget.setObjectName("notion_form_widget")

        self._form_layout = QFormLayout(self._form_widget)

        self.title_input = QLineEdit(placeholderText="Notion's name")

        self.form_title_error = CustomFormErrorLabel("")
        self.form_title_error.hide()

        self.category_input = QComboBox()
        self.category_input.setPlaceholderText("Choose a category")
        self.category_input.setCurrentIndex(0)
        self.form_category_error = CustomFormErrorLabel("")
        self.form_category_error.hide()

        self.tags_scroll_area = QScrollArea()
        self.tags_scroll_area.setWidgetResizable(True)
        self.tags_scroll_area.setMaximumHeight(150)
        self.tags_scroll_area.setMinimumHeight(70)

        self._tags_container_widget = QWidget()
        self._tags_container_widget.setObjectName("tags_container")
        self.tags_layout = QVBoxLayout(self._tags_container_widget)
        self.tags_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.tags_scroll_area.setWidget(self._tags_container_widget)

        self.context_input = QTextEdit(placeholderText="Use case or situation related to this notion")
        self.context_input.setMaximumHeight(200)
        self.description_input = QTextEdit(placeholderText="If acquired only : anything you have learned about this notion")
        self.description_input.setMaximumHeight(200)
        self.save_button = CustomToolButton("Create Notion")

        self._form_layout.addRow("Title :", self.title_input)
        self._form_layout.addRow("", self.form_title_error)
        self._form_layout.addRow("Category :", self.category_input)
        self._form_layout.addRow("", self.form_category_error)
        self._form_layout.addRow("Tags :", self.tags_scroll_area)
        self._form_layout.addRow("Context :", self.context_input)
        self._form_layout.addRow("Description :", self.description_input)
        self._form_layout.addRow("", self.save_button)

        self._form_container_layout.addWidget(self._form_widget)
        self._form_container_layout.addStretch()

        self._form_container_layout.setStretch(0, 1)
        self._form_container_layout.setStretch(1, 3)
        self._form_container_layout.setStretch(2, 1)

        self._main_v_layout.addWidget(self._form_container)
        self._main_v_layout.addStretch()
