import sys
import sqlite3
from flask import Flask


def register_cli_commands(app: Flask, setting: dict[str, str]):
    path = setting.get("path", False)
    name = setting.get("name", False)

    if not path or not name:
        sys.exit("Variables not found")

    @app.cli.command("init")
    def init():
        print(path)
        conn = sqlite3.connect(f"{path}/{name}.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS master (
                                        id INTEGER PRIMARY KEY,
                                        title TEXT UNIQUE,
                                        description TEXT,
                                        created_at TIMESTAMP,
                                        last_modified TIMESTAMP
                                    )''')
        conn.commit()
        conn.close()