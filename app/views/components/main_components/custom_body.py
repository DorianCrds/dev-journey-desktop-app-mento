from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStackedWidget

from app.views.pages.categories.categories_view import CategoriesView
from app.views.dashboard_view import DashboardView
from app.views.infos_view import InfosView
from app.views.pages.notions.notions_view import NotionsView
from app.views.settings_view import SettingsView
from app.views.pages.tags.tags_view import TagsView


class CustomBody(QStackedWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

        self.setStyleSheet(
            """
                #body {
                    border: 1px solid gray;
                    border-radius: 7px;
                }
            """
        )

    def _setup_ui(self):
        self.setObjectName("body")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.dashboard_view = DashboardView()
        self.addWidget(self.dashboard_view)

        self.notions_view = NotionsView()
        self.addWidget(self.notions_view)

        self.categories_view = CategoriesView()
        self.addWidget(self.categories_view)

        self.tags_view = TagsView()
        self.addWidget(self.tags_view)

        self.infos_view = InfosView()
        self.addWidget(self.infos_view)

        self.settings_view = SettingsView()
        self.addWidget(self.settings_view)

        self.setCurrentIndex(1)
