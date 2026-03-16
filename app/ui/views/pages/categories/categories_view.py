# app/ui/views/pages/categories/categories_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QStackedWidget

from app.ui.views.components.sub_components.custom_texts import CustomTitleMain
from app.ui.views.pages.categories.categories_list_page import CategoriesListPage
from app.ui.views.pages.categories.category_form_page import CategoryFormPage


class CategoriesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._setupt_ui()

    def _setupt_ui(self) -> None:
        layout = QVBoxLayout(self)

        title = CustomTitleMain("Manage Categories")

        self.categories_stacked_widget = QStackedWidget()

        self.categories_list_page = CategoriesListPage()
        self.category_form_page = CategoryFormPage()

        self.categories_stacked_widget.addWidget(self.categories_list_page)
        self.categories_stacked_widget.addWidget(self.category_form_page)

        layout.addWidget(title)
        layout.addWidget(self.categories_stacked_widget)
