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