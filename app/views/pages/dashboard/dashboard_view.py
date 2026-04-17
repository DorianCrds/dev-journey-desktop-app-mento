# app/views/pages/dashboard_view.py

from PySide6.QtCharts import (
    QChart,
    QChartView,
    QBarCategoryAxis,
    QValueAxis,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy

from app.views.components.main_components.basic_view import BasicView
from qute.design_system.spacing import Spacing
from qute.manager.theme_manager import ThemeManager
from qute.design_system.typography import Typography


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


    def display_pie_chart(self, pie_series):
        pie_chart = QChart()

        tm = ThemeManager.instance()

        chart_bg = tm.get_color("charts.background")
        title_color = tm.get_color("text.primary")
        legend_color = tm.get_color("text.secondary")

        pie_chart.setTitleBrush(QBrush(title_color))

        legend = pie_chart.legend()
        legend.setFont(Typography.from_preset("meta"))
        legend.setLabelColor(legend_color)

        pie_chart.setBackgroundVisible(True)
        pie_chart.setBackgroundBrush(QBrush(chart_bg))

        pie_chart.setPlotAreaBackgroundVisible(True)
        pie_chart.setPlotAreaBackgroundBrush(QBrush(chart_bg))

        pie_chart.addSeries(pie_series)

        pie_chart.setTitle("Overall distribution")
        pie_chart.setTitleFont(Typography.from_preset("body_md"))

        pie_chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        pie_chart.legend().setFont(Typography.from_preset("meta"))

        pie_chart_view = QChartView(pie_chart)
        pie_chart_view.setMinimumHeight(400)
        pie_chart_view.setRenderHint(pie_chart_view.renderHints())

        self.dashboard_charts_h_layout.addWidget(pie_chart_view, 1)


    def display_bar_chart(self, bar_series, categories):
        bar_chart = QChart()

        tm = ThemeManager.instance()

        chart_bg = tm.get_color("charts.background")
        title_color = tm.get_color("text.primary")
        secondary_color = tm.get_color("text.secondary")
        border_color = tm.get_color("border.default")

        bar_chart.setTitleBrush(QBrush(title_color))

        legend = bar_chart.legend()
        legend.setFont(Typography.from_preset("meta"))
        legend.setLabelColor(secondary_color)

        bar_chart.setBackgroundVisible(True)
        bar_chart.setBackgroundBrush(QBrush(chart_bg))

        bar_chart.setPlotAreaBackgroundVisible(True)
        bar_chart.setPlotAreaBackgroundBrush(QBrush(chart_bg))

        bar_chart.addSeries(bar_series)
        bar_chart.setTitle("Progression by categories")
        bar_chart.setTitleFont(Typography.from_preset("body_md"))
        bar_chart.legend().setFont(Typography.from_preset("meta"))

        bar_chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)

        axis_y = QValueAxis()
        axis_y.setRange(0, 100)

        axis_x.setLabelsColor(secondary_color)
        axis_x.setLinePenColor(secondary_color)
        axis_y.setLabelsColor(secondary_color)
        axis_y.setLinePenColor(secondary_color)

        axis_x.setLabelsFont(Typography.from_preset("meta"))
        axis_y.setLabelsFont(Typography.from_preset("meta"))

        axis_x.setGridLineVisible(False)
        axis_y.setGridLineColor(border_color)

        bar_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        bar_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        bar_series.attachAxis(axis_x)
        bar_series.attachAxis(axis_y)

        bar_chart_view = QChartView(bar_chart)
        bar_chart_view.setMinimumHeight(400)
        bar_chart_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.dashboard_charts_h_layout.addWidget(bar_chart_view, 1)