from flask import Blueprint, render_template

dashboard_page = Blueprint('dashboard', __name__, template_folder="templates")

@dashboard_page.route("/")
def dashboard():
    return render_template("dashboard.html")