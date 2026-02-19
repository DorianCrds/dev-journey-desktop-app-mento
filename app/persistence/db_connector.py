# app/persistence/db_connector.py
import os
import sqlite3
from contextlib import contextmanager

from app.utils.logger import logger


class DbConnector:
    def __init__(self):
        db_path = os.path.join(os.path.abspath("database"), "mento.db")
        self._con = sqlite3.connect(db_path)
        self._con.row_factory = sqlite3.Row
        self._enable_foreign_keys()
        self._init_schema()

    def _enable_foreign_keys(self) -> None:
        self._con.execute("PRAGMA foreign_keys = ON;")

    def _init_schema(self) -> None:
        schema_path = os.path.join(os.path.abspath("database"), "schema.sql")
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                self._con.executescript(f.read())
            logger.info("Database schema initialized")
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            raise

    @contextmanager
    def _cursor(self):
        cursor = self._con.cursor()
        try:
            yield cursor
            self._con.commit()
        except Exception:
            self._con.rollback()
            raise
        finally:
            cursor.close()

    def execute(self, query: str, params: tuple = ()) -> int:
        with self._cursor() as cursor:
            cursor.execute(query, params)
            return cursor.lastrowid

    def fetch_one(self, query: str, params: tuple = ()) -> dict:
        with self._cursor() as cursor:
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None

    def fetch_all(self, query: str, params: tuple = ()) -> list[dict]:
        with self._cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
