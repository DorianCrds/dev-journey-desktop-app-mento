# app/views/dashboard_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout

from app.views.components.sub_components.custom_text import CustomViewTitleLabel


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):
        self._main_v_layout = QVBoxLayout(self)

        self._view_label = CustomViewTitleLabel("Dashboard view")
        self._main_v_layout.addWidget(self._view_label)
        self._main_v_layout.addStretch()