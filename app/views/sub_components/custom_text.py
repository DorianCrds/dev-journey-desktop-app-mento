from PySide6.QtWidgets import QLabel


class CustomViewTitleLabel(QLabel):
    def __init__(self, text: str):
        super().__init__(text)
        self.setObjectName("view_title_label")

        self.setStyleSheet("""
            #view_title_label {
                font-size: 14pt;
            }
        """)