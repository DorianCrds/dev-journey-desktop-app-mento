# app/ui/views/components/sub_components/custom_buttons.py
from PySide6.QtWidgets import QToolButton, QSizePolicy, QPushButton
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

        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

class CustomToolButton(QToolButton):
    def __init__(self, text: str):
        super().__init__()
        self.setObjectName("primary")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setText(text)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

class CustomPushButton(QPushButton):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("primary")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)