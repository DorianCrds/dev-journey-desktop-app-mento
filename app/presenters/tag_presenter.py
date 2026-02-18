# app/presenters/tag_presenter.py
from app.services.tag_service import TagService

class TagPresenter:
    def __init__(self, view, tag_service: TagService):
        self._view = view
        self._service = tag_service

        self._connect_signals()
        self.load_tags()

    def _connect_signals(self) -> None:
        pass

    def load_tags(self) -> None:
        pass
