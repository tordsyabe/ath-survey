from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, HiddenField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from athsurveyapp.models.models import db, Survey, Choice


class SurveyForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
