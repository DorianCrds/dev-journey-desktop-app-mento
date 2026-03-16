# app/ui/views/pages/notions/notion_card.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from app.services.dto.notion_dto import NotionReadDTO
from app.ui.views.components.sub_components.custom_texts import CustomDocumentTitle, CustomStatusToLearn, \
    CustomStatusAcquired, CustomMetaInfo


class NotionCard(QWidget):
    def __init__(self, notion: NotionReadDTO):
        super().__init__()
        self.setObjectName("CardNotion")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.notion = notion

        main_v_layout = QVBoxLayout(self)
        self.title_label = CustomDocumentTitle(self.notion.title)

        if self.notion.status == "À apprendre":
            self.status_label = CustomStatusToLearn(self.notion.status)
        elif self.notion.status == "Acquise":
            self.status_label = CustomStatusAcquired(self.notion.status)

        first_line_layout = QHBoxLayout()
        first_line_layout.addWidget(self.title_label)
        first_line_layout.addStretch()
        first_line_layout.addWidget(self.status_label)

        self.category_label = CustomMetaInfo(self.notion.category_title)

        second_line_layout = QHBoxLayout()
        second_line_layout.addWidget(self.category_label)
        second_line_layout.addStretch()

        main_v_layout.addLayout(first_line_layout)
        main_v_layout.addLayout(second_line_layout)
