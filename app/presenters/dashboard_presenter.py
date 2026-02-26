# app/presenters/dashboard_presenter.py
from PySide6.QtCharts import (
    QChart,
    QChartView,
    QPieSeries,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QValueAxis,
)
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QSizePolicy

from app.services.dashboard_service import DashboardService
from app.views.pages.dashboard.dashboard_view import DashboardView
from app.views.pages.dashboard.stat_card import StatCard


class DashboardPresenter:
    def __init__(self, view: DashboardView, dashboard_service: DashboardService):
        self._view = view
        self._service = dashboard_service

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

    def _show_empty_state(self) -> None:
        empty_card = StatCard("Dashboard", "No Notion saved.")
        self._view.dashboard_cards_layout.addWidget(empty_card)

        message = QLabel("Add notions to access your statistics.")
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setStyleSheet("font-size: 16px; padding: 40px;")

        self._view.dashboard_charts_h_layout.addWidget(message)

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

        pie_chart = QChart()
        pie_chart.addSeries(pie_series)
        pie_chart.setTitle("Overall distribution")
        pie_chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        pie_chart_view = QChartView(pie_chart)
        pie_chart_view.setMinimumHeight(300)

        pie_chart_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._view.dashboard_charts_h_layout.addWidget(pie_chart_view, 1)

    def _build_bar_chart(self, dashboard_data) -> None:
        categories_progress = dashboard_data.categories_progress

        categories = []
        values = []

        for cat in categories_progress:
            categories.append(cat.category_title)
            values.append(cat.percent)

        bar_set = QBarSet("Progression %")
        bar_set.append(values)

        bar_series = QBarSeries()
        bar_series.append(bar_set)

        bar_chart = QChart()
        bar_chart.addSeries(bar_series)
        bar_chart.setTitle("Progression by categories")
        bar_chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)

        axis_y = QValueAxis()
        axis_y.setRange(0, 100)

        bar_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        bar_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        bar_series.attachAxis(axis_x)
        bar_series.attachAxis(axis_y)

        bar_chart_view = QChartView(bar_chart)
        bar_chart_view.setMinimumHeight(300)

        bar_chart_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._view.dashboard_charts_h_layout.addWidget(bar_chart_view, 1)

    @staticmethod
    def _clear_layout(layout) -> None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
