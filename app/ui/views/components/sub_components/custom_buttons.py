# app/ui/views/components/sub_components/custom_buttons.py
from PySide6.QtWidgets import QToolButton, QSizePolicy
from PySide6.QtCore import Qt


class CustomMenuToolButton(QToolButton):
    def __init__(self, text: str):
        super().__init__()

        self.setObjectName("SidebarItem")
        self.setText(text)

        self.setCheckable(True)
        self.setAutoExclusive(True)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setMinimumHeight(36)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

class CustomToolButton(QToolButton):
    def __init__(self, text: str):
        super().__init__()
        self.setObjectName("custom_tool_button")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.setMinimumWidth(100)
        self.setText(text)
