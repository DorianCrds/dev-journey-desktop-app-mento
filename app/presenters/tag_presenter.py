# app/presenters/tag_presenter.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox

from app.services.dto.tag_dto import TagDTO
from app.services.tag_service import TagService
from app.ui.views.pages.tags.tags_card import TagCard, TagInputCard
from app.ui.views.pages.tags.tags_view import TagsView


class TagPresenter:
    def __init__(self, view: TagsView, tag_service: TagService):
        self._view = view
        self._service = tag_service

        self._connect_signals()
        self.load_tags()

    def _connect_signals(self) -> None:
        self._view.tags_list_page.header.add_button.clicked.connect(self._on_add_button_clicked)

    ###############################
    ##### Buttons connections #####
    ###############################

    def _on_add_button_clicked(self) -> None:
        self._show_tag_input()

    #################
    ##### Cards #####
    #################

    def load_tags(self) -> None:
        cards_layout = self._view.tags_list_page.scroll_area.cards_layout

        while cards_layout.count():
            item = cards_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        tags = self._service.get_all_tags_for_display()

        for tag in tags:
            self._add_card(tag)

        cards_layout.addStretch()

    def _add_card(self, tag: TagDTO) -> None:
        card = TagCard(tag)

        card.edit_button.clicked.connect(lambda: self._start_edit(card))
        card.delete_button.clicked.connect(lambda: self._delete_tag(card))

        card.title_label.mouseDoubleClickEvent = lambda e: self._start_edit(card)

        self._connect_edit_signals(card)

        self._view.tags_list_page.scroll_area.cards_layout.insertWidget(
            self._view.tags_list_page.scroll_area.cards_layout.count() - 1,
            card
        )

    def _connect_edit_signals(self, card: TagCard):
        card.title_input.returnPressed.connect(lambda: self._save_edit(card))
        card.title_input.editingFinished.connect(lambda: self._on_edit_focus_out(card))

        original_key_press = card.title_input.keyPressEvent

        def custom_key_press(event):
            if event.key() == Qt.Key.Key_Escape:
                self._cancel_edit(card)
            else:
                original_key_press(event)

        card.title_input.keyPressEvent = custom_key_press

    def _show_tag_input(self) -> None:
        if hasattr(self, "input_card") and self.input_card:
            return

        self.input_card = TagInputCard()

        self._view.tags_list_page.scroll_area.cards_layout.insertWidget(
            self._view.tags_list_page.scroll_area.cards_layout.count() - 1,
            self.input_card
        )

        self._connect_input_card_signals()

        self.input_card.input.setFocus()

    def _connect_input_card_signals(self):
        ic = self.input_card

        ic.input.returnPressed.connect(self._create_tag)
        ic.save_button.clicked.connect(self._create_tag)
        ic.cancel_button.clicked.connect(self._cancel_input)

        original_key_press = ic.input.keyPressEvent

        def custom_key_press(event):
            if event.key() == Qt.Key.Key_Escape:
                self._cancel_input()
            else:
                original_key_press(event)

        ic.input.keyPressEvent = custom_key_press

    def _create_tag(self):
        title = self.input_card.input.text().strip()

        if not title:
            self._cancel_input()
            return

        tag = self._service.create_tag(title)

        dto = self._service.get_tag_for_display(tag.id)

        self._remove_input_card()
        self._add_card(dto)

        self._view.refresh_notions_required.emit()

    def _cancel_input(self):
        self._remove_input_card()

    def _remove_input_card(self):
        if self.input_card:
            self.input_card.deleteLater()
            self.input_card = None

    @staticmethod
    def _start_edit(card: TagCard):
        card.set_edit_mode(True)

    def _save_edit(self, card: TagCard):
        new_title = card.title_input.text().strip()

        if not new_title:
            self._cancel_edit(card)
            return

        self._service.update_tag(card.tag.id, new_title)

        updated = self._service.get_tag_for_display(card.tag.id)

        card.tag = updated
        card.title_label.setText(updated.title)

        card.set_edit_mode(False)

        self._view.refresh_notions_required.emit()

    @staticmethod
    def _cancel_edit(card: TagCard):
        card.title_input.setText(card.tag.title)
        card.set_edit_mode(False)

    def _on_edit_focus_out(self, card: TagCard):
        if card.title_input.text().strip():
            self._save_edit(card)
        else:
            self._cancel_edit(card)

    def _delete_tag(self, card: TagCard):
        reply = QMessageBox.question(
            self._view,
            "Delete Tag",
            f"Are you sure you want to delete:\n\n'{card.tag.title}' ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self._service.delete_tag(card.tag.id)

            card.deleteLater()

        self._view.refresh_notions_required.emit()
