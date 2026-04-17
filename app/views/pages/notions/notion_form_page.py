# app/ui/views/pages/notions/notion_form_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QCheckBox, QSizePolicy

from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_forms import CustomFormLineEdit, CustomFormComboBox, \
    CustomFormTextEdit, CustomFormScrollArea
from app.views.components.sub_components.custom_headers import PageNavHeader
from app.views.components.sub_components.custom_texts import CustomFormErrorLabel
from qute.design_system.spacing import Spacing


class NotionFormPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.tag_checkboxes: list[QCheckBox] = []

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)
        self._main_v_layout.setSpacing(Spacing.LG)
        self._main_v_layout.setContentsMargins(0, 0, 0, 0)

        self.header_widget = PageNavHeader()
        self.header_widget.setObjectName("NotionFormHeader")

        self._main_v_layout.addWidget(self.header_widget)

        self._form_container = QWidget()
        self._form_container.setObjectName("notion_form_container")
        self._form_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._form_container_layout = QHBoxLayout(self._form_container)
        self._form_container_layout.setContentsMargins(0, 0, 0, 0)
        self._form_container_layout.setSpacing(0)

        self._form_container_layout.addStretch()

        self._form_widget = QWidget()
        self._form_widget.setObjectName("NotionFormWidget")
        self._form_widget.setMaximumWidth(640)

        self._form_layout = QFormLayout(self._form_widget)
        self._form_layout.setVerticalSpacing(Spacing.V_FORM)
        self._form_layout.setHorizontalSpacing(Spacing.MD)
        self._form_layout.setContentsMargins(Spacing.LG, Spacing.LG, Spacing.LG, Spacing.LG)
        self._form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self._form_layout.setFormAlignment(Qt.AlignmentFlag.AlignTop)

        self.title_input = CustomFormLineEdit()
        self.title_input.setPlaceholderText("Name of the notion")

        self.form_title_error = CustomFormErrorLabel("")
        self.form_title_error.hide()

        self.category_input = CustomFormComboBox()
        self.category_input.setPlaceholderText("Choose a category")
        self.category_input.setCurrentIndex(0)
        self.form_category_error = CustomFormErrorLabel("")
        self.form_category_error.hide()

        self.tags_scroll_area = CustomFormScrollArea()
        self.tags_scroll_area.setWidgetResizable(True)
        self.tags_scroll_area.setMaximumHeight(180)
        self.tags_scroll_area.setMinimumHeight(80)

        self._tags_container_widget = QWidget()
        self._tags_container_widget.setObjectName("TagsContainer")
        self.tags_layout = QVBoxLayout(self._tags_container_widget)
        self.tags_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.tags_scroll_area.setWidget(self._tags_container_widget)

        self.context_input = CustomFormTextEdit()
        self.context_input.setPlaceholderText("Use case or situation related to this notion")
        self.context_input.setMaximumHeight(200)
        self.description_input = CustomFormTextEdit()
        self.description_input.setPlaceholderText("If acquired only : anything you have learned about this notion")
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