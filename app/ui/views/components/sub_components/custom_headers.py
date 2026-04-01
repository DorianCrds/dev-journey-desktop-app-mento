from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.ui.views.components.sub_components.custom_buttons import CustomToolButton

class CustomPageHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(16, 0, 16, 0)
        self.layout.setSpacing(8)

        self.add_button = CustomToolButton("Add")
        self.edit_button = CustomToolButton("Edit")
        self.delete_button = CustomToolButton("Delete")

        self.add_button.hide()
        self.edit_button.hide()
        self.delete_button.hide()


class PageActionsHeader(CustomPageHeader):
    def __init__(self):
        super().__init__()

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addStretch()


class PageNavHeader(CustomPageHeader):
    def __init__(self):
        super().__init__()

        self.back_button = CustomToolButton("Back")

        self.layout.addWidget(self.back_button)
        self.layout.addStretch()
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)