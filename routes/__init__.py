from flask import Flask, render_template
from routes.projects import _projects
from models import projects


def create_routes(app: Flask):
    """
    Create flask endpoints and returns flask instance
    """

    app.register_blueprint(_projects)

    @app.route("/", methods=["GET"])
    def landing_page():
        data = projects.get_all_projects(5)
        return render_template("landing.html", projects=data)

    return app
