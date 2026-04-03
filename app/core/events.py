# app/core/events.py

from PySide6.QtCore import QObject, Signal


class AppEvents(QObject):
    notions_changed = Signal()
    categories_changed = Signal()
    tags_changed = Signal()
    dashboard_changed = Signal()


events = AppEvents()