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
from app.views.main_window import MainWindow


class MainPresenter:
    def __init__(self, main_view: MainWindow):
        self._view = main_view

        self._setup_connections()

        db = DbConnector()

        notion_repo = NotionRepository(db)
        notion_service = NotionService(notion_repo)

        category_repo = CategoryRepository(db)
        category_service = CategoryService(category_repo)

        tag_repo = TagRepository(db)
        tag_service = TagService(tag_repo)

        self._notion_presenter = NotionPresenter(
            view=self._view.body.notions_view,
            notion_service=notion_service,
            category_service=category_service,
            tag_service=tag_service,
        )

        self._category_presenter = CategoryPresenter(
            view=self._view.body.categories_view,
            category_service=category_service,
        )

        self._tag_presenter = TagPresenter(
            view=self._view.body.tags_view,
            tag_service=tag_service,
        )

    def _setup_connections(self) -> None:
        self._view.menu.dashboard_button.clicked.connect(self._dashboard_menu_button_clicked)
        self._view.menu.notions_button.clicked.connect(self._notions_menu_button_clicked)
        self._view.menu.categories_button.clicked.connect(self._categories_menu_button_clicked)
        self._view.menu.tags_button.clicked.connect(self._tags_menu_button_clicked)
        self._view.menu.infos_button.clicked.connect(self._infos_menu_button_clicked)
        self._view.menu.settings_button.clicked.connect(self._settings_menu_button_clicked)

    def _dashboard_menu_button_clicked(self) -> None:
        self._view.body.setCurrentIndex(0)

    def _notions_menu_button_clicked(self) -> None:
        self._view.body.setCurrentIndex(1)

    def _categories_menu_button_clicked(self) -> None:
        self._view.body.setCurrentIndex(2)

    def _tags_menu_button_clicked(self) -> None:
        self._view.body.setCurrentIndex(3)

    def _infos_menu_button_clicked(self) -> None:
        self._view.body.setCurrentIndex(4)

    def _settings_menu_button_clicked(self) -> None:
        self._view.body.setCurrentIndex(5)
