from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, HiddenField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from athsurveyapp.models.models import db, Choice


class QuestionForm(FlaskForm):

    q_description = StringField("Description", validators=[DataRequired()])
    is_required = BooleanField("Is Required")
    place_number = StringField("Sequence no.", validators=[DataRequired()])
    question_type_id = HiddenField("Question Type", validators=[DataRequired()])
    choice_id = QuerySelectField(
        "Choice",
        query_factory=lambda: db.session.query(Choice).all(),
        get_label="description",
        render_kw={"data-live-search": "true"},
    )