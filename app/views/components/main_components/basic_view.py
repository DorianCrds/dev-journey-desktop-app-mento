# app/views/components/main_components/basic_view.py

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy

from app.views.components.sub_components.custom_texts import CustomTitleMain
from qute.design_system.spacing import Spacing


class BasicView(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._title_text = title

        self._setup_base_ui()

    def _setup_base_ui(self) -> None:
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(Spacing.LG)

        self.title_label = CustomTitleMain(self._title_text)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(Spacing.MD)

        self._main_layout.addWidget(self.title_label)
        self._main_layout.addWidget(self.content_widget)
