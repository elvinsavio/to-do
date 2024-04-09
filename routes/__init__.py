from flask import Flask, render_template


def create_routes(app: Flask):
    """
    Create flask endpoints and returns flask instance
    """

    @app.route("/", methods=["GET"])
    def landing_page():
        return render_template("landing.html", name="elvin")

    return app
