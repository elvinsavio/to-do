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
        res, value = projects.get_projects_with_limit(5)
        if res == "ok":
            return render_template("landing.html", projects=value)

        return render_template("landing.html", error=value)

    return app
