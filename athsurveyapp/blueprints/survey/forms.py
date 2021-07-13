from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from athsurveyapp.models.models import db, Survey


class SurveyForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
