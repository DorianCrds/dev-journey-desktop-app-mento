from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.ui.views.components.sub_components.custom_buttons import CustomToolButton

class CustomPageHeader(QWidget):
    def __init__(self, create_mode: bool = False, edit_mode: bool = False, delete_mode: bool = False):
        super().__init__()
        self._create_mode = create_mode
        self._edit_mode = edit_mode
        self._delete_mode = delete_mode

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(16, 0, 16, 0)
        self.layout.setSpacing(8)

        self.add_button = CustomToolButton("Add")
        self.edit_button = CustomToolButton("Edit")
        self.delete_button = CustomToolButton("Delete")

        if not self._create_mode:
            self.add_button.hide()

        if not self._edit_mode:
            self.edit_button.hide()

        if not self._delete_mode:
            self.delete_button.hide()


class PageActionsHeader(CustomPageHeader):
    def __init__(self, create_mode: bool = False, edit_mode: bool = False, delete_mode: bool = False):
        super().__init__(create_mode, edit_mode, delete_mode)

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addStretch()


class PageNavHeader(CustomPageHeader):
    def __init__(self, create_mode: bool = False, edit_mode: bool = False, delete_mode: bool = False):
        super().__init__(create_mode, edit_mode, delete_mode)

        self.back_button = CustomToolButton("Back")

        self.layout.addWidget(self.back_button)
        self.layout.addStretch()
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.edit_button)
        self.layout.addWidget(self.delete_button)