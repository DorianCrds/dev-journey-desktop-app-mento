# app/persistence/repositories/tag_repository.py
from app.persistence.db_connector import DbConnector


class TagRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_all_tags(self) -> list[dict]:
        query = "SELECT * FROM tags"
        return self._db_connector.fetch_all(query)

    def get_tag_by_id(self, tag_id: int) -> dict:
        query = "SELECT * FROM tags WHERE id = ?"
        return self._db_connector.fetch_one(query, (tag_id,))

    def create_tag(self, title: str) -> int:
        query = "INSERT INTO tags (title) VALUES (?)"
        return self._db_connector.execute(query, (title,))

    def update_tag(self, tag_id: int, title: str) -> int | None:
        fields = []
        params = []

        if title is not None:
            fields.append("title = ?")
            params.append(title)

        if not fields:
            return None

        query = """
            UPDATE tags
            SET {', '.join(fields)}
            WHERE id = ?
        """

        params.append(tag_id)

        return self._db_connector.execute(query, tuple(params))

    def delete_tag(self, tag_id: int) -> int:
        query = "DELETE FROM tags WHERE id = ?"
        return self._db_connector.execute(query, (tag_id,))
