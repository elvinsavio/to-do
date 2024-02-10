from flask import render_template
from database import get_existing_db


def get_landing_page():
    """
    Retrieve the list of existing database projects and render the landing page template.

    Returns:
    - Template: Renders the 'landing.html' template with the list of existing projects.
    """
    res = get_existing_db()
    return render_template("landing.html", existing_projects=res)
