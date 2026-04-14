# app/ui/views/components/sub_components/custom_texts.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy
from qute.design_system.typography import Typography


class CustomTitleMain(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("TitleMain")

class CustomDocumentTitle(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("DocumentTitle")
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

class CustomPrimaryPill(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("PrimaryPill")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class CustomMetaInfo(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("MetaInfo")
        self.setFont(Typography.from_preset("meta_md"))
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

class CustomFormErrorLabel(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("FormError")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
