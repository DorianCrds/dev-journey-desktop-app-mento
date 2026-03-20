# app/ui/views/pages/tags/tags_card.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QLineEdit

from app.services.dto.tag_dto import TagDTO
from app.ui.views.components.sub_components.custom_buttons import CustomToolButton, CustomIconSmallToolButton
from app.ui.views.components.sub_components.custom_texts import CustomDocumentTitle


class TagCard(QWidget):
    def __init__(self, tag: TagDTO):
        super().__init__()
        self.setObjectName("CardTag")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumHeight(50)

        self.tag = tag

        self._main_h_layout = QHBoxLayout(self)

        self.title_label = CustomDocumentTitle(self.tag.title)

        self.title_input = QLineEdit(self.tag.title)
        self.title_input.hide()

        self._main_h_layout.addWidget(self.title_label)
        self._main_h_layout.addWidget(self.title_input)
        self._main_h_layout.addStretch()

        self.edit_button = CustomIconSmallToolButton("assets/icons/pencil.svg")
        self.delete_button = CustomIconSmallToolButton("assets/icons/trash.svg")

        self._main_h_layout.addWidget(self.edit_button)
        self._main_h_layout.addWidget(self.delete_button)

        self.edit_button.hide()
        self.delete_button.hide()

    def set_edit_mode(self, enabled: bool):
        self.title_label.setVisible(not enabled)
        self.title_input.setVisible(enabled)

        if enabled:
            self.title_input.setFocus()
            self.title_input.selectAll()

    def enterEvent(self, event):
        if not self.title_input.isVisible():
            self.edit_button.show()
            self.delete_button.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if not self.title_input.isVisible():
            self.edit_button.hide()
            self.delete_button.hide()
        super().leaveEvent(event)

class TagInputCard(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("CardTagInput")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QHBoxLayout(self)

        self.input = QLineEdit()
        self.input.setPlaceholderText("New tag...")

        self.save_button = CustomIconSmallToolButton("assets/icons/check.svg")
        self.cancel_button = CustomIconSmallToolButton("assets/icons/x.svg")

        layout.addWidget(self.input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)
        layout.addStretch()