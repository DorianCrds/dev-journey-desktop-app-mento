# app/presenters/notion_presenter.py

from app.core.events import AppEvents
from app.presenters.form_mode_enum import FormMode
from app.services.category_service import CategoryService
from app.services.dto.notion_dto import NotionReadDTO
from app.services.dto.tag_dto import TagDTO
from app.services.notion_service import NotionService
from app.services.tag_service import TagService
from app.views.components.sub_components.custom_dialogs import CustomDialog
from app.views.components.sub_components.custom_forms import CustomFormCheckBox
from app.views.components.sub_components.custom_texts import CustomStatusToLearn, CustomStatusAcquired, \
    CustomTagLabel
from app.views.pages.notions.notion_card import NotionCard
from app.views.pages.notions.notions_view import NotionsView


class NotionPresenter:
    LIST_PAGE = 0
    DETAIL_PAGE = 1
    FORM_PAGE = 2

    def __init__(self, view: NotionsView, events: AppEvents, notion_service: NotionService, category_service: CategoryService, tag_service: TagService):
        self._view = view
        self._events = events
        self._notion_service = notion_service
        self._category_service = category_service
        self._tag_service = tag_service

        self._form_mode = FormMode.CREATE
        self._editing_notion: NotionReadDTO | None = None

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._events.notions_changed.connect(self.refresh_view)

        # List
        self._view.notions_list_page.header.add_button.clicked.connect(self._on_add_button_clicked)

        # Detail
        self._view.notion_detail_page.header_widget.back_button.clicked.connect(self._on_detail_back_clicked)
        self._view.notion_detail_page.header_widget.edit_button.clicked.connect(self._on_edit_button_clicked)
        self._view.notion_detail_page.header_widget.delete_button.clicked.connect(self._on_delete_button_clicked)

        # Form
        self._view.notion_form_page.header_widget.back_button.clicked.connect(self._on_form_back_clicked)
        self._view.notion_form_page.save_button.clicked.connect(self._on_form_button_clicked)

        self._view.notion_form_page.title_input.textChanged.connect(self._validate_form)
        self._view.notion_form_page.category_input.currentIndexChanged.connect(self._validate_form)

    def _emit_events(self):
        self._events.notions_changed.emit()
        self._events.categories_changed.emit()
        self._events.tags_changed.emit()
        self._events.dashboard_changed.emit()

    #########################################
    ##### Notions list widget's methods #####
    #########################################

    def load_notions(self) -> None:
        cards_layout = self._view.notions_list_page.scroll_area.cards_layout

        while cards_layout.count() > 1:
            item = cards_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        notions = self._notion_service.get_all_notions_for_display()

        for notion in notions:
            self._add_card(notion)

        self._editing_notion = None

    def _add_card(self, notion: NotionReadDTO) -> None:
        card = NotionCard(notion)

        card.clicked.connect(self._on_card_clicked)

        self._view.notions_list_page.scroll_area.cards_layout.insertWidget(
            self._view.notions_list_page.scroll_area.cards_layout.count() - 1,
            card
        )

    def _on_card_clicked(self, clicked_card: NotionCard) -> None:

        notion: NotionReadDTO = clicked_card.notion

        self._show_notion_details(notion)

        self._view.notions_stacked_widget.setCurrentIndex(self.DETAIL_PAGE)

    ###############################
    ##### Buttons connections #####
    ###############################

    def _on_add_button_clicked(self) -> None:
        self._open_form(FormMode.CREATE)

    def _on_detail_back_clicked(self) -> None:
        self._view.notions_stacked_widget.setCurrentIndex(self.LIST_PAGE)

    def _on_edit_button_clicked(self) -> None:
        if not self._editing_notion:
            return

        self._open_form(FormMode.EDIT, self._editing_notion)

    def _on_delete_button_clicked(self) -> None:

        notion = self._editing_notion

        if not notion:
            return

        if CustomDialog.confirm(
            self._view,
            "Delete notion",
            f"Are you sure you want to delete:\n\n'{notion.title}' ?",
        ):
            self._notion_service.delete_notion(notion.id)

            self._view.notions_stacked_widget.setCurrentIndex(self.LIST_PAGE)

            self._emit_events()

    def _on_form_button_clicked(self) -> None:
        form = self._view.notion_form_page

        title = form.title_input.text().strip()
        category = form.category_input.currentData()
        context = form.context_input.toPlainText().strip()
        description = form.description_input.toPlainText().strip()
        tag_ids = self._get_selected_tag_ids()

        if not self._validate_and_show_errors(title, category):
            return

        created_notion_id = None

        if self._form_mode == FormMode.CREATE:
            notion = self._notion_service.create_notion(
                title,
                category.id,
                context,
                description,
                tag_ids
            )
            created_notion_id = notion.id

        elif self._form_mode == FormMode.EDIT and self._editing_notion:
            self._notion_service.update_notion(
                self._editing_notion.id,
                title,
                category.id,
                context,
                description,
                tag_ids,
            )
            created_notion_id = self._editing_notion.id

        self._after_submit(created_notion_id)

        self._emit_events()

    def _on_form_back_clicked(self) -> None:
        self._reset_form()

        if self._form_mode == FormMode.CREATE:
            self._view.notions_stacked_widget.setCurrentIndex(self.LIST_PAGE)

        elif self._form_mode == FormMode.EDIT:
            self._view.notions_stacked_widget.setCurrentIndex(self.DETAIL_PAGE)

    ########################
    ##### Details flow #####
    ########################
    def _show_notion_details(self, notion: NotionReadDTO) -> None:

        details = self._view.notion_detail_page

        details.title_value.setText(notion.title)

        details.category_value.setText(notion.category_title)

        details.context_value.setText(notion.context or "")
        details.description_value.setText(notion.description or "")

        self._set_details_status(notion.status)
        self._set_details_tags(notion.tags)

        self._editing_notion = notion

    def _set_details_status(self, status: str) -> None:

        details = self._view.notion_detail_page

        for i in reversed(range(details.status_layout.count())):
            widget = details.status_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if status == "À apprendre":
            badge = CustomStatusToLearn(status)
        else:
            badge = CustomStatusAcquired(status)

        details.status_layout.addWidget(badge)

    def _set_details_tags(self, tags: list[TagDTO]) -> None:

        details = self._view.notion_detail_page

        for label in details.tag_labels:
            label.deleteLater()

        details.tag_labels.clear()

        while details.tags_layout.count():
            item = details.tags_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for tag in tags:
            label = CustomTagLabel(tag.title)
            details.tags_layout.addWidget(label)
            details.tag_labels.append(label)

        details.tags_layout.addStretch()

    def _clear_detail_view(self) -> None:

        details = self._view.notion_detail_page

        details.title_value.setText("")
        details.category_value.setText("")
        details.context_value.setText("")
        details.description_value.setText("")

        for i in reversed(range(details.status_layout.count())):
            widget = details.status_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for label in details.tag_labels:
            label.deleteLater()

        details.tag_labels.clear()

        while details.tags_layout.count():
            item = details.tags_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        details.tags_layout.addStretch()

    ##############################
    ##### FORM TAGS HANDLING #####
    ##############################

    def _set_form_tags(self) -> None:
        form = self._view.notion_form_page

        for checkbox in form.tag_checkboxes:
            checkbox.deleteLater()
        form.tag_checkboxes.clear()

        tags = self._tag_service.get_all_tags()

        for tag in tags:
            checkbox = CustomFormCheckBox(tag.title)
            checkbox.setProperty("tag_id", tag.id)
            form.tags_layout.addWidget(checkbox)
            form.tag_checkboxes.append(checkbox)

    def _get_selected_tag_ids(self) -> list[int]:
        form = self._view.notion_form_page

        return [checkbox.property("tag_id") for checkbox in form.tag_checkboxes if checkbox.isChecked()]

    def _set_selected_tags(self, tag_ids: list[int]) -> None:
        form = self._view.notion_form_page
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

        form = self._view.notion_form_page

        if mode == FormMode.CREATE:
            form.save_button.setText("Create Notion")
            self._reset_form_fields()
            self._clear_detail_view()

        elif mode == FormMode.EDIT and notion:
            form.save_button.setText("Update Notion")
            self._fill_form_with_notion(notion)

        self._validate_form()
        self._view.notions_stacked_widget.setCurrentIndex(self.FORM_PAGE)

    def _populate_form_combobox(self) -> None:
        categories = self._category_service.get_all_categories()

        combo = self._view.notion_form_page.category_input
        combo.clear()

        combo.addItem("Select a category...", None)

        for category in categories:
            combo.addItem(category.title, category)

        self._view.notion_form_page.save_button.setEnabled(False)

    def _fill_form_with_notion(self, notion: NotionReadDTO) -> None:
        form = self._view.notion_form_page

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
        form = self._view.notion_form_page

        title_valid = bool(form.title_input.text().strip())
        category_valid = form.category_input.currentData() is not None

        form.save_button.setEnabled(title_valid and category_valid)

    def _validate_and_show_errors(self, title, category) -> bool:
        form = self._view.notion_form_page

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
        form = self._view.notion_form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()

        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()

        form.save_button.setEnabled(False)

    def _after_submit(self, notion_id: int | None) -> None:
        self._form_mode = FormMode.CREATE

        if notion_id:
            notion = self._notion_service.get_notion_for_display(notion_id)

            if notion:
                self._show_notion_details(notion)

        self._view.notions_stacked_widget.setCurrentIndex(self.DETAIL_PAGE)

    def _reset_form_fields(self) -> None:
        form = self._view.notion_form_page

        form.title_input.clear()
        form.context_input.clear()
        form.description_input.clear()
        form.category_input.setCurrentIndex(0)

        form.form_title_error.hide()
        form.form_category_error.hide()

    def refresh_view(self) -> None:
        self.load_notions()
        self._clear_detail_view()
        self._view.notions_stacked_widget.setCurrentIndex(self.LIST_PAGE)