# app/presenters/notion_presenter.py
from PySide6.QtCore import QItemSelectionModel

from app.domain.models.notion import Notion
from app.services.notion_service import NotionService
from app.views.notions.notions_table_model import NotionsTableModel
from app.views.notions.notions_view import NotionsView


class NotionPresenter:
    def __init__(self, view: NotionsView, notion_service: NotionService):
        self._view = view
        self._service = notion_service

        self._table_model = NotionsTableModel()
        self._view.list_page.table_view.setModel(self._table_model)

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._view.list_page.add_button.clicked.connect(self._add_button_clicked)
        self._view.form_page.back_button.clicked.connect(self._back_button_clicked)

        selection_model = self._view.list_page.table_view.selectionModel()
        selection_model.selectionChanged.connect(self._on_selection_changed)

    def load_notions(self) -> None:
        notions = self._service.get_all_notions()
        self._table_model.set_notions(notions)

        if not notions:
            return

        table = self._view.list_page.table_view
        index = self._table_model.index(0, 0)

        table.selectionModel().select(index, QItemSelectionModel.SelectionFlag.Select)

        table.setCurrentIndex(index)
        table.setFocus()
        table.scrollTo(index)

    def _add_button_clicked(self) -> None:
        self._view.content.setCurrentIndex(1)

    def _back_button_clicked(self) -> None:
        self._view.content.setCurrentIndex(0)

    def _on_selection_changed(self, selected, deselected):
        indexes = selected.indexes()
        if not indexes:
            return

        row = indexes[0].row()
        notion = self._table_model.get_notion_at(row)

        if notion:
            self._display_notion_detail(notion)

    def _display_notion_detail(self, notion: Notion):
        self._view.list_page.title_input.setText(notion.title)
        self._view.list_page.category_input.setText(str(notion.category_id))
        self._view.list_page.status_input.setText(notion.status)
        self._view.list_page.context_input.setText(notion.context)
        self._view.list_page.description_input.setText(notion.description)
