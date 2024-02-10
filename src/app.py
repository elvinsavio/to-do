from flask import Flask, redirect, render_template, request
from methods import new_project, get_landing_page

app = Flask(__name__)


@app.route("/")
def redirect_to_new():
    return redirect("/new")


@app.route("/new")
def landing_route():
    return get_landing_page()

@app.route("/new-project", methods=["GET", "POST"])
def new_project_route():
    return new_project()
