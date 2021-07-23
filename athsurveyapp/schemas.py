from flask_marshmallow import Marshmallow
from marshmallow import fields
from athsurveyapp.models.models import QuestionType, Survey, Question, Choice

ma = Marshmallow()


class ChoiceSchema(ma.Schema):
    class Meta:
        model = Choice
        fields = ("id", "description", "value")


class QuestionSchema(ma.Schema):
    class Meta:
        model = Question
        fields = (
            "id",
            "description",
            "is_required",
            "sequence",
            "choice",
            "question_type_id",
        )

    choice = fields.Nested(ChoiceSchema)


class QtSchema(ma.Schema):
    class Meta:
        model = QuestionType
        fields = ("id", "description", "questions")

    questions = fields.Nested(QuestionSchema, many=True)


class SurveySchema(ma.Schema):
    class Meta:
        model = Survey
        fields = ("id", "name", "description", "question_types")

    question_types = fields.Nested(QtSchema, many=True)