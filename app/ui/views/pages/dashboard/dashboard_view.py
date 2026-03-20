# app/ui//views/pages/dashboard_view.py
from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.ui.views.components.main_components.basic_view import BasicView


class DashboardView(BasicView):
    def __init__(self):
        super().__init__("Dashboard")

        self._setup_ui()

    def _setup_ui(self):
        self.dashboard_cards_layout = QHBoxLayout()

        self._dashboard_charts_container = QWidget()
        self.dashboard_charts_h_layout = QHBoxLayout(self._dashboard_charts_container)

        self.content_layout.addLayout(self.dashboard_cards_layout)
        self.content_layout.addWidget(self._dashboard_charts_container)
