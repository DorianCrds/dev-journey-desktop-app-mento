# app/persistence/repositories/notion_repository.py
from typing import Optional

from app.persistence.db_connector import DbConnector


class NotionRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_all_notions(self) -> list[dict]:
        query = "SELECT * FROM notions"
        return self._db_connector.fetch_all(query)

    def get_notion_by_id(self, notion_id: int) -> dict:
        query = "SELECT * FROM notions WHERE id = ?"
        return self._db_connector.fetch_one(query, (notion_id,))

    def create_notion(self, title: str, category_id: int, context: Optional[str], description: Optional[str], status: str) -> int:
        query = """
            INSERT INTO notions (title, category_id, context, description, status)
            VALUES (?, ?, ?, ?, ?)
        """
        return self._db_connector.execute(query,(title, category_id, context, description, status))

    def update_notion(
            self,
            notion_id: int,
            title: Optional[str] = None,
            context: Optional[str] = None,
            description: Optional[str] = None,
            status: Optional[str] = None,
    ) -> int | None:
        fields = []
        params = []

        if title is not None:
            fields.append("title = ?")
            params.append(title)

        if context is not None:
            fields.append("context = ?")
            params.append(context)

        if description is not None:
            fields.append("description = ?")
            params.append(description)

        if status is not None:
            fields.append("status = ?")
            params.append(status)

        if not fields:
            return None

        query = f"""
            UPDATE notions
            SET {', '.join(fields)}
            WHERE id = ?
        """
        params.append(notion_id)

        return self._db_connector.execute(query, tuple(params))

    def delete_notion(self, notion_id: int) -> int:
        query = "DELETE FROM notions WHERE id = ?"
        return self._db_connector.execute(query, (notion_id,))
