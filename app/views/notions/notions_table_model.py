# app/views/notions/notions_table_model.py
from typing import List

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

from app.domain.models.notion import Notion


class NotionsTableModel(QAbstractTableModel):
    COLUMN_TITLE = 0
    COLUMN_CATEGORY = 1
    COLUMN_STATUS = 2

    HEADERS = ["Title", "Category", "Status"]

    def __init__(self, notions: List[Notion] | None = None):
        super().__init__()
        self._notions: List[Notion] = notions or []

    def rowCount(self, parent=QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self._notions)

    def columnCount(self, parent=QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return 3

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        notion = self._notions[index.row()]
        column = index.column()

        if role == Qt.DisplayRole:
            if column == self.COLUMN_TITLE:
                return notion.title

            if column == self.COLUMN_CATEGORY:
                return notion.category_id

            if column == self.COLUMN_STATUS:
                return notion.status

        return None

    def headerData(self, section: int, orientation, role: int = Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.HEADERS[section]

        return super().headerData(section, orientation, role)

    def set_notions(self, notions: List[Notion]) -> None:
        self.beginResetModel()
        self._notions = notions
        self.endResetModel()

    def get_notion_at(self, row: int) -> Notion | None:
        if 0 <= row < len(self._notions):
            return self._notions[row]
        return None

    def get_all_notions(self) -> List[Notion]:
        return self._notions.copy()
