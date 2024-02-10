from database import get_existing_db
from flask import render_template


def get_landing_page():
    res = get_existing_db()
    return render_template("new.html", existing_projects=res)
