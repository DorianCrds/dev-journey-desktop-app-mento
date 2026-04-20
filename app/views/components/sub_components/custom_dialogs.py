# qute/widgets/mento_dialog.py

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QWidget
)
from PySide6.QtCore import Qt


class CustomDialog(QDialog):
    def __init__(self, title: str, message: str, parent=None):
        super().__init__(parent)

        self.setObjectName("Dialog")
        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumWidth(360)

        self._result = None

        self._setup_ui(title, message)

    def _setup_ui(self, title, message):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(24, 20, 24, 20)
        self.layout.setSpacing(16)

        # ---- Title
        self.title_label = QLabel(title)
        self.title_label.setObjectName("DialogTitle")
        self.title_label.setAlignment(Qt.AlignLeft)

        # ---- Message
        self.message_label = QLabel(message)
        self.message_label.setObjectName("DialogMessage")
        self.message_label.setWordWrap(True)

        # ---- Buttons container
        self.buttons_container = QWidget()
        self.buttons_container.setObjectName("DialogButtonsContainer")
        self.buttons_layout = QHBoxLayout(self.buttons_container)
        self.buttons_layout.setSpacing(12)
        self.buttons_layout.addStretch()

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.buttons_container)

    # ---------------------
    # BUTTONS API
    # ---------------------

    def add_button(self, text: str, role: str):
        button = QPushButton(text)
        button.setObjectName(f"DialogButton_{role}")

        if role == "accept":
            button.clicked.connect(self._accept)
        elif role == "reject":
            button.clicked.connect(self._reject)
        else:
            button.clicked.connect(self.close)

        self.buttons_layout.addWidget(button)

        return button

    def set_buttons(self, buttons: list[tuple[str, str]]):
        """
        buttons = [("Cancel", "reject"), ("Delete", "accept")]
        """
        for text, role in buttons:
            self.add_button(text, role)

    # ---------------------
    # RESULTS
    # ---------------------

    def _accept(self):
        self._result = True
        self.accept()

    def _reject(self):
        self._result = False
        self.reject()

    def get_result(self):
        return self._result

    # ---------------------
    # STATIC HELPERS
    # ---------------------

    @staticmethod
    def confirm(parent, title, message) -> bool:
        dialog = CustomDialog(title, message, parent)
        dialog.set_buttons([
            ("Cancel", "reject"),
            ("Confirm", "accept"),
        ])
        dialog.exec()
        return dialog.get_result()

    @staticmethod
    def error(parent, title, message):
        dialog = CustomDialog(title, message, parent)
        dialog.set_buttons([
            ("OK", "accept"),
        ])
        dialog.exec()

    @staticmethod
    def info(parent, title, message):
        dialog = CustomDialog(title, message, parent)
        dialog.set_buttons([
            ("OK", "accept"),
        ])
        dialog.exec()