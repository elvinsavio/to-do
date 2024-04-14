import sqlite3
from sqlite3 import Connection
import sys
from flask import g


def create_database(settings: dict[str, str]):
    """
    Wrapper class to support constants
    args:
        setting: env var

    return:
        func
    """

    def database(db_type: str, db_name: str) -> Connection:
        """
        Create a new database connection and
        store in the flask context

        args:
            db_type: master/<project_name> for accessing the database
            dn_name: db_type == <project_name> for accessing the database

        returns:
            db connection
        """
        if db_type == "master":
            db = getattr(g, "_database", None)
            if db is None:

                path = settings.get("path", False)
                name = settings.get("name", False)
                db_url = f"{path}/{name}.db"
                if not path or not name:
                    sys.exit("Environment file not found")
                db = g._database = sqlite3.connect(db_url)

            return db
        elif db_type == "project":
            ...

    return database
