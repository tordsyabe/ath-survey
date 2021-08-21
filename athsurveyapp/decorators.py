from functools import wraps
from flask import url_for, request, redirect
from athsurveyapp.models.models import User
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        user = User.query.get(int(current_user.id))
        if not user.is_admin:
            return redirect(url_for('survey_page.conduct_survey'))
        return f(*args, **kwargs)
    return decorated_function