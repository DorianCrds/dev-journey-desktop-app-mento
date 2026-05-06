# app/persistence/db_connector.py
import shutil
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from app.utils.logger import logger
from app.utils.path import get_user_data_path, resource_path


class DbConnector:
    DB_FILENAME = "mento.db"
    SCHEMA_FILENAME = "schema.sql"

    def __init__(self):
        self.database_dir = get_user_data_path() / "database"
        self.database_dir.mkdir(parents=True, exist_ok=True)

        self.db_path = self.database_dir / self.DB_FILENAME
        self.schema_path = resource_path(Path("database") / self.SCHEMA_FILENAME)

        self._ensure_database_file()

        self._con = sqlite3.connect(str(self.db_path))
        self._con.row_factory = sqlite3.Row

        self._enable_foreign_keys()
        self._init_schema()

        logger.info(f"Database connected: {self.db_path}")

    def _ensure_database_file(self) -> None:
        if self.db_path.exists():
            return

        bundled_db_path = resource_path(Path("database") / self.DB_FILENAME)

        if bundled_db_path.exists():
            shutil.copy2(bundled_db_path, self.db_path)
            logger.info(f"Bundled database copied to user data: {self.db_path}")
        else:
            self.db_path.touch()
            logger.info(f"Empty database created: {self.db_path}")

    def _enable_foreign_keys(self) -> None:
        self._con.execute("PRAGMA foreign_keys = ON;")

    def _init_schema(self) -> None:
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Missing database schema: {self.schema_path}")

        try:
            with self.schema_path.open("r", encoding="utf-8") as f:
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

    def fetch_one(self, query: str, params: tuple = ()) -> dict | None:
        with self._cursor() as cursor:
            cursor.execute(query, params)
            row = cursor.fetchone()
            return dict(row) if row else None

    def fetch_all(self, query: str, params: tuple = ()) -> list[dict]:
        with self._cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def close(self) -> None:
        self._con.close()