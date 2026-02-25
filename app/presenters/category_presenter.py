# app/presenters/category_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QMessageBox

from app.domain.models.category import Category
from app.services.category_service import CategoryService
from app.views.pages.categories.categories_card import CategoryCard
from app.views.pages.categories.categories_view import CategoriesView


class CategoryPresenter:
    def __init__(self, view: CategoriesView, category_service: CategoryService):
        self._view = view
        self._service = category_service

        self._editing_category: Category | None = None

        self._connect_signals()
        self.load_categories()

    def _connect_signals(self) -> None:
        self._view.list_widget.itemSelectionChanged.connect(self._on_selection_changed)
        self._view.form_button.clicked.connect(self._on_form_button_clicked)

        self._view.form_title_input.textChanged.connect(lambda: self._view.form_title_error.hide())
        self._view.form_description_input.textChanged.connect(lambda: self._view.form_description_error.hide())

        self._view.edit_button.clicked.connect(self._on_edit_button_clicked)
        self._view.delete_button.clicked.connect(self._on_delete_button_clicked)

    def load_categories(self) -> None:
        self._view.list_widget.clear()
        categories = self._service.get_all_categories()

        for category in categories:
            self._add_card(category)

        if self._view.list_widget.count() > 0:
            self._view.list_widget.setFocus()
            self._view.list_widget.setCurrentRow(0)

        self._view.delete_button.setEnabled(False)
        self._view.edit_button.setEnabled(False)

    def _add_card(self, category: Category) -> None:
        item = QListWidgetItem()

        item.setData(Qt.ItemDataRole.UserRole, category)

        card = CategoryCard(category)

        item.setSizeHint(card.sizeHint())

        self._view.list_widget.addItem(item)
        self._view.list_widget.setItemWidget(item, card)

    def _on_selection_changed(self) -> None:
        selected_items = self._view.list_widget.selectedItems()

        if not selected_items:
            return

        self._view.delete_button.setEnabled(bool(selected_items))
        self._view.edit_button.setEnabled(bool(selected_items))

        item = selected_items[0]

        category = item.data(Qt.ItemDataRole.UserRole)

        self._view.detail_title_value.setText(category.title)
        self._view.detail_description_value.setText(category.description)

    def _on_form_button_clicked(self) -> None:
        title = self._view.form_title_input.text().strip()
        description = self._view.form_description_input.toPlainText().strip()

        self._view.form_title_error.hide()
        self._view.form_description_error.hide()

        has_error = False

        if not title:
            self._view.form_title_error.setText("Title is required.")
            self._view.form_title_error.show()
            has_error = True

        if not description:
            self._view.form_description_error.setText("Description is required.")
            self._view.form_description_error.show()
            has_error = True

        if has_error:
            return

        if self._editing_category is None:
            self._service.create_category(title, description)
        else:
            self._editing_category._title = title
            self._editing_category._description = description
            self._service.update_category(self._editing_category)

        self._reset_form()

        self.load_categories()

    def _on_edit_button_clicked(self) -> None:
        selected_item = self._view.list_widget.currentItem()

        if not selected_item:
            return

        category = selected_item.data(Qt.ItemDataRole.UserRole)

        self._editing_category = category

        self._view.form_title_input.setText(category.title)
        self._view.form_description_input.setText(category.description)

        self._view.form_button.setText("Update category")

    def _reset_form(self) -> None:
        self._editing_category = None
        self._view.form_title_input.clear()
        self._view.form_description_input.clear()
        self._view.form_button.setText("Save category")

    def _on_delete_button_clicked(self) -> None:
        selected_item = self._view.list_widget.currentItem()

        if not selected_item:
            return

        category = selected_item.data(Qt.ItemDataRole.UserRole)

        reply = QMessageBox.question(self._view,"Delete category", f"Are you sure you want to delete the category:\n\n'{category.title}' ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self._service.delete_category(category.id)

            if self._editing_category and self._editing_category.id == category.id:
                self._reset_form()

            self.load_categories()