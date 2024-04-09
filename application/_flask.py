from flask import Flask


def create_flask_app(settings):
    """
        Create an instance of flask
    """
    app = Flask(settings["name"])

    return app
