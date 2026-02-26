# app/views/pages/dashboard/stat_card.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel


class StatCard(QFrame):
    def __init__(self, title: str, value: str):
        super().__init__()
        self._title = title
        self._value = value

        self._setup_ui()

        self.setStyleSheet("""
            #stat_card {
                padding: 15px;
            }
            
            #stat_card_title_label {
                font-size: 14px;
            }
            
            #stat_card_value_label {
                font-size: 22px; 
                font-weight: bold;
            }
        """)

    def _setup_ui(self) -> None:
        self.setObjectName("stat_card")
        self.setFrameShape(QFrame.Shape.StyledPanel)

        layout = QVBoxLayout(self)

        title_label = QLabel(self._title)
        title_label.setObjectName("stat_card_title_label")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        value_label = QLabel(self._value)
        value_label.setObjectName("stat_card_value_label")
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)
        layout.addWidget(value_label)