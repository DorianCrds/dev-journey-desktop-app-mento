# app/ui/views/components/sub_components/custom_texts.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy

from app.ui.theme.typography import Typography


class CustomTitleMain(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("TitleMain")

class CustomTitleNotion(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("TitleNotion")

class CustomStatusToLearn(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("StatusToLearn")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class CustomStatusAcquired(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("StatusAcquired")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class CustomMetaInfo(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("MetaInfo")
        self.setFont(Typography.get_font(Typography.META, Typography.MEDIUM))
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

class CustomTextNormal(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("TextNormal")

class CustomTagLabel(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("TagLabel")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)



class CustomViewTitleLabel(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("view_title_label")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.setStyleSheet("""
            #view_title_label {
                font-size: 14pt;
                border: 1px solid green;
            }
        """)

class CustomPrimaryContentLabel(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("primary_content_label")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.setStyleSheet("""
            #primary_content_label {
                font-size: 12pt;
                font-weight: bold;
            }
        """)

class CustomFormErrorLabel(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("form_error_label")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.setStyleSheet("""
            #form_error_label {
                color: #e5484d;
                font-size: 9pt;
                padding-left: 4px;
            }
        """)