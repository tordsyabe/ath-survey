from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from athsurveyapp.models.models import db, Branch


class QuestionTypeForm(FlaskForm):

    qt_description = StringField("Description", validators=[DataRequired()])
