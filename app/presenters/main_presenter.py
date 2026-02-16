# app/presenters/main_presenter.py
from app.persistence.repositories.category_repository import CategoryRepository
from app.persistence.repositories.tag_repository import TagRepository
from app.presenters.category_presenter import CategoryPresenter
from app.presenters.notion_presenter import NotionPresenter
from app.presenters.tag_presenter import TagPresenter
from app.services.category_service import CategoryService
from app.services.notion_service import NotionService
from app.persistence.repositories.notion_repository import NotionRepository
from app.persistence.db_connector import DbConnector
from app.services.tag_service import TagService


class MainPresenter:
    def __init__(self, main_view):
        self._view = main_view

        db = DbConnector()
        notion_repo = NotionRepository(db)
        notion_service = NotionService(notion_repo)

        self._notion_presenter = NotionPresenter(
            view=self._view.notion_view,
            notion_service=notion_service,
        )

        category_repo = CategoryRepository(db)
        category_service = CategoryService(category_repo)

        self._category_presenter = CategoryPresenter(
            view=self._view.notion_view,
            category_service=category_service,
        )

        tag_repo = TagRepository(db)
        tag_service = TagService(tag_repo)

        self._tag_presenter = TagPresenter(
            view=self._view.notion_view,
            tag_service=tag_service,
        )