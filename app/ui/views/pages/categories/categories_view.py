# app/ui/views/pages/categories/categories_view.py

from PySide6.QtWidgets import QStackedWidget

from app.ui.views.components.main_components.basic_view import BasicView
from app.ui.views.pages.categories.categories_list_page import CategoriesListPage
from app.ui.views.pages.categories.category_form_page import CategoryFormPage


class CategoriesView(BasicView):
    def __init__(self):
        super().__init__("Manage Categories")

        self._setup_ui()

    def _setup_ui(self):
        self.categories_stacked_widget = QStackedWidget()

        self.categories_list_page = CategoriesListPage()
        self.category_form_page = CategoryFormPage()

        self.categories_stacked_widget.addWidget(self.categories_list_page)
        self.categories_stacked_widget.addWidget(self.category_form_page)

        self.content_layout.addWidget(self.categories_stacked_widget)
