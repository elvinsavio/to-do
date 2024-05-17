from flask import Flask

from application._constants import Constants


def create_flask_app(settings: Constants) -> Flask:
    """
    Create an instance of flask
    """
    app = Flask(settings.APPLICATION["name"])

    if settings.APPLICATION["debug"]:
        app.debug = settings.APPLICATION["debug"]

    from routes import create_routes

    app = create_routes(app)

    return app
