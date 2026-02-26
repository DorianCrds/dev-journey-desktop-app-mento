# app/persistence/repositories/dashboard_repository.py
from app.persistence.db_connector import DbConnector


class DashboardRepository:
    def __init__(self, db_connector: DbConnector):
        self._db_connector = db_connector

    def get_global_stats(self) -> dict:
        query = """
            SELECT
                COUNT(*) as total,
                SUM(CASE WHEN status = 'Acquise' THEN 1 ELSE 0 END) as acquired,
                SUM(CASE WHEN status = 'À apprendre' THEN 1 ELSE 0 END) as to_learn
            FROM notions
        """
        return self._db_connector.fetch_one(query)

    def get_category_progress(self) -> list[dict]:
        query = """
            SELECT
                c.title as category_title,
                COUNT(n.id) as total,
                SUM(CASE WHEN n.status = 'Acquise' THEN 1 ELSE 0 END) as acquired
            FROM categories c
            LEFT JOIN notions n ON n.category_id = c.id
            GROUP BY c.id
            ORDER BY c.title
        """
        return self._db_connector.fetch_all(query)
