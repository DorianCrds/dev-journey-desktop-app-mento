# app/presenters/notion_presenter.py
from app.services.notion_service import NotionService


class NotionPresenter:
    def __init__(self, view, notion_service: NotionService):
        self._view = view
        self._service = notion_service

        self._connect_signals()
        self.load_notions()

    def _connect_signals(self) -> None:
        self._view.create_notion_requested.connect(self.create_notion)
        self._view.delete_notion_requested.connect(self.delete_notion)
        self._view.notion_selected.connect(self.show_notion_details)

    def load_notions(self) -> None:
        notions = self._service.get_all_notions()
        self._view.display_notions(notions)

    def create_notion(self, form_data: dict) -> None:
        try:
            self._service.create_notion(
                title=form_data["title"],
                category_id=form_data["category_id"],
                context=form_data.get("context"),
                description=form_data.get("description"),
            )
        except ValueError as e:
            self._view.show_error(str(e))
            return

        self.load_notions()
        self._view.clear_form()

    def delete_notion(self, notion_id: int) -> None:
        self._service.delete_notion(notion_id)
        self.load_notions()

    def show_notion_details(self, notion_id: int) -> None:
        notion = self._service.get_notion_by_id(notion_id)
        if notion is None:
            return

        self._view.display_notion_details(notion)
