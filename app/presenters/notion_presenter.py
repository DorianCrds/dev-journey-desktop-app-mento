# app/presenters/notion_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QMessageBox, QCheckBox, QLabel

from app.presenters.form_mode_enum import FormMode
from app.services.category_service import CategoryService
from app.services.dto.notion_dto import NotionReadDTO
from app.services.dto.tag_dto import TagDTO
from app.services.notion_service import NotionService
from app.services.tag_service import TagService
from app.views.pages.notions.notions_card import NotionCard
from app.views.pages.notions.notions_view import NotionsView


class NotionPresenter:
    def __init__(self, view: NotionsView, notion_service: NotionService, category_service: CategoryService, tag_service: TagService):
        self._view = view
        self._notion_service = notion_service
        self._category_service = category_service
        self._tag_service = tag_service

        self._form_mode = FormMode.CREATE
        self._editing_notion: NotionReadDTO | None = None

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._view.notions_custom_list_widget.list_widget.itemSelectionChanged.connect(self._on_selection_changed)

        self._view.add_notion_button.clicked.connect(self._on_add_button_clicked)
        self._view.edit_notion_button.clicked.connect(self._on_edit_button_clicked)
        self._view.delete_notion_button.clicked.connect(self._on_delete_button_clicked)
        self._view.notions_form_page.back_button.clicked.connect(self._on_back_button_clicked)
        self._view.notions_form_page.save_button.clicked.connect(self._on_form_button_clicked)

        self._view.notions_form_page.title_input.textChanged.connect(self._validate_form)
        self._view.notions_form_page.category_input.currentIndexChanged.connect(self._validate_form)

    #########################################
    ##### Notions list widget's methods #####
    #########################################

    def load_notions(self) -> None:
        self._view.notions_custom_list_widget.list_widget.clear()
        notions = self._notion_service.get_all_notions_for_display()

        for notion in notions:
            self._add_card(notion)

        if self._view.notions_custom_list_widget.list_widget.count() > 0:
            self._view.notions_custom_list_widget.list_widget.setCurrentRow(0)

        self._update_details_and_options()

    def _add_card(self, notion: NotionReadDTO) -> None:
        item = QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole, notion)

        card = NotionCard(notion)
        item.setSizeHint(card.sizeHint())

        self._view.notions_custom_list_widget.list_widget.addItem(item)
        self._view.notions_custom_list_widget.list_widget.setItemWidget(item, card)

    def _on_selection_changed(self) -> None:
        selected_items = self._view.notions_custom_list_widget.list_widget.selectedItems()

        if not selected_items:
            self._update_details_and_options()
            return

        notion: NotionReadDTO = selected_items[0].data(Qt.ItemDataRole.UserRole)

        self._view.notions_detail_widget.title_value.setText(notion.title)
        self._view.notions_detail_widget.category_value.setText(notion.category_title)
        self._view.notions_detail_widget.context_value.setText(notion.context or "")
        self._view.notions_detail_widget.description_value.setText(notion.description or "")
        self._view.notions_detail_widget.status_value.setText(notion.status)

        self._set_details_tags(notion.tags)

        self._update_details_and_options()

    def _update_details_and_options(self) -> None:
        has_selection = bool(self._view.notions_custom_list_widget.list_widget.selectedItems())
        if not has_selection:
            details = self._view.notions_detail_widget
            details.title_value.setText("")
            details.category_value.setText("")
            details.context_value.setText("")
            details.description_value.setText("")
            details.status_value.setText("")
            self._set_details_tags([])

        self._view.edit_notion_button.setEnabled(has_selection)
        self._view.delete_notion_button.setEnabled(has_selection)

    ###############################
    ##### Buttons connections #####
    ###############################

    def _on_add_button_clicked(self) -> None:
        self._open_form(FormMode.CREATE)

    def _on_edit_button_clicked(self) -> None:
        selected_item = self._view.notions_custom_list_widget.list_widget.currentItem()
        if not selected_item:
            return

        notion = selected_item.data(Qt.ItemDataRole.UserRole)
        self._open_form(FormMode.EDIT, notion)

    def _on_delete_button_clicked(self) -> None:
        selected_item = self._view.notions_custom_list_widget.list_widget.currentItem()

        if not selected_item:
            return

        notion = selected_item.data(Qt.ItemDataRole.UserRole)

        reply = QMessageBox.question(self._view, "Delete notion",
                                     f"Are you sure you want to delete the notion:\n\n'{notion.title}' ?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self._notion_service.delete_notion(notion.id)

            self.load_notions()

    def _on_back_button_clicked(self) -> None:
        self._reset_form()
        self._view.notions_content_stacked_widget.setCurrentIndex(0)

    def _on_form_button_clicked(self) -> None:
        form = self._view.notions_form_page

        title = form.title_input.text().strip()
        category = form.category_input.currentData()
        context = form.context_input.toPlainText().strip()
        description = form.description_input.toPlainText().strip()
        tag_ids = self._get_selected_tag_ids()

        if not self._validate_and_show_errors(title, category):
            return

        if self._form_mode == FormMode.CREATE:
            self._notion_service.create_notion(
                title,
                category.id,
                context,
                description,
                tag_ids
            )

        elif self._form_mode == FormMode.EDIT and self._editing_notion:
            self._notion_service.update_notion(
                self._editing_notion.id,
                title,
                category.id,
                context,
                description,
                tag_ids,
            )

        self._after_submit()

    #################################
    ##### Details tags handling #####
    #################################

    def _set_details_tags(self, tags: list[TagDTO]) -> None:
        details = self._view.notions_detail_widget

        for label in details.tag_labels:
            label.deleteLater()
        details.tag_labels.clear()

        # Remove stretch temporarily
        details.tags_layout.takeAt(details.tags_layout.count() - 1)

        for tag in tags:
            label = QLabel(tag.title)
            details.tags_layout.addWidget(label)
            details.tag_labels.append(label)

        details.tags_layout.addStretch()

    ##############################
    ##### FORM TAGS HANDLING #####
    ##############################

    def _set_form_tags(self) -> None:
        form = self._view.notions_form_page

        for checkbox in form.tag_checkboxes:
            checkbox.deleteLater()
        form.tag_checkboxes.clear()

        tags = self._tag_service.get_all_tags()

        for tag in tags:
            checkbox = QCheckBox(tag.title)
            checkbox.setProperty("tag_id", tag.id)
            form.tags_layout.addWidget(checkbox)
            form.tag_checkboxes.append(checkbox)

    def _get_selected_tag_ids(self) -> list[int]:
        form = self._view.notions_form_page

        return [checkbox.property("tag_id") for checkbox in form.tag_checkboxes if checkbox.isChecked()]

    def _set_selected_tags(self, tag_ids: list[int]) -> None:
        form = self._view.notions_form_page
        for checkbox in form.tag_checkboxes:
            checkbox.setChecked(checkbox.property("tag_id") in tag_ids)

    #####################
    ##### Form flow #####
    #####################

    def _open_form(self, mode: FormMode, notion: NotionReadDTO | None = None) -> None:
        self._form_mode = mode
        self._editing_notion = notion

        self._populate_form_combobox()
        self._set_form_tags()

        form = self._view.notions_form_page

        if mode == FormMode.CREATE:
            form.save_button.setText("Create Notion")
            self._reset_form_fields()

        elif mode == FormMode.EDIT and notion:
            form.save_button.setText("Update Notion")
            self._fill_form_with_notion(notion)

        self._validate_form()
        self._view.notions_content_stacked_widget.setCurrentIndex(1)

    def _populate_form_combobox(self) -> None:
        categories = self._category_service.get_all_categories()

        combo = self._view.notions_form_page.category_input
        combo.clear()

        combo.addItem("Select a category...", None)

        for category in categories:
            combo.addItem(category.title, category)

        self._view.notions_form_page.save_button.setEnabled(False)

    def _fill_form_with_notion(self, notion: NotionReadDTO) -> None:
        form = self._view.notions_form_page

        form.title_input.setText(notion.title)
        form.context_input.setText(notion.context or "")
        form.description_input.setText(notion.description or "")

        combo = form.category_input
        for i in range(combo.count()):
            category = combo.itemData(i)
            if category and category.id == notion.category_id:
                combo.setCurrentIndex(i)
                break

        tag_ids = [tag.id for tag in notion.tags]
        self._set_selected_tags(tag_ids)

    def _validate_form(self) -> None:
        form = self._view.notions_form_page

        title_valid = bool(form.title_input.text().strip())
        category_valid = form.category_input.currentData() is not None

        form.save_button.setEnabled(title_valid and category_valid)

    def _validate_and_show_errors(self, title, category) -> bool:
        form = self._view.notions_form_page

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

    def _reset_form(self) -> None:
        form = self._view.notions_form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()

        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()

        form.save_button.setEnabled(False)

    def _after_submit(self) -> None:
        self._form_mode = FormMode.CREATE
        self._editing_notion = None

        self._reset_form_fields()
        self.load_notions()
        self._view.notions_content_stacked_widget.setCurrentIndex(0)

    def _reset_form_fields(self) -> None:
        form = self._view.notions_form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()
        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()
