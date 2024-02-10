from flask import Flask
from methods import new_project, get_landing_page

app = Flask(__name__)


@app.route("/")
def landing_route():
    """
    Route for the landing page.

    Returns:
    - str: The landing page HTML content.
    """
    return get_landing_page()


@app.route("/new-project", methods=["GET", "POST"])
def new_project_route():
    """
    Route for creating a new project.

    Returns:
    - str: The response for creating a new project.
    """
    return new_project()
