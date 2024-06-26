import os

from datetime import datetime
from sqlite3 import Cursor, IntegrityError
from typing import Literal, Tuple, TypeVar

from application import database, logger, constants
from libs import parser, date


def get_projects_with_limit(
    limit: int | None = None,
) -> Tuple[Literal["ok", "err"], str | list[str]]:
    """
    Query master db and return all projects
    args:
        limit: max number of projects to return

    returns:
        List of projects
    """
    try:

        if limit is None:
            raise ValueError("Limit not specified")

        db = database("master")
        cursor: Cursor = db.cursor()
        result = cursor.execute(
            """
            SELECT title, last_modified, created_at
            FROM master 
            ORDER BY last_modified DESC
            LIMIT ?
            """,
            (limit,),
        )
        data = []
        for index, row in enumerate(result.fetchall()):
            data.append(
                {
                    "index": index,
                    "name": parser.url_to_name(row[0]),
                    "url": f"/project/{row[0]}",
                    "last_modified": row[1],
                    "created": row[2],
                }
            )
        return ("ok", data)
    except ValueError as e:
        logger.error(e)
        return ("err", "Limit not specified")  # type: ignore
    except Exception as e:
        logger.error(e)
        return ("err", "Something went wrong")
    finally:
        db.close()


def get_all_projects() -> Tuple[Literal["ok", "err"], str | list[str]]:
    """
    Query master db and return all projects
    args:

    returns:
        List of projects
    """
    try:
        db = database("master")
        cursor = db.cursor()
        # raise Exception
        result = cursor.execute(
            """
            SELECT title, last_modified, created_at
            FROM master 
            ORDER BY last_modified DESC
            """,
        )
        data = []
        for index, row in enumerate(result.fetchall()):
            data.append(
                {
                    "index": index + 1,
                    "name": parser.url_to_name(row[0]),
                    "url": f"/projects/{row[0]}",
                    "last_modified": date.parse_date("dBY", row[1]),
                    "created_at": date.parse_date("dBY", row[2]),
                }
            )
        return ("ok", data)
    except Exception as e:
        logger.error(e)
        return ("err", "Failed to get all projects")
    finally:
        db.close()


def create_new_project(
    name: str, description: str | None = None
) -> Tuple[Literal["ok", "err"], str | list[str]]:
    """
    Create a new project
    args:
        name: name of project
        description: <optional> description for project
    """
    try:
        # create an entry in the master db
        db_name = constants.DATABASE.get("name")

        db = database(db_name)
        cursor = db.cursor()

        project_db = database(name)
        project_cursor = project_db.cursor()

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

        return ("ok", "")

    except IntegrityError as e:
        logger.error("Duplicate warning error :", e)
        return ("err", f"{name} already exists.")

    except Exception as e:
        logger.error("Failed to insert into database :", e)
        return ("err", "Something went wrong!")

    finally:
        project_cursor.close()
        db.close()


def delete_project(name: str | None = None) -> Tuple[Literal["ok", "err"], str | list[str]]:
    """
    Deletes a project

    args:
        name: name of project to delete

    """
    if name is None or name == "":
        return ("err", "Failed to delete, project not found")

    db_name = constants.DATABASE.get("name")
    

    try:
        db = database(db_name)
        cursor = db.cursor()
        # raise Exception
        cursor.execute(
            f"""
                DELETE FROM {db_name}
                WHERE title=(?)
            """,
            (name),
        )

        db.commit()  

        path = constants.DATABASE["path"] + name + ".db"
        os.remove(path)


    except Exception as e:
        return ("err", "Failed to delete, project not found")
    finally:
        cursor.close()
        db.close()
        return ("ok", "")
