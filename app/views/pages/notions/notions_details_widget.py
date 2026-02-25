# app/views/pages/notions/notions_details_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit

from app.views.components.sub_components.custom_texts import CustomPrimaryContentLabel


class NotionsDetailsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self) -> None:
        self._main_v_layout = QVBoxLayout(self)

        self._title_label = CustomPrimaryContentLabel("Title")
        self.title_value = QLabel("")

        self._category_label = CustomPrimaryContentLabel("Category")
        self.category_value = QLabel("")

        self._context_label = CustomPrimaryContentLabel("Context")
        self.context_value = QTextEdit("")
        self.context_value.setReadOnly(True)

        self._description_label = CustomPrimaryContentLabel("Description")
        self.description_value = QTextEdit("")
        self.description_value.setReadOnly(True)

        self._status_label = CustomPrimaryContentLabel("Status")
        self.status_value = QLabel("")

        self._main_v_layout.addWidget(self._title_label)
        self._main_v_layout.addWidget(self.title_value)
        self._main_v_layout.addWidget(self._category_label)
        self._main_v_layout.addWidget(self.category_value)
        self._main_v_layout.addWidget(self._context_label)
        self._main_v_layout.addWidget(self.context_value)
        self._main_v_layout.addWidget(self._description_label)
        self._main_v_layout.addWidget(self.description_value)
        self._main_v_layout.addWidget(self._status_label)
        self._main_v_layout.addWidget(self.status_value)
        self._main_v_layout.addStretch()
