from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from athsurveyapp.models.models import db, Branch


def skill_level_choices():
    return


class EmployeeForm(FlaskForm):

    name = StringField("Fullname", validators=[DataRequired()])
    code = StringField("Code", validators=[DataRequired()])
    designation = StringField("Designation", validators=[DataRequired()])
    branch = QuerySelectField('Branch', query_factory=lambda: db.session.query(
        Branch).all(), get_label='name', render_kw={"data-live-search": "true"})
