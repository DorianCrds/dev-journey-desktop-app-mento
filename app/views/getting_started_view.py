# app/views/getting_started_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.views.components.main_components.basic_view import BasicView
from app.views.components.sub_components.custom_cards_scroll_area import CustomCardsScrollArea
from app.views.components.sub_components.custom_texts import (
    CustomDocumentTitle,
    CustomTextNormal,
)
from qute.design_system.spacing import Spacing


class GettingStartedView(BasicView):
    def __init__(self):
        super().__init__("Start here")

        self._setup_ui()

    def _setup_ui(self):
        scroll_area = CustomCardsScrollArea()

        intro_card = self._create_card(
            "What is Mento?",
            [
                "Mento helps you keep track of what you learn over time.",
                "Structure your knowledge using notions, categories, and tags.",
            ],
        )

        steps_card = self._create_card(
            "Getting started",
            [
                "1. Create a category (e.g. Python, Databases)",
                "2. Add a notion and assign it to a category",
                "3. Use tags to add extra context (e.g. async, API)",
            ],
        )

        concepts_card = self._create_card(
            "Core concepts",
            [
                "Category — Groups your notions and acts as your main filter",
                "Tag — Adds context and helps refine your organization",
                "Notion — Represents a piece of knowledge you want to track",
            ],
        )

        example_card = self._create_card(
            "Example",
            [
                "Category: Python",
                "Notion: Decorators",
                "Tags: advanced, functions",
            ],
        )

        scroll_area.cards_layout.insertWidget(0, intro_card)
        scroll_area.cards_layout.insertWidget(1, steps_card)
        scroll_area.cards_layout.insertWidget(2, concepts_card)
        scroll_area.cards_layout.insertWidget(3, example_card)

        self.content_layout.addWidget(scroll_area)

    def _create_card(self, title: str, lines: list[str]) -> QWidget:
        card = QWidget()
        card.setObjectName("CardGettingStarted")

        layout = QVBoxLayout(card)
        layout.setSpacing(Spacing.SM)
        layout.setContentsMargins(
            Spacing.MD, Spacing.MD, Spacing.MD, Spacing.MD
        )

        title_label = CustomDocumentTitle(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(title_label)

        for line in lines:
            text = CustomTextNormal(line)
            layout.addWidget(text)

        return card