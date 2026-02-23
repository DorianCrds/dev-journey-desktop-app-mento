# app/presenters/notion_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from app.domain.models.notion import Notion
from app.services.category_service import CategoryService
from app.services.notion_service import NotionService
from app.views.notions.notions_card import NotionCard
from app.views.notions.notions_view import NotionsView


class NotionPresenter:
    def __init__(self, view: NotionsView, notion_service: NotionService, categories_service: CategoryService):
        self._view = view
        self._notions_service = notion_service
        self._categories_service = categories_service

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._view.list_widget.itemSelectionChanged.connect(self._on_selection_changed)

        self._view.add_button.clicked.connect(self._on_add_button_clicked)
        self._view.form_page.back_button.clicked.connect(self._on_back_button_clicked)
        self._view.form_page.save_button.clicked.connect(self._on_form_button_clicked)

        self._view.form_page.title_input.textChanged.connect(self._validate_form)
        self._view.form_page.category_input.currentIndexChanged.connect(self._validate_form)

    def load_notions(self) -> None:
        self._view.list_widget.clear()
        notions = self._notions_service.get_all_notions()

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

    def _on_add_button_clicked(self) -> None:
        self._populate_form_combobox()
        self._view.content.setCurrentIndex(1)

    def _populate_form_combobox(self):
        categories = self._categories_service.get_all_categories()

        combo = self._view.form_page.category_input
        combo.clear()

        combo.addItem("Select a category...", None)

        for category in categories:
            combo.addItem(category.title, category)

        self._view.form_page.save_button.setEnabled(False)

    def _validate_form(self):
        form = self._view.form_page

        title_valid = bool(form.title_input.text().strip())
        category_valid = form.category_input.currentData() is not None

        form.save_button.setEnabled(title_valid and category_valid)

    def _on_back_button_clicked(self) -> None:
        self._reset_form()
        self._view.content.setCurrentIndex(0)

    def _on_form_button_clicked(self):
        title = self._view.form_page.title_input.text().strip()
        category = self._view.form_page.category_input.currentData()
        context = self._view.form_page.context_input.toPlainText().strip()
        description = self._view.form_page.description_input.toPlainText().strip()

        self._view.form_page.form_title_error.hide()

        has_error = False

        if not title:
            self._view.form_page.form_title_error.setText("Title is required.")
            self._view.form_page.form_title_error.show()
            has_error = True

        if category is None:
            self._view.form_page.form_category_error.setText("Select an existing category.")
            self._view.form_page.form_category_error.show()
            has_error = True

        if has_error:
            return

        self._notions_service.create_notion(title, category.id, context, description)

        self._reset_form()

        self.load_notions()

        self._on_back_button_clicked()

    def _reset_form(self):
        form = self._view.form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()

        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()

        form.save_button.setEnabled(False)
