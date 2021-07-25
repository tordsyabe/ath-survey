from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, HiddenField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from athsurveyapp.models.models import db, Employee, Branch, Survey


class SurveyForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])

class ConductSurveyForm(FlaskForm):
    
     employee = QuerySelectField('Employee', query_factory=lambda: db.session.query(Employee).all(), get_label='name', render_kw={"data-live-search": "true"})
     branch = QuerySelectField('Branch', query_factory=lambda: db.session.query(Branch).all(), get_label='name', render_kw={"data-live-search": "true"})
     survey = QuerySelectField('Survey', query_factory=lambda: db.session.query(Survey).all(), get_label='name', render_kw={"data-live-search": "true"})
     