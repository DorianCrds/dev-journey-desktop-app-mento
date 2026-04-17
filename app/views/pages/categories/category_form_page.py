# app/views/pages/categories/category_form_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QFormLayout

from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_forms import CustomFormLineEdit, CustomFormTextEdit
from app.views.components.sub_components.custom_texts import CustomFormErrorLabel
from qute.design_system.spacing import Spacing


class CategoryFormPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)

        self._header_widget = QWidget()
        self._header_widget.setObjectName("CategoryFormHeader")
        self._header_h_layout = QHBoxLayout(self._header_widget)

        self.back_button = CustomToolButton("Back")
        self._header_h_layout.addWidget(self.back_button)
        self._header_h_layout.addStretch()

        self._main_v_layout.addWidget(self._header_widget)

        self._form_container = QWidget()
        self._form_container.setObjectName("category_form_container")
        self._form_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._form_container_layout = QHBoxLayout(self._form_container)

        self._form_container_layout.addStretch()

        self._form_widget = QWidget()
        self._form_widget.setObjectName("CategoryFormWidget")
        self._form_widget.setMaximumWidth(640)

        self._form_layout = QFormLayout(self._form_widget)
        self._form_layout.setVerticalSpacing(Spacing.V_FORM)
        self._form_layout.setHorizontalSpacing(Spacing.MD)
        self._form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self._form_layout.setFormAlignment(Qt.AlignmentFlag.AlignTop)

        self.title_input = CustomFormLineEdit()
        self.title_input.setPlaceholderText("Name of the category")

        self.form_title_error = CustomFormErrorLabel("")
        self.form_title_error.hide()

        self.description_input = CustomFormTextEdit()
        self.description_input.setPlaceholderText("The most explicit description of what kind of notions this category wraps")
        self.description_input.setMaximumHeight(200)

        self.form_description_error = CustomFormErrorLabel("")
        self.form_description_error.hide()

        self.save_button = CustomToolButton("Create Category")

        self._form_layout.addRow("Title :", self.title_input)
        self._form_layout.addRow("", self.form_title_error)
        self._form_layout.addRow("Description :", self.description_input)
        self._form_layout.addRow("", self.form_description_error)
        self._form_layout.addRow("", self.save_button)

        self._form_container_layout.addWidget(self._form_widget)
        self._form_container_layout.addStretch()

        self._form_container_layout.setStretch(0, 1)
        self._form_container_layout.setStretch(1, 3)
        self._form_container_layout.setStretch(2, 1)

        self._main_v_layout.addWidget(self._form_container)
        self._main_v_layout.addStretch()