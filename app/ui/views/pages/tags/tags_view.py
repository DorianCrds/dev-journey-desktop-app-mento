# app/ui/views/pages/tags/tags_view.py
from app.ui.views.components.main_components.basic_view import BasicView
from app.ui.views.components.sub_components.custom_list_page import CustomListPage


class TagsView(BasicView):
    def __init__(self):
        super().__init__("Handle available Tags")

        self._setup_ui()

    def _setup_ui(self):
        self.tags_list_page = CustomListPage()
        self.tags_list_page.header.add_button.show()

        self.content_layout.addWidget(self.tags_list_page)
