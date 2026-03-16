# app/ui/views/pages/categories/categories_card.py
from PySide6.QtCore import Qt, Signal, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QSizePolicy

from app.services.dto.category_dto import CategoryReadDTO
from app.ui.views.components.sub_components.arrow_indicator import ArrowIndicator
from app.ui.views.components.sub_components.custom_texts import CustomDocumentTitle, CustomMetaInfo


class CategoryCard(QWidget):

    clicked = Signal(object)

    def __init__(self, category: CategoryReadDTO):
        super().__init__()
        self.setObjectName("CardCategory")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)

        self.category = category
        self.expanded = False

        main_h_layout = QVBoxLayout(self)

        self.first_line_layout = QHBoxLayout()

        self.title_label = CustomDocumentTitle(self.category.title)
        self.first_line_layout.addWidget(self.title_label)
        self.first_line_layout.addStretch()

        self.arrow_icon = ArrowIndicator()
        self.first_line_layout.addWidget(self.arrow_icon)

        self.description_value = CustomMetaInfo(self.category.description)
        self.description_value.setWordWrap(True)
        self.description_value.hide()

        main_h_layout.addLayout(self.first_line_layout)
        main_h_layout.addWidget(self.description_value)

    def set_selected(self, selected: bool):
        if self.expanded == selected:
            return

        self.expanded = selected

        self.description_value.setVisible(selected)

        self.arrow_icon.rotate(selected)

        self.setProperty("selected", selected)
        self.style().polish(self)

        self.updateGeometry()

    def mousePressEvent(self, event):
        self.clicked.emit(self)
