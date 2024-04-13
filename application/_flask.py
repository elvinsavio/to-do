from flask import Flask


def create_flask_app(settings: dict[str, any]) -> Flask:
    """
    Create an instance of flask
    """
    app = Flask(settings["name"])

    if settings["debug"]:
        app.debug = settings["debug"]

    from routes import create_routes

    app = create_routes(app)

    return app
