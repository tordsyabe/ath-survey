from flask import Blueprint, render_template
from flask_login import current_user, login_required

dashboard_page = Blueprint('dashboard', __name__, template_folder="templates")

@dashboard_page.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html", current_user=current_user)