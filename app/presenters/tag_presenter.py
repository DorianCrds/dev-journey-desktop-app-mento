# app/presenters/tag_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QMessageBox

from app.domain.models.tag import Tag
from app.presenters.form_mode_enum import FormMode
from app.services.tag_service import TagService
from app.views.pages.tags.tags_card import TagCard
from app.views.pages.tags.tags_view import TagsView


class TagPresenter:
    def __init__(self, view: TagsView, tag_service: TagService):
        self._view = view
        self._service = tag_service

        self._form_mode = FormMode.CREATE
        self._editing_tag: Tag | None = None

        self._connect_signals()
        self.load_tags()

    def _connect_signals(self) -> None:
        self._view.add_tag_button.clicked.connect(self._on_add_button_clicked)
        self._view.edit_tag_button.clicked.connect(self._on_edit_button_clicked)
        self._view.delete_tag_button.clicked.connect(self._on_delete_button_clicked)
        self._view.tags_back_button.clicked.connect(self._on_back_button_clicked)
        self._view.tags_form_button.clicked.connect(self._on_form_button_clicked)

        self._view.tags_list_widget.itemSelectionChanged.connect(self._on_selection_changed)

        self._view.tag_name_input.textChanged.connect(self._validate_form)

    ###############################
    ##### Buttons connections #####
    ###############################

    def _on_add_button_clicked(self) -> None:
        self._open_form(FormMode.CREATE)

    def _on_edit_button_clicked(self) -> None:
        selected_item = self._view.tags_list_widget.currentItem()
        if not selected_item:
            return

        tag = selected_item.data(Qt.ItemDataRole.UserRole)
        self._open_form(FormMode.EDIT, tag)

    def _on_delete_button_clicked(self) -> None:
        selected_item = self._view.tags_list_widget.currentItem()
        if not selected_item:
            return

        tag = selected_item.data(Qt.ItemDataRole.UserRole)
        reply = QMessageBox.question(self._view, "Delete tag",
                                     f"Are you sure you want to delete the tag:\n\n'{tag.title}' ?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self._service.delete_tag(tag.id)

            self.load_tags()

    def _on_back_button_clicked(self) -> None:
        self._view.tag_name_input.clear()
        self._view.form_tag_name_error.hide()
        self._view.tags_form_button.setEnabled(False)

        self._view.tags_stacked_widget.setCurrentIndex(0)

    def _on_form_button_clicked(self) -> None:
        title = self._view.tag_name_input.text().strip()

        if not title:
            self._view.form_tag_name_error.setText("Title is required.")
            self._view.form_tag_name_error.show()
            return

        if self._form_mode == FormMode.CREATE:
            self._service.create_tag(title)

        elif self._form_mode == FormMode.EDIT and self._editing_tag:
            self._editing_tag.update_title(title)

            self._service.update_tag(self._editing_tag)

        self._after_submit()

    #######################
    ##### List widget #####
    #######################

    def load_tags(self) -> None:
        self._view.tags_list_widget.clear()
        tags = self._service.get_all_tags()

        for tag in tags:
            self._add_card(tag)

        if self._view.tags_list_widget.count() > 0:
            self._view.tags_list_widget.setFocus()
            self._view.tags_list_widget.setCurrentRow(0)

        self._update_details_and_options()

    def _add_card(self, tag: Tag) -> None:
        item = QListWidgetItem()

        item.setData(Qt.ItemDataRole.UserRole, tag)

        card = TagCard(tag)

        item.setSizeHint(card.sizeHint())

        self._view.tags_list_widget.addItem(item)
        self._view.tags_list_widget.setItemWidget(item, card)

    def _on_selection_changed(self) -> None:
        selected_items = self._view.tags_list_widget.selectedItems()

        if not selected_items:
            self._update_details_and_options()
            return

        tag = selected_items[0].data(Qt.ItemDataRole.UserRole)

        self._view.value.setText(tag.title)

        self._update_details_and_options()

    def _update_details_and_options(self) -> None:
        has_selection = bool(self._view.tags_list_widget.selectedItems())
        if not has_selection:
            self._view.value.setText("")
        self._view.edit_tag_button.setEnabled(has_selection)
        self._view.delete_tag_button.setEnabled(has_selection)

    #################################
    ##### Reusable Form methods #####
    #################################

    def _open_form(self, mode: FormMode, tag: Tag | None = None) -> None:
        self._form_mode = mode
        self._editing_tag = tag

        if mode == FormMode.CREATE:
            self._view.tags_form_button.setText("Create Tag")
            self._reset_form_fields()

        elif mode == FormMode.EDIT and tag:
            self._view.tags_form_button.setText("Update Tag")
            self._view.tag_name_input.setText(tag.title)

        self._validate_form()
        self._view.tags_stacked_widget.setCurrentIndex(1)

    def _validate_form(self) -> None:
        title_valid = bool(self._view.tag_name_input.text().strip())
        self._view.tags_form_button.setEnabled(title_valid)

    def _after_submit(self) -> None:
        self._form_mode = FormMode.CREATE
        self._editing_tag = None

        self._reset_form_fields()

        self.load_tags()
        self._view.tags_stacked_widget.setCurrentIndex(0)

    def _reset_form_fields(self) -> None:
        self._view.tag_name_input.clear()
        self._view.form_tag_name_error.hide()