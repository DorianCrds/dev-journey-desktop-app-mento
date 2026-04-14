# app/views/infos_view.py

from app.views.components.main_components.basic_view import BasicView


class InfosView(BasicView):
    def __init__(self):
        super().__init__("Informations view")

        self._setup_ui()

    def _setup_ui(self):
        pass