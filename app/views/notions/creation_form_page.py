from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox, QLineEdit, QTextEdit

from app.views.sub_components.custom_buttons import CustomToolButton


class CreationFormPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("creation_form_page")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

    def _setup_ui(self):
        self._main_v_layout = QVBoxLayout(self)

        self._header_widget = QWidget()
        self._header_h_layout = QHBoxLayout(self._header_widget)

        self.back_button = CustomToolButton("< Back")
        self._header_h_layout.addWidget(self.back_button)

        self._header_h_layout.addStretch()

        self._main_v_layout.addWidget(self._header_widget)

        self._form_widget = QWidget()
        self._form_layout = QFormLayout(self._form_widget)

        self.title_input = QLineEdit()
        self.category_input = QComboBox()
        self.context_input = QTextEdit()
        self.description_input = QTextEdit()

        self._form_layout.addRow("Title :", self.title_input)
        self._form_layout.addRow("Category :", self.category_input)
        self._form_layout.addRow("Context :", self.context_input)
        self._form_layout.addRow("Description :", self.description_input)

        self._main_v_layout.addWidget(self._form_widget)

        self.save_button = CustomToolButton("Create Notion")

        self._main_v_layout.addWidget(self.save_button)

