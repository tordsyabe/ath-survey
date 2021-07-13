from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class BranchForm(FlaskForm):
    name = StringField('Branch Name', validators=[DataRequired()])
    address = StringField('Branch Address', validators=[DataRequired()])
