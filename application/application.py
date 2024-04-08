"""
    Module to setup application
    - constants
    - logger
"""

from application._logger import Logger
from application._constants import Constants


def setup_application():
    """
    Sets up the application for flask
    """
    constants = Constants()
    logger = Logger(constants.LOGS)
    logger.info("Application initialized (constants, logger)")
    return (logger, constants)
