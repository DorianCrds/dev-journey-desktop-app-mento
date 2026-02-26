# app/persistence/repositories/notion_repository.py
from app.persistence.db_connector import DbConnector
from app.services.dto.notion_dto import NotionDTO


class NotionRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_all_notions(self) -> list[dict]:
        query = """
                SELECT n.*,
                       c.title AS category_title
                FROM notions n
                JOIN categories c ON c.id = n.category_id
                """
        return self._db_connector.fetch_all(query)

    def get_notion_by_id(self, notion_id: int) -> dict | None:
        query = """
                SELECT n.*,
                       c.title AS category_title
                FROM notions n
                JOIN categories c ON c.id = n.category_id
                WHERE n.id = ?
                """
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

    def get_tags_for_notion(self, notion_id: int) -> list[dict]:
        query = """
            SELECT t.*
            FROM tags t
            JOIN notions_tags nt ON nt.tag_id = t.id
            WHERE nt.notion_id = ?
        """
        return self._db_connector.fetch_all(query, (notion_id,))

    def set_tags_for_notion(self, notion_id: int, tag_ids: list[int]) -> None:
        delete_query = "DELETE FROM notions_tags WHERE notion_id = ?"
        self._db_connector.execute(delete_query, (notion_id,))

        insert_query = """
            INSERT INTO notions_tags (notion_id, tag_id)
            VALUES (?, ?)
        """

        for tag_id in tag_ids:
            self._db_connector.execute(insert_query, (notion_id, tag_id))