import sqlite3
from sqlite3 import Connection
import sys
from flask import g

from application._constants import Constants

def create_database(settings:  Constants):
    """
    Wrapper class to support constants
    args:
        setting: env var

    return:
        func
    """

    def database(db_name: str) -> Connection:
        """
        Create a new database connection and
        store in the flask context

        args:
            db_type: master/<project_name> for accessing the database
            dn_name: db_type == <project_name> for accessing the database

        returns:
            db connection
        """
        if db_name is None:
            raise ValueError("Name must be specified")

        # returns the master db instance
        if db_name == "master":
            db = getattr(g, "_database", None)
            if db is None:

                path = settings.DATABASE.get("path", False)
                name = settings.DATABASE.get("name", False)
                db_url = f"{path}/{name}.db"
                if not path or not name:
                    sys.exit("Environment file not found")
                db = g._database = sqlite3.connect(db_url)

            return db

        is_db_conn_present = getattr(g, "is_db_conn_present", False)
        conn_db_name = getattr(g, "conn_db_name", None)

        if is_db_conn_present:
            raise DatabaseInUser("DatabaseInUse", conn_db_name)

        g.is_db_conn_present = True
        g.conn_db_name = db_name

        db = getattr(g, f"_database-{db_name}", None)
        if db is None:
            path = settings.DATABASE.get("path", False)
            db_url = f"{path}/{db_name}.db"
            if not path or not db_name:
                sys.exit("Environment file not found")
            db = g._database = sqlite3.connect(db_url)

        return db

    return database


class DatabaseInUser(Exception):
    """
    Exception when another db connection
    is present
    """

    def __init__(self, message, name) -> None:
        super().__init__(message)
        self.name = name
