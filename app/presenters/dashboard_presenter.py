# app/presenters/dashboard_presenter.py

from PySide6.QtCharts import (
    QPieSeries,
    QBarSeries,
    QBarSet,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush

from app.core.events import AppEvents
from app.services.dashboard_service import DashboardService
from app.views.components.sub_components.empty_state_widget import EmptyStateWidget
from app.views.pages.dashboard.dashboard_view import DashboardView
from app.views.pages.dashboard.stat_card import StatCard
from qute.manager.theme_manager import ThemeManager
from qute.core.signals import theme_signals


class DashboardPresenter:
    def __init__(self, view: DashboardView, events: AppEvents, dashboard_service: DashboardService):
        self._view = view
        self._events = events
        self._service = dashboard_service

        self._events.dashboard_changed.connect(self.load_datas)
        theme_signals.theme_applied.connect(self._on_theme_changed)

        self.load_datas()

    def load_datas(self) -> None:
        dashboard_data = self._service.get_dashboard_data()

        self._clear_layout(self._view.dashboard_cards_layout)
        self._clear_layout(self._view.dashboard_charts_h_layout)

        if dashboard_data.global_stats.total == 0:
            self._show_empty_state()
            return

        self._build_stat_cards(dashboard_data)
        self._build_pie_chart(dashboard_data)
        self._build_bar_chart(dashboard_data)

    def _on_theme_changed(self, _):
        self.load_datas()

    def _show_empty_state(self) -> None:
        empty_card = EmptyStateWidget()
        empty_card.title_label.setText("No notions yet")
        empty_card.subtitle_label.setText("Start by creating your first notion to organize your knowledge.")
        self._view.dashboard_cards_layout.addWidget(empty_card)

    def _build_stat_cards(self, dashboard_data) -> None:
        global_stats = dashboard_data.global_stats

        cards = [
            StatCard("Total notions", str(global_stats.total)),
            StatCard("Acquired", str(global_stats.acquired)),
            StatCard("To learn", str(global_stats.to_learn)),
            StatCard("Progression", f"{global_stats.progression_percent} %"),
        ]

        for card in cards:
            self._view.dashboard_cards_layout.addWidget(card)

    def _build_pie_chart(self, dashboard_data) -> None:
        global_stats = dashboard_data.global_stats

        pie_series = QPieSeries()
        pie_series.append("Acquired", global_stats.acquired)
        pie_series.append("To learn", global_stats.to_learn)

        pie_series.slices()[0].setBrush(QBrush(ThemeManager.instance().get_color("charts.acquired")))
        pie_series.slices()[1].setBrush(QBrush(ThemeManager.instance().get_color("charts.to_learn")))

        for slice in pie_series.slices():
            slice.setPen(Qt.PenStyle.NoPen)

        def on_hovered(slice, state):
            slice.setExploded(state)

        pie_series.hovered.connect(on_hovered)

        self._view.display_pie_chart(pie_series)

    def _build_bar_chart(self, dashboard_data) -> None:
        categories_progress = dashboard_data.top_categories

        categories = []
        values = []

        for cat in categories_progress:
            categories.append(cat.category_title)
            values.append(cat.percent)

        bar_set = QBarSet("Progression % (top 5 notions count)")
        bar_set.append(values)

        bar_set.setColor(ThemeManager.instance().get_color("charts.acquired"))

        bar_series = QBarSeries()
        bar_series.append(bar_set)

        for bar_set in bar_series.barSets():
            bar_set.setBorderColor(Qt.transparent)

        self._view.display_bar_chart(bar_series, categories)

    @staticmethod
    def _clear_layout(layout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()