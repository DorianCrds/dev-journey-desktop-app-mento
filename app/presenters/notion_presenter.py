# app/presenters/notion_presenter.py
from app.services.notion_service import NotionService


class NotionPresenter:
    def __init__(self, view, notion_service: NotionService):
        self._view = view
        self._service = notion_service

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        pass

    def load_notions(self) -> None:
        pass
