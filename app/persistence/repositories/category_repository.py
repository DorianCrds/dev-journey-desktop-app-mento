# app/persistence/repositories/category_repository.py
from typing import Optional

from app.persistence.db_connector import DbConnector


class CategoryRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_all_categories(self) -> list[dict]:
        query = "SELECT * FROM categories"
        return self._db_connector.fetch_all(query)

    def get_category_by_id(self, category_id: int) -> dict:
        query = "SELECT * FROM categories WHERE id = ?"
        return self._db_connector.fetch_one(query,(category_id,))

    def create_category(self, title: str, description: str) -> int:
        query = """
            INSERT INTO categories (title, description)
            VALUES (?, ?)
        """
        return self._db_connector.execute(query, (title, description))

    def update_category(self, category_id: int, title: Optional[str], description: Optional[str]) -> int | None:
        fields = []
        params = []

        if title is not None:
            fields.append("title = ?")
            params.append(title)

        if description is not None:
            fields.append("description = ?")
            params.append(description)

        if not fields:
            return None

        query = f"""
            UPDATE categories
            SET {', '.join(fields)}
            WHERE id = ?
        """

        params.append(category_id)

        return self._db_connector.execute(query, tuple(params))

    def delete_category(self, category_id: int) -> int:
        check_query = "SELECT COUNT(*) AS count FROM notions WHERE category_id = ?"
        count_row = self._db_connector.fetch_one(check_query, (category_id,))

        if count_row["count"] > 0:
            raise ValueError("Impossible to delete used category.")

        query = "DELETE FROM categories WHERE id = ?"
        return self._db_connector.execute(query, (category_id,))
