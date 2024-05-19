from flask import Blueprint, render_template, request, redirect

from libs import parser
import models.projects as p
from application import constants

_projects = Blueprint(
    "projects_bp",
    __name__,
    template_folder="../templates/projects",
    url_prefix="/projects",
)


@_projects.route("/new", methods=["GET"])
def new_project_form():
    """
    Handler for create project page

    request:
        None

    response:
        Renders the page
    """
    return render_template("new.html")


@_projects.route("/new", methods=["POST"])
def create_project():
    """
    Handler for create projects form

    request:
        project_name: name of project
        description: <optional> description for project

    response:
        renders the page new project page
        renders the page new project page with errors
        redirects to the new created project
    """
    form_data = request.form
    project_name = form_data.get("name", False)
    description = form_data.get("description", False)

    if not project_name:
        return render_template("new.html", error="Name is required")

    url = parser.name_to_url_safe(project_name)

    # checks if name is same as master db name
    master_db_name = constants.DATABASE.get("name", None)
    if project_name == master_db_name:
        return render_template("new.html", error=f"Name cannot be {master_db_name}")

    res = p.create_new_project(name=url, description=description)
    if res == "ok":
        return redirect(f"/project/{url}/")

    return render_template("new.html", error=res)


@_projects.route("/all", methods=["GET"])
def view_all_project():
    """
    Handler for create project page

    request:
        None

    response:
        Renders the page
    """
    result = p.get_all_projects()
    return render_template("all.html", projects=result)



@_projects.route("/<name>/delete", methods=["GET"])
def delete_project(name: str):
    res = p.delete_project(name)
    if res[0]:
        return redirect("/")
    return render_template()