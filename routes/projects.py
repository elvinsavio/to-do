from flask import Blueprint, render_template, request, redirect
import models.projects as p

_projects = Blueprint(
    "projects_bp",
    __name__,
    template_folder="../templates/projects",
    url_prefix="/projects",
)


@_projects.route("/new", methods=["GET"])
def new_project():
    return render_template("new.html")


@_projects.route("/new", methods=["POST"])
def create_project():
    form_data = request.form
    project_name = form_data.get("name", False)
    description = form_data.get("description", False)

    if not project_name:
        return render_template("new.html", error="Name is required")

    res = p.create_new_project(name=project_name, description=description)
    print(res)
    if res == "ok":
        return redirect("/")

    return render_template("new.html", error=res)
