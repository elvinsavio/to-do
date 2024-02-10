from flask import request, redirect, render_template
from database import create_db


def create_new_project():
    form_data = request.form
    project_name = form_data["project-name"].strip().replace(" ", "-")
    res = create_db(project_name)
    if res == "ok":
        return redirect(f"project/{project_name}")
    elif res == "already_exists":
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
