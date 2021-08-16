from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy.sql.functions import mode
from athsurveyapp.models.models import QuestionType, Survey, Question, Choice, Employee, Branch, Response, QuestionResponse, User

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
    
    
class BranchSchema(ma.Schema):
    class Meta:
        model = Branch
        fields = ("id", "name", "address")

class QuestionResponseSchema(ma.Schema):
    class Meta:
        model = QuestionResponse
        fields = ("id", "question_id", "answer", "feedback", "question")

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("id", "email", "name")

class ResponseSchema(ma.Schema):
    class Meta:
        model = Response
        fields = ("id", "date_created", "survey", "question_responses", "user")
    
    survey = fields.Nested(SurveySchema, only=('name','description', ))
    user = fields.Nested(UserSchema)
    question_responses = fields.Nested(QuestionResponseSchema, many=True)

class EmployeeSchema(ma.Schema):
    class Meta:
        model = Employee
        fields = ("id", "name", "designation", "code", "branch", "responses")
        
    branch = fields.Nested(BranchSchema)
    responses = fields.Nested(ResponseSchema, many=True)

class EmployeeByBranchSchema(ma.Schema):
    class Meta:
        model = Employee
        fields = ("id", "name", "designation", "code")
        
