# app/persistence/repositories/tag_repository.py
from app.persistence.db_connector import DbConnector
from app.services.dto.tag_dto import TagDTO


class TagRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_all_tags(self) -> list[dict]:
        query = "SELECT * FROM tags"
        return self._db_connector.fetch_all(query)

    def get_all_tags_with_count(self) -> list[dict]:
        query = """
                SELECT t.id, \
                       t.title, \
                       COUNT(nt.notion_id) AS notions_count
                FROM tags t
                         LEFT JOIN notions_tags nt ON t.id = nt.tag_id
                GROUP BY t.id \
                """
        return self._db_connector.fetch_all(query)

    def get_tag_by_id(self, tag_id: int) -> dict:
        query = "SELECT * FROM tags WHERE id = ?"
        return self._db_connector.fetch_one(query, (tag_id,))

    def create_tag(self, dto: TagDTO) -> int:
        query = "INSERT INTO tags (title) VALUES (?)"
        return self._db_connector.execute(query, (dto.title,))

    def update_tag(self, dto: TagDTO) -> int | None:
        query = "UPDATE tags SET title = ? WHERE id = ?"

        return self._db_connector.execute(query, (dto.title, dto.id))

    def delete_tag(self, tag_id: int) -> int:
        query = "DELETE FROM tags WHERE id = ?"
        return self._db_connector.execute(query, (tag_id,))
