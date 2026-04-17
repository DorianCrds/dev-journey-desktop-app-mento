# app/views/components/sub_components/custom_forms.py
from PySide6.QtWidgets import QLineEdit, QComboBox, QTextEdit, QScrollArea, QCheckBox

from qute.design_system.spacing import Spacing


class CustomFormLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setObjectName("FormLineEdit")

class CustomFormComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setObjectName("FormComboBox")

class CustomFormTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setObjectName("FormTextEdit")

class CustomFormScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setObjectName("FormScrollArea")

class CustomFormCheckBox(QCheckBox):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("FormCheckBox")
