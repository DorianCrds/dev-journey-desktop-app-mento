from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QFrame

from app.views.components.sub_components.custom_texts import CustomTitleMain, CustomDocumentTitle


class EmptyStateWidget(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName("EmptyStateWidget")
        self.setFrameShape(QFrame.Shape.StyledPanel)

        layout = QVBoxLayout(self)

        self.title_label = CustomDocumentTitle("")
        self.title_label.setObjectName("EmptyStateTitle")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitle_label = CustomTitleMain("")
        self.subtitle_label.setObjectName("EmptyStateSubtitle")
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)
