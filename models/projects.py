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
        # create an entry in the master db
        db = database("master")
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

        # create the projects tables
        project_db = database(name)
        project_cursor = project_db.cursor()

        # task table
        project_cursor.execute(
            """
            CREATE TABLE task (
                id INT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                type_id INT,
                priority_id INT,
                due_date TEXT,
                status TEXT,
                FOREIGN KEY (type_id) REFERENCES task_type(id),
                FOREIGN KEY (priority_id) REFERENCES task_priority(id)
            );
            """
        )

        project_cursor.execute(
            """
            CREATE TABLE priority (
                id INT PRIMARY KEY,
                name TEXT NOT NULL,
                color TEXT
            );
            """
        )

        project_cursor.execute(
            """
            CREATE TABLE type (
                id INT PRIMARY KEY,
                name TEXT NOT NULL,
                color TEXT
            );
            """
        )

        project_db.commit()
        db.commit()

        return "ok"
    
    except IntegrityError as e:
        logger.error("Duplicate warning error :", e)
        return f"{name} already exists."

    except Exception as e:
        logger.error("Failed to insert into database :", e)
        return "Something went wrong!"
    finally:
        project_cursor.close()
        db.close()
