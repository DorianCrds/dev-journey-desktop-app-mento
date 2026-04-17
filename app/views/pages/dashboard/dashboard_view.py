# app/views/pages/dashboard_view.py
from PySide6.QtWidgets import QWidget, QHBoxLayout

from app.views.components.main_components.basic_view import BasicView
from qute.design_system.spacing import Spacing


class DashboardView(BasicView):
    def __init__(self):
        super().__init__("Observe your progress")

        self._setup_ui()

    def _setup_ui(self):
        self.dashboard_cards_layout = QHBoxLayout()
        self.dashboard_cards_layout.setContentsMargins(Spacing.MD, 0, Spacing.MD, 0)

        self._dashboard_charts_container = QWidget()
        self.dashboard_charts_h_layout = QHBoxLayout(self._dashboard_charts_container)

        self.content_layout.addLayout(self.dashboard_cards_layout)
        self.content_layout.addWidget(self._dashboard_charts_container)
        self.content_layout.addStretch()
