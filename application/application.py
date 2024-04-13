"""
    Module to setup application
    - constants
    - logger
"""
from application._logger import Logger
from application._constants import Constants
from application._flask import create_flask_app
from routes import create_routes


def setup_application():
    """
    Sets up the application for flask
    """
    constants = Constants()
    logger = Logger(constants.LOGS)
    flask = create_flask_app(constants.APPLICATION, logger)
    flask = create_routes(flask)

    return (logger, constants, flask)
