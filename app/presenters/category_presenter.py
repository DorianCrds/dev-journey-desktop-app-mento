# app/presenters/category_presenter.py
from app.services.category_service import CategoryService

class CategoryPresenter:
    def __init__(self, view, category_service: CategoryService):
        self._view = view
        self._service = category_service

        self._connect_signals()
        self.load_categories()

    def _connect_signals(self) -> None:
        self._view.create_category_requested.connect(self.create_category)
        self._view.delete_category_requested.connect(self.delete_category)
        self._view.category_selected.connect(self.show_category_details)

    def load_categories(self) -> None:
        categories = self._service.get_all_categories()
        self._view.display_categories(categories)

    def create_category(self, form_data: dict) -> None:
        try:
            self._service.create_category(
                title=form_data["title"],
                description=form_data["description"]
            )
        except ValueError as e:
            self._view.show_error(str(e))
            return

        self.load_categories()
        self._view.clear_form()

    def delete_category(self, category_id: int) -> None:
        try:
            self._service.delete_category(category_id)
        except ValueError as e:
            self._view.show_error(str(e))
            return

        self.load_categories()

    def show_category_details(self, category_id: int) -> None:
        category = self._service.get_category_by_id(category_id)
        if category is None:
            return
        self._view.display_category_details(category)
