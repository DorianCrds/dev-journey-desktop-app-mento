from PySide6.QtWidgets import QLabel, QSizePolicy


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