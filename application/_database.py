import sys
from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from application._logger import Logger

Base = declarative_base()


class Master(Base):
    __tablename__ = "master"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    last_modified = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class Master_Database:
    def __init__(self, settings: dict[str, str], logger: Logger):
        self.path = settings["path"]
        self.name = settings["name"]
        self.logger = logger
        self.engine = None
        self.Session = None
        self._create_path_if_not_exists(self.path)
        self._connect_to_master_db()

        Base.metadata.create_all(self.engine)

    @staticmethod
    def _create_path_if_not_exists(path):
        """
        Creates the log output folder
        """
        Path(path).mkdir(parents=True, exist_ok=True)


    def _connect_to_master_db(self):
        try:
            self.engine = create_engine(f"sqlite:///{self.path}/{self.name}.db")
            self.Session = sessionmaker(bind=self.engine)
            self.logger.info("Connected to database")
        except SQLAlchemyError as e:
            self.logger.error(e)
            sys.exit("Failed to connect to database!")

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
            session = self.Session()
            new_project = Master(title=name, description=description)
            session.add(new_project)
            session.commit()
            session.close()
            return "ok"
        except SQLAlchemyError as e:
            self.logger.error(e)
            return "err"
