from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.ui.views.components.sub_components.custom_buttons import CustomToolButton


class PageActionsHeader(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(8)

        self.add_button = CustomToolButton("Add")
        self.edit_button = CustomToolButton("Edit")
        self.delete_button = CustomToolButton("Delete")

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addStretch()

        self.add_button.hide()
        self.edit_button.hide()
        self.delete_button.hide()