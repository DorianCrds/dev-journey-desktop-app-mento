# app/presenters/category_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem

from app.domain.models.category import Category
from app.services.category_service import CategoryService
from app.views.categories.categories_card import CategoryCard
from app.views.categories.categories_view import CategoriesView


class CategoryPresenter:
    def __init__(self, view: CategoriesView, category_service: CategoryService):
        self._view = view
        self._service = category_service

        self._connect_signals()
        self.load_categories()

    def _connect_signals(self) -> None:
        self._view.list_widget.itemSelectionChanged.connect(self._on_selection_changed)
        self._view.form_button.clicked.connect(self._on_form_button_clicked)

        self._view.form_title_input.textChanged.connect(lambda: self._view.form_title_error.hide())
        self._view.form_description_input.textChanged.connect(lambda: self._view.form_description_error.hide())

    def load_categories(self) -> None:
        self._view.list_widget.clear()
        categories = self._service.get_all_categories()

        for category in categories:
            self._add_card(category)

        if self._view.list_widget.count() > 0:
            self._view.list_widget.setFocus()
            self._view.list_widget.setCurrentRow(0)

    def _add_card(self, category: Category):
        item = QListWidgetItem()

        item.setData(Qt.ItemDataRole.UserRole, category)

        card = CategoryCard(category)

        item.setSizeHint(card.sizeHint())

        self._view.list_widget.addItem(item)
        self._view.list_widget.setItemWidget(item, card)

    def _on_selection_changed(self):
        selected_items = self._view.list_widget.selectedItems()

        if not selected_items:
            return

        item = selected_items[0]

        category = item.data(Qt.ItemDataRole.UserRole)

        self._view.detail_title_value.setText(category.title)
        self._view.detail_description_value.setText(category.description)

    def _on_form_button_clicked(self):
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

        self._service.create_category(title, description)

        self._view.form_title_input.clear()
        self._view.form_description_input.clear()

        self.load_categories()
