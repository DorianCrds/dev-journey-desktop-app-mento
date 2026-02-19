from PySide6.QtCore import Qt
from PySide6.QtWidgets import QToolButton, QSizePolicy


class CustomMenuToolButton(QToolButton):
    def __init__(self):
        super().__init__()
        self.setObjectName("custom_menu_tool_button")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setAutoRaise(True)
        self.setStyleSheet("""
            #custom_menu_tool_button {
                padding: 5px;
            }
        """)

class CustomToolButton(QToolButton):
    def __init__(self, text: str):
        super().__init__()
        self.setObjectName("custom_tool_button")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.setMinimumWidth(100)
        self.setText(text)

        self.setStyleSheet("""
            #custom_tool_button {
                padding: 5px;
            }
        """)