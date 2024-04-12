import sqlite3
import datetime
import sys
from pathlib import Path

class Master_Database:
    def __init__(self, settings: dict[str, str], logger):
        self.path = settings["path"]
        self.name = settings["name"]
        self.logger = logger
        self.conn = None
        self.cursor = None
        self._create_path_if_not_exists(self.path)

        # No database operations should be done in __init__

    def _create_path_if_not_exists(self, path):
        """
        Creates the log output folder
        """
        Path(path).mkdir(parents=True, exist_ok=True)

    async def connect_to_master_db(self):
        try:
            self.conn = await sqlite3.connect(f"{self.path}/{self.name}.db")
            self.cursor = self.conn.cursor()
            self.logger.info(f"Connected to database - {self.name}")
        except sqlite3.Error as e:
            self.logger.error(e)
            sys.exit(f"Failed to connect to database! - {self.name}")

    async def create_project(self, name: str, description: str):
        """
        Inserts a new row into the master db
        args:
            name: str - name of project
            description: str - some description of the project
        return:
            ok, err
        """
        try:
            await self.connect_to_master_db()  # Await the connection
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            last_modified = created_at
            self.cursor.execute("INSERT INTO master (title, description, created_at, last_modified) VALUES (?, ?, ?, ?)",
                                (name, description, created_at, last_modified))
            self.conn.commit()
            self.conn.close()
            return "ok"
        except sqlite3.Error as e:
            self.logger.error(e)
            return "err"
