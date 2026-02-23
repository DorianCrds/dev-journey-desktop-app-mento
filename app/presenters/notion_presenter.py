# app/presenters/notion_presenter.py
from PySide6.QtCore import QItemSelectionModel, Qt
from PySide6.QtWidgets import QListWidgetItem

from app.domain.models.notion import Notion
from app.services.notion_service import NotionService
from app.views.notions.notions_card import NotionCard
from app.views.notions.notions_view import NotionsView


class NotionPresenter:
    def __init__(self, view: NotionsView, notion_service: NotionService):
        self._view = view
        self._service = notion_service

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._view.list_widget.itemSelectionChanged.connect(self._on_selection_changed)

        self._view.add_button.clicked.connect(self._add_button_clicked)
        self._view.form_page.back_button.clicked.connect(self._back_button_clicked)

    def load_notions(self) -> None:
        self._view.list_widget.clear()
        notions = self._service.get_all_notions()

        for notion in notions:
            self._add_card(notion)

        if self._view.list_widget.count() > 0:
            self._view.list_widget.setFocus()
            self._view.list_widget.setCurrentRow(0)

        self._view.edit_button.setEnabled(False)
        self._view.delete_button.setEnabled(False)

    def _add_card(self, notion: Notion):
        item = QListWidgetItem()

        item.setData(Qt.ItemDataRole.UserRole, notion)

        card = NotionCard(notion)

        item.setSizeHint(card.sizeHint())

        self._view.list_widget.addItem(item)
        self._view.list_widget.setItemWidget(item, card)

    def _on_selection_changed(self):
        selected_items = self._view.list_widget.selectedItems()

        if not selected_items:
            return

        self._view.delete_button.setEnabled(bool(selected_items))
        self._view.edit_button.setEnabled(bool(selected_items))

        item = selected_items[0]

        notion = item.data(Qt.ItemDataRole.UserRole)

        self._view.detail_title_value.setText(notion.title)
        self._view.detail_category_value.setText(str(notion.category_id))
        self._view.detail_context_value.setText(notion.context)
        self._view.detail_description_value.setText(notion.description)
        self._view.detail_status_value.setText(notion.status)

    def _add_button_clicked(self) -> None:
        self._view.content.setCurrentIndex(1)

    def _back_button_clicked(self) -> None:
        self._view.content.setCurrentIndex(0)
