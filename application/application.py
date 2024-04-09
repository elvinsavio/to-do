"""
    Module to setup application
    - constants
    - logger
"""

from time import perf_counter
import os


from application._logger import Logger
from application._constants import Constants
from application._flask import create_flask_app
from application._database import Master_Database
from routes import create_routes


def setup_application():
    """
    Sets up the application for flask
    """
    start_time = perf_counter()
    os.system('cls' if os.name == 'nt' else 'clear')
    constants = Constants()
    logger = Logger(constants.LOGS)
    flask = create_flask_app(constants.APPLICATION, logger)
    flask = create_routes(flask)
    master_db = Master_Database(constants.DATABASE, logger)

    end_time = perf_counter() - start_time
    logger.info(f"Application started {end_time}s")
    return (logger, constants, flask)
