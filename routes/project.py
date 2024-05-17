from flask import Blueprint, render_template, request, redirect

from libs import parser
import models.project as p
from application import constants

_project = Blueprint(
    "project_bp",
    __name__,
    template_folder="../templates/project",
    url_prefix="/project",
)


@_project.route("/<name>/delete")
def delete_project(name: str):
    p.delete_project(name)
    return "ok"
