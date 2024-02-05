from flask import Flask, redirect, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def redirect_to_new():
    return redirect('/new')


@app.route('/new')
def new_project():
    return render_template('new.html', title="New project")