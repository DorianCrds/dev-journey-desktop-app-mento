# app/views/components/sub_components/custom_headers.py
from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_forms import CustomSearchLineEdit, CustomFilterComboBox
from qute.design_system.spacing import Spacing


class CustomPageHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(Spacing.MD, 0, Spacing.MD, 0)
        self.layout.setSpacing(Spacing.SM)
        self.setMinimumHeight(50)

        self.add_button = CustomToolButton("Add")
        self.edit_button = CustomToolButton("Edit")
        self.delete_button = CustomToolButton("Delete")

        self.add_button.hide()
        self.edit_button.hide()
        self.delete_button.hide()


class PageActionsHeader(CustomPageHeader):
    def __init__(self):
        super().__init__()

        self.category_filter = CustomFilterComboBox()
        self.category_filter.setFixedWidth(180)
        self.category_filter.hide()

        self.search_input = CustomSearchLineEdit()
        self.search_input.setFixedWidth(300)
        self.search_input.hide()

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addStretch()
        self.layout.addWidget(self.search_input)
        self.layout.addSpacing(Spacing.MD)
        self.layout.addWidget(self.category_filter)


class PageNavHeader(CustomPageHeader):
    def __init__(self):
        super().__init__()

        self.back_button = CustomToolButton("Back")

        self.layout.addWidget(self.back_button)
        self.layout.addStretch()
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)