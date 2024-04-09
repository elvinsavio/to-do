import sqlite3
from pathlib import Path
from application._logger import Logger
import sys


class Master_Database:
    def __init__(self, settings: dict[str, str], logger: Logger):
        self.path = settings["path"]
        self.name = settings["name"]
        self.logger = logger
        self.conn = None
        self.cursor = None
        self._connect_to_master_db()

        self._create_path_if_not_exists(self.path)
        self._create_master_tables()

    def _connect_to_master_db(self):
        try:
            self.conn = sqlite3.connect(f"{self.path}/{self.name}.db")
            self.cursor = self.conn.cursor()
            self.logger.info("Connected to database")
        except sqlite3.Error as e:
            self.logger.error(e)
            sys.exit("Failed to connect to database!")

    @staticmethod
    def _create_path_if_not_exists(path):
        """
        Creates the log output folder
        """
        Path(path).mkdir(parents=True, exist_ok=True)

    def _create_master_tables(self):
        """
        Create tables if not exists
        """
        try:
            self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS master (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            title TEXT UNIQUE,
                            description TEXT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );"""
            )
        except sqlite3.Error as e:
            self.logger.error(e)
            sys.exit("Failed to create tables")

    def create_project(self, name: str, description: str):
        """
        Inserts a new row into the master db
        args: 
            name: str - name of project
            description: str - some description of the project
        return:
            ok, err
        """
        try:
            self.cursor.execute(
                f"INSERT INTO your_table (title, description) VALUES ({name}, {description})"
            )
            self.conn.commit()
            return "ok"
        except sqlite3.Error as e:
            self.logger.error(e)
            return "err"
