"""
    Module to setup application
    - constants
    - logger
"""
from application._logger import Logger
from application._constants import Constants
from application._flask import create_flask_app
from application._cli import register_cli_commands

def setup_application():
    """
    Sets up the application for flask
    """
    constants = Constants()
    logger = Logger(constants.LOGS)
    flask = create_flask_app(constants.APPLICATION)
    register_cli_commands(flask, constants.DATABASE)

    return (logger, constants, flask)
