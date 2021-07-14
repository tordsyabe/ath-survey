from flask_wtf import FlaskForm
from wtforms import StringField, QuerySelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired 

from athsurveyapp.models.models import db, QuestionType, Question, Choice

class QuestionForm(FlaskForm):
    
    description = StringField('Description', validators = [DataRequired()])
    is_required = BooleanField('Is Required')
    place_number = IntegerField('Place Number', validators = [DataRequired()])
    question_type = QuerySelectField('Branch', query_factory=lambda: db.session.query(Question).all(), get_label='description', render_kw={"data-live-search": "true"})
    choice = QuerySelectField('Choice', query_factory=lambda: db.session.query(Choice).all(), get_label='description', render_kw={"data-live-search": "true"})
    survey = IntegerField("Survey", validators=[DataRequired()])

