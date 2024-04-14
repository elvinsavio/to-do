"""
Sets up the application for flask
"""

from application._logger import Logger
from application._constants import Constants
from application._flask import create_flask_app
from application._cli import register_cli_commands
from application._database import create_database

constants = Constants()
logger = Logger(constants.LOGS)
database = create_database(constants.DATABASE)
flask = create_flask_app(constants.APPLICATION)
register_cli_commands(flask, constants.DATABASE)
