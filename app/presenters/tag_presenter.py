# app/presenters/tag_presenter.py
from app.services.tag_service import TagService

class TagPresenter:
    def __init__(self, view, tag_service: TagService):
        self._view = view
        self._service = tag_service

        self._connect_signals()
        self.load_tags()

    def _connect_signals(self) -> None:
        self._view.create_tag_requested.connect(self.create_tag)
        self._view.delete_tag_requested.connect(self.delete_tag)
        self._view.tag_selected.connect(self.show_tag_details)

    def load_tags(self) -> None:
        tags = self._service.get_all_tags()
        self._view.display_tags(tags)

    def create_tag(self, form_data: dict) -> None:
        try:
            self._service.create_tag(title=form_data["title"])
        except ValueError as e:
            self._view.show_error(str(e))
            return

        self.load_tags()
        self._view.clear_form()

    def delete_tag(self, tag_id: int) -> None:
        self._service.delete_tag(tag_id)
        self.load_tags()

    def show_tag_details(self, tag_id: int) -> None:
        tag = self._service.get_tag_by_id(tag_id)
        if tag is None:
            return
        self._view.display_tag_details(tag)
