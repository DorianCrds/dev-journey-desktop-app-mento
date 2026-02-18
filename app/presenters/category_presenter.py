# app/presenters/category_presenter.py
from app.services.category_service import CategoryService

class CategoryPresenter:
    def __init__(self, view, category_service: CategoryService):
        self._view = view
        self._service = category_service

        self._connect_signals()
        self.load_categories()

    def _connect_signals(self) -> None:
        pass

    def load_categories(self) -> None:
        pass
