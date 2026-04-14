# app/views/settings_view.py

from app.views.components.main_components.basic_view import BasicView


class SettingsView(BasicView):
    def __init__(self):
        super().__init__("Apply your settings")

        self._setup_ui()

    def _setup_ui(self):
        pass
