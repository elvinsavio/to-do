from datetime import datetime
from application import database, logger
from sqlite3 import IntegrityError


def create_new_project(name: str, description: str = None):
    """
    Create a new project
    args:
        name: name of project
        description: <optional> description for project
    """
    try:
        db = database("master", None)
        cursor = db.cursor()
        time_now = datetime.now()
        cursor.execute(
            """
                INSERT INTO 
                master (title, description, created_at, last_modified) 
                VALUES (?, ?, ?, ?)
            """,
            (name, description, time_now, time_now),
        )
        db.commit()
        return "ok"
    except IntegrityError as e:
        logger.error("Duplicate warning error :", e)
        return f"{name} already exists."
    except Exception as e:
        logger.error("Failed to insert into database :", e)
        return "Something went wrong!"
    finally:
        db.close()
