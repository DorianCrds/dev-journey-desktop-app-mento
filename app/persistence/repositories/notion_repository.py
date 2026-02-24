# app/persistence/repositories/notion_repository.py
from app.persistence.db_connector import DbConnector
from app.services.dto.notion_dto import NotionDTO


class NotionRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_all_notions(self) -> list[dict]:
        query = "SELECT * FROM notions"
        return self._db_connector.fetch_all(query)

    def get_notion_by_id(self, notion_id: int) -> dict | None:
        query = "SELECT * FROM notions WHERE id = ?"
        return self._db_connector.fetch_one(query, (notion_id,))

    def create_notion(self, dto: NotionDTO) -> int:
        query = """
            INSERT INTO notions (title, category_id, context, description, status)
            VALUES (?, ?, ?, ?, ?)
        """
        return self._db_connector.execute(query,(dto.title, dto.category_id, dto.context, dto.description, dto.status))

    def update_notion(self, dto: NotionDTO) -> int | None:
        query = """
            UPDATE notions
            SET title = ?,
                category_id = ?,
                context = ?,
                description = ?,
                status = ?
            WHERE id = ?
        """

        return self._db_connector.execute(
            query,
            (
                dto.title,
                dto.category_id,
                dto.context,
                dto.description,
                dto.status,
                dto.id,
            ),
        )

    def delete_notion(self, notion_id: int) -> int:
        query = "DELETE FROM notions WHERE id = ?"
        return self._db_connector.execute(query, (notion_id,))
