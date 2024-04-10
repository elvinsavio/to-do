from flask import Blueprint, render_template, request

projects = Blueprint(
    "projects_bp",
    __name__,
    template_folder="../templates/projects",
    url_prefix="/projects",
)


@projects.route("/new", methods=["GET"])
def new_project():
    return render_template("new.html")


@projects.route("/new", methods=["POST"])
def create_project():
    form_data = request.form
    project_name = form_data.get("name", False)
    if not project_name:
        return render_template("new.html", error="Name is required")

    

    return render_template("new.html")