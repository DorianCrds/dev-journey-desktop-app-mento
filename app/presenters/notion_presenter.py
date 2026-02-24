# app/presenters/notion_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from enum import Enum, auto

from app.domain.models.notion import Notion
from app.services.category_service import CategoryService
from app.services.notion_service import NotionService
from app.views.notions.notions_card import NotionCard
from app.views.notions.notions_view import NotionsView


class FormMode(Enum):
    CREATE = auto()
    EDIT = auto()


class NotionPresenter:
    def __init__(self, view: NotionsView, notion_service: NotionService, categories_service: CategoryService):
        self._view = view
        self._notions_service = notion_service
        self._categories_service = categories_service

        self._form_mode = FormMode.CREATE
        self._editing_notion: Notion | None = None

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._view.list_widget.itemSelectionChanged.connect(self._on_selection_changed)

        self._view.add_button.clicked.connect(self._on_add_button_clicked)
        self._view.edit_button.clicked.connect(self._on_edit_button_clicked)
        self._view.form_page.back_button.clicked.connect(self._on_back_button_clicked)
        self._view.form_page.save_button.clicked.connect(self._on_form_button_clicked)

        self._view.form_page.title_input.textChanged.connect(self._validate_form)
        self._view.form_page.category_input.currentIndexChanged.connect(self._validate_form)

    #########################################
    ##### Notions list widget's methods #####
    #########################################

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

    ###############################
    ##### Buttons connections #####
    ###############################

    def _on_add_button_clicked(self):
        self._open_form(FormMode.CREATE)

    def _on_edit_button_clicked(self):
        selected_item = self._view.list_widget.currentItem()
        if not selected_item:
            return

        notion = selected_item.data(Qt.ItemDataRole.UserRole)
        self._open_form(FormMode.EDIT, notion)

    def _on_back_button_clicked(self) -> None:
        self._reset_form()
        self._view.content.setCurrentIndex(0)

    def _on_form_button_clicked(self):
        form = self._view.form_page

        title = form.title_input.text().strip()
        category = form.category_input.currentData()
        context = form.context_input.toPlainText().strip()
        description = form.description_input.toPlainText().strip()

        if not self._validate_and_show_errors(title, category):
            return

        if self._form_mode == FormMode.CREATE:
            self._notions_service.create_notion(
                title,
                category.id,
                context,
                description
            )

        elif self._form_mode == FormMode.EDIT and self._editing_notion:
            self._editing_notion.update_title(title)
            self._editing_notion.update_category(category.id)
            self._editing_notion.update_context(context)
            self._editing_notion.update_description(description)

            self._notions_service.update_notion(self._editing_notion)

        self._after_submit()

    #################################
    ##### Reusable Form methods #####
    #################################

    def _open_form(self, mode: FormMode, notion: Notion | None = None):
        self._form_mode = mode
        self._editing_notion = notion

        self._populate_form_combobox()

        form = self._view.form_page

        if mode == FormMode.CREATE:
            form.save_button.setText("Create Notion")
            self._reset_form_fields()

        elif mode == FormMode.EDIT and notion:
            form.save_button.setText("Update Notion")
            self._fill_form_with_notion(notion)

        self._validate_form()
        self._view.content.setCurrentIndex(1)

    def _populate_form_combobox(self):
        categories = self._categories_service.get_all_categories()

        combo = self._view.form_page.category_input
        combo.clear()

        combo.addItem("Select a category...", None)

        for category in categories:
            combo.addItem(category.title, category)

        self._view.form_page.save_button.setEnabled(False)

    def _fill_form_with_notion(self, notion: Notion):
        form = self._view.form_page

        form.title_input.setText(notion.title)
        form.context_input.setText(notion.context or "")
        form.description_input.setText(notion.description or "")

        combo = form.category_input
        for i in range(combo.count()):
            category = combo.itemData(i)
            if category and category.id == notion.category_id:
                combo.setCurrentIndex(i)
                break

    def _validate_form(self):
        form = self._view.form_page

        title_valid = bool(form.title_input.text().strip())
        category_valid = form.category_input.currentData() is not None

        form.save_button.setEnabled(title_valid and category_valid)

    def _validate_and_show_errors(self, title, category) -> bool:
        form = self._view.form_page

        form.form_title_error.hide()
        form.form_category_error.hide()

        valid = True

        if not title:
            form.form_title_error.setText("Title is required.")
            form.form_title_error.show()
            valid = False

        if category is None:
            form.form_category_error.setText("Select an existing category.")
            form.form_category_error.show()
            valid = False

        return valid

    def _reset_form(self):
        form = self._view.form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()

        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()

        form.save_button.setEnabled(False)

    def _after_submit(self):
        self._form_mode = FormMode.CREATE
        self._editing_notion = None

        self._reset_form_fields()
        self.load_notions()
        self._view.content.setCurrentIndex(0)

    def _reset_form_fields(self):
        form = self._view.form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()
        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()
