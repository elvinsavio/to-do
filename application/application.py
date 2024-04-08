"""
    Module to setup application
    - constants
    - logger
"""

import tomllib
import sys
from application._logger import Logger
from application._constants import Constants


def setup_application():
    """
    Sets up the application for flask
    """
    _env = _load_toml_file()
    constants = Constants(_env)
    logger = Logger(constants.LOGS)
    logger.info("Logger initialized")
    return (logger, constants)


def _load_toml_file():
    """
    Loads local env file into memory
    Application exits if not found
    """
    try:
        with open("env.toml", "rb") as f:
            data = tomllib.load(f)
            return data
    except FileNotFoundError:
        sys.exit("Environment file not found")
