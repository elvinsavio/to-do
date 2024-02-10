from flask import request, redirect, render_template
from database import create_db


def _create_new_project():
    """
    Helper function to create a new project.

    This function is called when a POST request is made to the '/new-project' route.

    Returns:
    - Redirect: Redirects to the new project page if the project is created successfully.
    - Template: Renders the 'new-project.html' template with an error message if the project
      name already exists or if there is an error creating the project.
    """
    form_data = request.form
    project_name = form_data["project-name"].strip().replace(" ", "-")
    res = create_db(project_name)
    if res == "ok":
        return redirect(f"project/{project_name}")
    if res == "already_exists":
        return render_template(
            "new-project.html",
            input=project_name,
            err=f"{form_data['project-name']} already exists",
        )
    return render_template(
        "new-project.html",
        input=project_name,
        err=f"Could not react project {form_data['project-name']}.",
    )


def new_project():
    """
    Flask route for creating a new project.

    Renders the 'new-project.html' template if a GET request is made.
    Calls the _create_new_project function if a POST request is made.

    Returns:
    - Template: Renders the 'new-project.html' template if a GET request is made.
    - Redirect or Template: Redirects to the new project page or renders the 'new-project.html'
      template with an error message if a POST request is made.
    """
    if request.method == "GET":
        return render_template("new-project.html")
    if request.method == "POST":
        return _create_new_project()
    return "not found"
