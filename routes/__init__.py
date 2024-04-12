from flask import Flask, render_template
from routes.projects import _projects 

def create_routes(app: Flask):
    """
    Create flask endpoints and returns flask instance
    """

    app.register_blueprint(_projects)


    @app.route("/", methods=["GET"])
    def landing_page():
        return render_template("landing.html", name="elvin")

    return app
