from flask import Flask


def create_routes(app: Flask):
    """
    Create flask endpoints and returns flask instance
    """

    @app.route("/", methods=["GET"])
    def landing_page():
        return "hello world"

    return app
