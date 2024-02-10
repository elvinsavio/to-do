import sqlite3
import os
from typing import Literal, List


def create_db(db_name: str) -> Literal["ok", "err", "already_exists"]:
    """
    Create a SQLite database with the specified name.

    Parameters:
        db_name (str): The name of the database to be created. This will be used as the filename
                       in the .db directory.

    Returns:


    Raises:
        sqlite3.Error: If there's an error connecting to the database.
    """
    db_path = r".db/"
    if not os.path.exists(db_path):
        os.makedirs(db_path)

    if os.path.exists(f"{db_path}/{db_name}.sqlite3"):
        return "already_exists"
    try:
        sqlite3.connect(database=f".db/{db_name}.sqlite3")
        return "ok"
    except sqlite3.Error:
        return "Err"


def get_existing_db() -> List[str]:
    """
    Retrieve a list of existing SQLite database files with the '.sqlite3' extension
    within the '.db/' directory and its subdirectories.

    Returns:
    - files (List[str]): List of file paths of existing SQLite database files.
    """
    files = []
    for _, _, filenames in os.walk(r".db/"):
        for filename in filenames:
            if filename.endswith(".sqlite3"):
                files.append(filename.replace(".sqlite3", "").replace("-", " "))
    return files
