# app/presenters/category_presenter.py
from PySide6.QtWidgets import QMessageBox

from app.core.events import AppEvents
from app.presenters.form_mode_enum import FormMode
from app.services.category_service import CategoryService
from app.services.dto.category_dto import CategoryReadDTO
from app.ui.views.pages.categories.categories_card import CategoryCard
from app.ui.views.pages.categories.categories_view import CategoriesView


class CategoryPresenter:
    LIST_PAGE = 0
    FORM_PAGE = 1

    def __init__(self, view: CategoriesView, events: AppEvents, category_service: CategoryService):
        self._view = view
        self._events = events
        self._service = category_service

        self._form_mode = FormMode.CREATE
        self._editing_category: CategoryReadDTO | None = None

        self._connect_signals()
        self.load_categories()

    def _connect_signals(self) -> None:
        self._events.categories_changed.connect(self.load_categories)

        # List
        self._view.categories_list_page.header.add_button.clicked.connect(self._on_add_button_clicked)
        self._view.categories_list_page.header.edit_button.clicked.connect(self._on_edit_button_clicked)
        self._view.categories_list_page.header.delete_button.clicked.connect(self._on_delete_button_clicked)

        # Form
        self._view.category_form_page.back_button.clicked.connect(self._on_form_back_button_clicked)
        self._view.category_form_page.save_button.clicked.connect(self._on_form_button_clicked)

        self._view.category_form_page.title_input.textChanged.connect(self._validate_form)
        self._view.category_form_page.description_input.textChanged.connect(self._validate_form)

    def _emit_events(self):
        self._events.categories_changed.emit()
        self._events.notions_changed.emit()
        self._events.dashboard_changed.emit()

    ###############################
    ##### Buttons connections #####
    ###############################

    def _on_add_button_clicked(self):
        self._open_form(FormMode.CREATE)

    def _on_form_back_button_clicked(self):
        self._reset_form()
        self._view.categories_stacked_widget.setCurrentIndex(self.LIST_PAGE)

    def _on_form_button_clicked(self):
        form = self._view.category_form_page

        title = form.title_input.text().strip()
        description = form.description_input.toPlainText().strip()

        if not self._validate_and_show_errors(title, description):
            return

        if self._form_mode == FormMode.CREATE:
            self._service.create_category(
                title,
                description
            )

        elif self._form_mode == FormMode.EDIT and self._editing_category:
            self._service.update_category(
                self._editing_category.id,
                title,
                description
            )

        self._emit_events()

        self._view.categories_stacked_widget.setCurrentIndex(self.LIST_PAGE)

    def _on_edit_button_clicked(self) -> None:
        if not self._editing_category:
            return

        self._open_form(FormMode.EDIT, self._editing_category)

    def _on_delete_button_clicked(self) -> None:
        if not self._editing_category:
            return

        category = self._editing_category

        reply = QMessageBox.question(self._view,"Delete category", f"Are you sure you want to delete the category:\n\n'{category.title}' ?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                self._service.delete_category(category.id)
            except ValueError as e:
                QMessageBox.critical(
                    self._view,
                    "Cannot delete category",
                    str(e)  # "Impossible to delete used category."
                )
            else:
                self._emit_events()

    ###########################
    ##### Categories List #####
    ###########################

    def load_categories(self) -> None:
        cards_layout = self._view.categories_list_page.scroll_area.cards_layout

        while cards_layout.count() > 1:
            item = cards_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        categories = self._service.get_all_categories_for_display()

        for category in categories:
            self._add_card(category)

        self._editing_category = None

        self._view.categories_list_page.header.delete_button.setEnabled(False)
        self._view.categories_list_page.header.edit_button.setEnabled(False)

    def _add_card(self, category: CategoryReadDTO) -> None:
        card = CategoryCard(category)

        card.clicked.connect(self._on_card_clicked)

        self._view.categories_list_page.scroll_area.cards_layout.insertWidget(
            self._view.categories_list_page.scroll_area.cards_layout.count() - 1,
            card
        )

    def _on_card_clicked(self, clicked_card):
        layout = self._view.categories_list_page.scroll_area.cards_layout

        clicked_was_expanded = clicked_card.expanded
        selection = None

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()

            if isinstance(widget, CategoryCard):

                if widget == clicked_card:
                    new_state = not clicked_was_expanded
                    widget.set_selected(new_state)

                    if new_state:
                        selection = widget.category
                else:
                    widget.set_selected(False)

        self._editing_category = selection

        self._update_buttons_state()

    def _update_buttons_state(self):

        enabled = self._editing_category is not None

        self._view.categories_list_page.header.edit_button.setEnabled(enabled)
        self._view.categories_list_page.header.delete_button.setEnabled(enabled)

    #################################
    ##### Reusable Form methods #####
    #################################

    def _open_form(self, mode: FormMode, category: CategoryReadDTO | None = None) -> None:
        self._form_mode = mode
        self._editing_category = category

        form = self._view.category_form_page

        if mode == FormMode.CREATE:
            form.save_button.setText("Create Category")
            self._reset_form_fields()

        elif mode == FormMode.EDIT and category:
            form.save_button.setText("Update Category")
            form.title_input.setText(category.title)
            form.description_input.setText(category.description)

        self._validate_form()
        self._view.categories_stacked_widget.setCurrentIndex(self.FORM_PAGE)

    def _reset_form(self) -> None:
        self._editing_category = None

        form = self._view.category_form_page
        form.title_input.clear()
        form.description_input.clear()
        form.save_button.setText("Save category")

    def _validate_form(self):
        form = self._view.category_form_page

        title_valid = bool(form.title_input.text().strip())
        description_valid = bool(form.description_input.toPlainText().strip())

        form.save_button.setEnabled(title_valid and description_valid)

    def _validate_and_show_errors(self, title, description) -> bool:
        form = self._view.category_form_page

        form.form_title_error.hide()
        form.form_description_error.hide()

        valid = True

        if not title:
            form.form_title_error.setText("Title is required.")
            form.form_title_error.show()
            valid = False

        if not description:
            form.form_description_error.setText("Description is required.")
            form.form_description_error.show()
            valid = False

        return valid

    def _reset_form_fields(self) -> None:
        form = self._view.category_form_page

        form.title_input.clear()
        form.description_input.clear()

        form.form_title_error.hide()
        form.form_description_error.hide()
