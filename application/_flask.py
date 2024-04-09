from flask import Flask
from application._logger import Logger


def create_flask_app(settings: dict[str, any], logger: Logger) -> Flask:
    """
    Create an instance of flask
    """
    logger.info(f"Creating flask app - {settings['name']}")
    app = Flask(settings["name"])

    if settings["debug"]:
        logger.info("Debug mode - on")
        app.debug = settings["debug"]

    return app
