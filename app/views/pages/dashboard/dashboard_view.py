# app/views/pages/dashboard_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from app.views.components.sub_components.custom_texts import CustomViewTitleLabel


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        #########################
        ##### View's layout #####
        #########################

        self._dashboard_main_v_layout = QVBoxLayout(self)

        self._dashboard_view_label = CustomViewTitleLabel("Dashboard")

        self._dashboard_content = QWidget()
        self._dashboard_content.setObjectName("dashboard_content_widget")
        self._dashboard_content_v_layout = QVBoxLayout(self._dashboard_content)

        #############################
        ##### Content's widgets #####
        #############################

        self.dashboard_cards_layout = QHBoxLayout()

        self._dashboard_charts_container = QWidget()
        self.dashboard_charts_h_layout = QHBoxLayout(self._dashboard_charts_container)

        self._dashboard_content_v_layout.addLayout(self.dashboard_cards_layout)
        self._dashboard_content_v_layout.addWidget(self._dashboard_charts_container)

        #############################
        ##### Adding to layouts #####
        #############################

        self._dashboard_main_v_layout.addWidget(self._dashboard_view_label)
        self._dashboard_main_v_layout.addWidget(self._dashboard_content)
        self._dashboard_main_v_layout.addStretch()