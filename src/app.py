from flask import Flask, redirect, render_template, request
from methods import create_new_project

app = Flask(__name__)


@app.route("/")
def redirect_to_new():
    return redirect("/new")


@app.route("/new")
def new_app():
    return render_template("new.html")


@app.route("/new-project", methods=["GET", "POST"])
def new_project():
    if request.method == "GET":
        return render_template("new-project.html")
    if request.method == "POST":
        return create_new_project()
